# Software Engineering Portfolio (GitHub Pages Ready)

A clean, high-performance, zero-dependency developer portfolio built with pure HTML5, modern CSS3, and vanilla JavaScript. 

**Zero build tools, zero Vercel/Node dependencies, and 100% free hosting directly on GitHub Pages.**

---

## 🚀 2-Minute Deployment Guide

### Option 1: Direct Repository Deployment
1. Go to [GitHub.com](https://github.com) and click **New Repository**.
2. Name the repository:
   * `<your-github-username>.github.io` *(e.g., `yashrawal.github.io`)*
3. Make sure the repository is set to **Public**.
4. Push or upload the files from this `Portfoloio_Github` folder into the root of that repo:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio release"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```
5. Go to **Settings** → **Pages** → Under **Build and deployment**, ensure Source is set to **Deploy from a branch** (`main` / `root`).
6. Your site is instantly live at:
   `https://<your-github-username>.github.io`

---

## 🛠 Features Included
- **Dark / Light Theme Toggle**: Persistent via `localStorage`.
- **Software Engineer Focused**: Highlights architecture metrics, MCP tools, and backend distributed systems.
- **Single-click Contact Action**: Copy email to clipboard + direct mailto trigger.
- **Embedded Resume Integration**: Direct link to your PDF resume.
- **Responsive Design**: Looks crisp on 4K desktops, laptops, tablets, and phones.
- **Zero Build / Zero Lock-in**: Edit HTML/CSS directly without running npm, vite, or bundlers.
