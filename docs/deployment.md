# Deployment

GitHub Pages publishes the generated `dist/` directory through `.github/workflows/pages.yml`. In repository **Settings → Pages → Build and deployment**, the source must be **GitHub Actions**.

Each push to `main` runs syntax, curriculum, backup and public portfolio checks, builds the site and deploys it. Pull requests validate and build without deploying. Use **Actions → Validate and deploy Binary Atlas → Run workflow** for a manual deployment.

All website assets use relative paths and hash routing, so the project works under `/binary-atlas/`. No Sites credentials, hosting identifiers, login integrations or runtime secrets are needed. GitHub Pages does not provide the original ChatGPT sign-in restriction.

If deployment fails, inspect the failing Actions job. Do not mark the site as deployed until the Pages job succeeds. The site has no server database; browser records require export/import backups.
