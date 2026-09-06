"""Safe & Blazing Fast SMTP Handshake Verifier & Catch-All Detector."""
import smtplib
import socket
import random
import string
from functools import lru_cache
from typing import Tuple, Optional, List
from finding_engine.models import EmailStatus
from finding_engine.verifier.dns_check import get_mx_records


@lru_cache(maxsize=128)
def is_smtp_port_reachable(mx_server: str, port: int = 25, timeout: float = 0.8) -> bool:
    """Fast probe to check if port 25 is reachable."""
    try:
        sock = socket.create_connection((mx_server, port), timeout=timeout)
        sock.close()
        return True
    except Exception:
        return False


@lru_cache(maxsize=128)
def check_domain_catch_all(domain: str, mx_server: str, timeout: float = 1.0) -> bool:
    """Check if domain is catch-all (cached per domain)."""
    if not is_smtp_port_reachable(mx_server, 25, timeout=0.8):
        return False
    
    random_user = "chk_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    fake_email = f"{random_user}@{domain}"
    
    try:
        server = smtplib.SMTP(timeout=timeout)
        server.connect(mx_server, 25)
        server.helo("verify.local")
        server.mail("probe@verify.local")
        code, _ = server.rcpt(fake_email)
        server.quit()
        return code == 250
    except Exception:
        return False


def verify_email_smtp(
    email: str,
    domain: Optional[str] = None,
    mx_records: Optional[List[str]] = None,
    timeout: float = 1.0
) -> EmailStatus:
    """
    Verify an email address without sending an actual email.
    Steps:
    1. Extract domain & lookup MX
    2. Fast test port 25 reachability
    3. Simulate SMTP handshake (HELO -> MAIL FROM -> RCPT TO)
    """
    if "@" not in email:
        return EmailStatus(email=email, status="invalid", reason="Malformed email syntax")

    if not domain:
        domain = email.split("@")[1].strip()

    if mx_records is None:
        mx_records = get_mx_records(domain)

    if not mx_records:
        return EmailStatus(
            email=email,
            status="invalid",
            confidence=0.0,
            mx_valid=False,
            reason="No MX records found for domain"
        )

    primary_mx = mx_records[0]

    # Fast probe port 25
    if not is_smtp_port_reachable(primary_mx, 25, timeout=0.8):
        return EmailStatus(
            email=email,
            status="unverified",
            confidence=0.75,
            mx_valid=True,
            smtp_check=None,
            is_catch_all=None,
            reason="MX active; SMTP port 25 filtered by network"
        )

    # Perform handshake
    try:
        is_catch_all = check_domain_catch_all(domain, primary_mx, timeout=timeout)
        
        server = smtplib.SMTP(timeout=timeout)
        server.connect(primary_mx, 25)
        server.helo("verify.local")
        server.mail("probe@verify.local")
        code, msg = server.rcpt(email)
        server.quit()
        
        if code == 250:
            if is_catch_all:
                return EmailStatus(
                    email=email,
                    status="catch_all",
                    confidence=0.80,
                    mx_valid=True,
                    smtp_check=True,
                    is_catch_all=True,
                    reason="Mail server accepted recipient, but domain has catch-all enabled"
                )
            else:
                return EmailStatus(
                    email=email,
                    status="valid",
                    confidence=0.98,
                    mx_valid=True,
                    smtp_check=True,
                    is_catch_all=False,
                    reason="Mailbox confirmed via SMTP RCPT TO handshake"
                )
        elif code in (550, 551, 552, 553, 554):
            return EmailStatus(
                email=email,
                status="invalid",
                confidence=0.0,
                mx_valid=True,
                smtp_check=False,
                is_catch_all=False,
                reason=f"Mailbox rejected by server (code {code})"
            )
        else:
            return EmailStatus(
                email=email,
                status="risky",
                confidence=0.5,
                mx_valid=True,
                smtp_check=None,
                reason=f"Server returned response code: {code}"
            )
    except Exception as e:
        return EmailStatus(
            email=email,
            status="unverified",
            confidence=0.75,
            mx_valid=True,
            smtp_check=None,
            is_catch_all=None,
            reason=f"MX active; handshake skipped ({type(e).__name__})"
        )
