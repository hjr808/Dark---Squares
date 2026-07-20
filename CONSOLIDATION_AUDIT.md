# Dark Squares Consolidation Audit

**Consolidation base:** `f9cc967927c791ca9006947ab2cb7fdd8ade2b5b` (the checked-out current main snapshot)
**Consolidation branch:** `codex/consolidate-completed-work`
**Audit date:** 2026-07-20 (UTC)

## Scope and source review

This consolidation was made from every Git ref and object available in the local
checkout. The checkout contains one reachable branch/ref (`work`) at the
consolidation base and no configured Git remote or remote-tracking refs.

The Git history records two already-merged pull requests:

- PR #1 — `organize-repository`, merged at `5dce80b`.
- PR #2 — `codex/populate-master_canon.md-with-existing-materials`, merged at
  `f9cc967`.

No open pull request or additional Codex branch was available locally to merge.
External GitHub enumeration could not be completed because outbound GitHub/API
access is blocked in this environment (HTTP 403), and no remote is configured.
Accordingly, this audit does **not** claim that an external PR list is complete;
it records the complete set that was available to this consolidation.

## Completed material retained

All files present at the base were retained unless identified below as an
incomplete duplicate. The retained package includes:

- Canon and series-bible material: `Series-Bible/MASTER_CANON.md`,
  `Series-Bible/README.md`, and `Book-1/DarkSquares_SeriesBible 2.pdf`.
- Manuscript and screenplay-related material: `Book-1/Dark-Squares-Book-1.md`,
  the Book One DOCX/PDF files, `Book-1/ED_EPISODE_21.pdf`, and
  `Screenplays/README.md`.
- Production, business, pitch, branding, and inventory material:
  `Production`, `PRODUCER_MASTER_PACKAGE.md`,
  `PRODUCER_EDITION_MATERIALS.md`, `BRAND_GUIDELINES.md`, and
  `ASSET_INVENTORY_GUIDE.md`.
- Repository structure and continuity placeholders, including Book 2, Book 3,
  Characters, Timeline, and Series-Bible directories.

No additional legal/business documents, Season Two screenplay files,
continuity logs, pitch materials, or master audits were available as separate
unmerged files in the local refs. Existing completed files in those categories
were retained rather than rewritten.

## Duplicate and conflict resolution

- **Removed:** `Series-Bible/MASTER_CANON.m`. It was a one-byte file containing
  only `m` and is an incomplete duplicate/typo beside the complete canonical
  Markdown file `Series-Bible/MASTER_CANON.md`. The complete `.md` file is
  retained unchanged.
- **Retained intentionally:** `Book-1/Book 1  (1).pdf` and
  `Book-1/ED_EPISODE_21.pdf` have identical content, but their filenames imply
  potentially distinct production uses. Neither was deleted or overwritten.
- **Retained intentionally:** repeated `README.md` and `.gitkeep` basenames
  occur in different directories and are not filename conflicts.
- **Conflicts encountered:** none. There were no additional local branch tips
  to merge, so no textual merge conflict occurred.

## Integrity checks

- Checked the Git object database for unreachable commits; no additional
  reachable or dangling work was found.
- Compared the consolidation base against the initial commit; it already
  contains the completed files listed above.
- Reviewed duplicate basenames and exact-content duplicates.
- Searched Markdown links; the only Markdown URL points to Google Sheets and
  is syntactically valid. No repository-relative Markdown links required repair.
- Confirmed required top-level folders exist: `Book-1`, `Book-2`, `Book-3`,
  `Characters`, `Screenplays`, `Series-Bible`, and `Timeline`.

## Canon assurance

This consolidation introduces no story material, dialogue, narrator language,
Chat/Check Check language, nursery rhymes, episode numbering, or canon. Apart
from removal of the incomplete one-byte `.m` duplicate, canonical material is
preserved verbatim in `Series-Bible/MASTER_CANON.md`.
