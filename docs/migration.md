# Move your existing progress

1. Open the original private Binary Atlas site in the browser where you used it.
2. Open workspace settings and choose **Export workspace**.
3. Open the GitHub Pages version and choose **Workspace settings → Import backup**.
4. Review the counts before restoring. Export the destination record first if it already contains work; restore replaces rather than merges it.
5. Verify notes, completion evidence, session history and local project reports.

The unchanged `binary-atlas-v1` key and schema 1 preserve compatibility, but data does not cross website origins automatically. GitHub cannot recover browser-only data. Keep JSON backups outside the public repository, for example in the ignored `backups/` folder.

The GitHub website is public. Local drafts stay in the browser until you deliberately commit or share them. Published reports are repository files visible to all visitors. They are not imported into local draft state.
