# FeedFare Landing Page

Landing page for [FeedFare](https://feedfare.app) — Walk More. Scroll Less.

## Deploy to GitHub Pages

1. Create a repo (e.g. `feedfare-landing`) on GitHub
2. Push this directory:
   ```bash
   cd landing-page
   git init
   git add .
   git commit -m "Initial landing page"
   git remote add origin git@github.com:NicholasRae/feedfare-landing.git
   git push -u origin main
   ```
3. Go to **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main` / `/ (root)`
4. If using a custom domain (`feedfare.app`):
   - Add an `A` record pointing to GitHub Pages IPs (`185.199.108-111.153`)
   - Or a `CNAME` record pointing to `nicholasrae.github.io`
   - The `CNAME` file is already included
5. Wait a few minutes — site will be live at `https://feedfare.app`

## Local Preview

```bash
npx serve .
# or
python3 -m http.server 8000
```

## Customization

- Replace `#appstore` with your real App Store link
- Replace the app icon placeholder with your actual icon
- Update testimonials in the social proof section
- Add real social media links in the footer
