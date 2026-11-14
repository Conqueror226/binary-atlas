# Publish an investigation

Use `portfolio/templates/investigation.md`. Include the research question, owned or authorized scope, provenance and SHA-256, exact environment, reproducible method, observations, evidence, alternatives and limitations. Record actual outputs rather than expected results as findings.

1. Save your reviewed report as `portfolio/projects/<slug>.md`.
2. Add public evidence under `portfolio/evidence/<slug>/` and cite relative paths from the report. Text artifacts are easiest to review. Do not commit browser backups or unreviewed telemetry.
3. Add a record to `portfolio/projects.json` using the template below. Replace placeholders with actual information. Begin with `in-progress` when the work is incomplete.
4. Run `npm test` and `npm run build`. Open the Portfolio page locally and check the report and evidence links.
5. Commit and push or merge the change to `main`.

~~~json
{
  "id": "your-investigation-slug",
  "title": "Your actual investigation title",
  "question": "The specific question investigated",
  "status": "in-progress",
  "report": "projects/your-investigation-slug.md",
  "evidence": []
}
~~~

For `self-verified` status, add nonempty `provenance`, `tools`, `method`, `observations`, `limits`, and `rerun` fields plus at least one existing evidence file. A rerun should describe the date, clean environment, commands and observed outcome. The build checks references and required fields, not whether the findings are scientifically valid.

The project list intentionally starts empty. No research achievements are assumed. Exporting a local draft does not publish it by itself.
