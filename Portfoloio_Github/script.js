// Disable automatic browser scroll restoration on refresh
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}

// Reset scroll to top on fresh load
window.addEventListener('load', () => {
  if (!window.location.hash) {
    window.scrollTo(0, 0);
  }
});

// Spotlight cursor tracker
const spotlight = document.getElementById('spotlight');

window.addEventListener('pointermove', (e) => {
  const { clientX, clientY } = e;
  if (spotlight) {
    spotlight.style.setProperty('--mouse-x', `${clientX}px`);
    spotlight.style.setProperty('--mouse-y', `${clientY}px`);
  }
});

// Scrollspy for navigation links
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav a');

window.addEventListener('scroll', () => {
  let current = '';
  const scrollPosition = window.scrollY + 180;

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// Smooth in-page navigation without disruptive hash locks
navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    const targetId = link.getAttribute('href');
    if (targetId && targetId.startsWith('#')) {
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({ behavior: 'smooth' });
        history.replaceState(null, '', window.location.pathname);
      }
    }
  });
});
