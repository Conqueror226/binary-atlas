# Contributing and updating

Use one branch per lab or improvement:

~~~sh
git switch -c lab/branch-boundary
# Edit source or add your actual investigation and reviewed evidence.
npm test
npm run build
git add site scripts labs portfolio docs
git commit -m "Document branch boundary investigation"
git push -u origin lab/branch-boundary
~~~

Open a pull request to `main`, review its diff, and merge when the checks pass. Direct pushes to `main` also deploy. Commit only what exists; use in-progress status when conclusions remain uncertain.

For learning content, edit `site/data.js`. Run `npm run labs:export` to refresh the exercise guides and starter sources, then check the generated diff. Update `docs/learning-log.md` with actual work, questions and next steps.

For public investigations, follow [portfolio-workflow.md](docs/portfolio-workflow.md). Browser-only edits do not update the repository. Download a Markdown report and commit the reviewed version explicitly.
