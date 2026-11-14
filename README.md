# Binary Atlas

A hands-on learning workspace and evidence-based portfolio by **A. Kader BONZI**, exploring low-level binary analysis, reverse engineering and defensive vulnerability research.

The path builds on Python, Windows event logs, SIEM, digital forensics and identity security. C and assembly proficiency remain unassessed until practical work demonstrates them.

## Start here

- **Website:** https://conqueror226.github.io/binary-atlas/
- **Learning:** eight stages, twenty guided exercises, core concepts, official resources and comparison views. Stages 06–07 cover automated analysis (fuzzing, coverage, symbolic execution, call-graph reachability) and engineering for industry (hardening inventory, patch verification, crash triage, design brief).
- **EngD alignment:** known and unknown facts about the target position, a competency map tied to your completion records, and four candidate design directions. See [the alignment review](docs/engd-alignment.md).
- **Practice:** local notes, progress, session tracking and JSON backup import/export.
- **Portfolio:** committed public reports appear alongside your local draft workspace, with provenance, evidence and bounded conclusions.

No completed investigations or personal findings are pre-populated. Starter programs are teaching material, not completed portfolio work.

## Run locally

Requires Node.js 22+ and Python 3 for the optional preview server. No third-party package installation is needed.

~~~sh
git clone https://github.com/Conqueror226/binary-atlas.git
cd binary-atlas
npm test
npm run build
npm run preview
~~~

Open `http://localhost:8000`. Edit `site/`, then rebuild to preview changes.

## Repository map

| Path | Purpose |
| --- | --- |
| `site/` | HTML, CSS, app logic and learning content |
| `labs/` | Twenty exported exercise guides, teaching sources and small analysis scripts (Python standard library; `solve_gate.py` needs angr) |
| `portfolio/projects.json` | Index of reviewed public investigations |
| `portfolio/projects/` | Public Markdown reports |
| `portfolio/evidence/` | Reviewed evidence referenced by public reports |
| `portfolio/templates/` | Research, evidence and EngD design brief templates |
| `docs/` | Deployment, migration, contribution workflow and roadmap |
| `scripts/` | Build, curriculum checks, backup checks and lab export |
| `.github/workflows/pages.yml` | Checks on pull requests; deployment from main |

## Keep learning and publishing

1. Choose a lab and run it in your isolated lab environment.
2. Preserve actual commands, inputs, outputs, hashes, tool versions and alternative explanations.
3. Save a draft in the browser workspace, or use `portfolio/templates/investigation.md`.
4. Review the report for accuracy and public sharing. Commit it under `portfolio/projects/`, add reviewed evidence and register the project in `portfolio/projects.json`.
5. Run `npm test` and `npm run build`, then push to `main`. GitHub Actions validates and publishes the website.

See [the contribution guide](CONTRIBUTING.md), [publication workflow](docs/portfolio-workflow.md), [migration guide](docs/migration.md), and [roadmap](docs/roadmap.md).

## What is saved where?

| Record | Storage | Shared publicly? |
| --- | --- | --- |
| Learning materials and website source | GitHub commits | Yes |
| Reports registered in `portfolio/projects.json` | GitHub commits and site build | Yes |
| Notes, local project drafts and progress | Browser localStorage | No automatic upload or sync |
| JSON workspace backups | Your downloaded file | Only if you deliberately share them |


## Evidence standards

Separate observation, inference and uncertainty. Record clean reruns before self-verification. Automated checks validate structure and file references; they cannot establish the truth of a research claim. Do not present generated teaching examples as your own verified findings.

Each resource records the date its page was last checked. Resources added on 2026-11-14 that have not been opened yet are shown as **not yet checked**; consult the official sites for current requirements. Study times are estimates. The instruction trace is an illustrative unsigned x86-64 model. The site does not run native compilers or debuggers.

No redistribution license has been selected yet. Third-party tools and resources retain their own licenses.
