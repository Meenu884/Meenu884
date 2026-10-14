# Portfolio

Static portfolio (HTML, CSS, JS). No build step.

## Before you deploy
1. Find and replace `USERNAME` with your GitHub username in `index.html`, `robots.txt`, `sitemap.xml`.
2. Replace `you@example.com`, LinkedIn URL, and each project's Code / Live demo links.
3. Put your resume at `assets/Jayameenakshi_Resume.pdf`.

## Deploy to GitHub Pages
1. Create a repo named `USERNAME.github.io` (public).
2. From this folder:
   ```bash
   git init
   git add .
   git commit -m "Add portfolio"
   git branch -M main
   git remote add origin https://github.com/USERNAME/USERNAME.github.io.git
   git push -u origin main
   ```
3. Repo Settings > Pages > Source: Deploy from a branch > `main` / `(root)` > Save.
4. Live at `https://USERNAME.github.io/` in about a minute.

## Local preview
```bash
python -m http.server 8000
```

## SEO follow-up
Submit `https://USERNAME.github.io/sitemap.xml` in Google Search Console.
