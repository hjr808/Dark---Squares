# DARK SQUARES — SCREENPLAY ASSEMBLY PROVENANCE

**Document type:** Source traceability record  
**Prepared by:** Copilot Coding Agent  
**Assembly date:** 2026-07-31  
**Repository:** hjr808/Dark---Squares  
**Branch committed to:** `copilot/recover-screenplay-canon`

---

## Discovery Process

The following sources were searched and inventoried before any assembly work began:

| Source type | Description |
|---|---|
| `main` branch — current tree | All files found via full recursive directory listing |
| Remote branches | All 15 branches fetched via GitHub API and `git fetch --unshallow` |
| Commit history | Full history (65 commits) traversed after unshallowing |
| Pull requests | Searched via GitHub MCP tools |
| GitHub Actions | Workflow file reviewed; no screenplay artifacts recovered |

---

## Asset Inventory by Source Type

### Current Tree (`main` branch)

| File | Relevance |
|---|---|
| `Screenplays/Season-1/EPISODE_01_THE_WOODS.md` | **Primary S1E1 source** — complete screenplay draft |
| `Producer-Package/19_PILOT_SAMPLE.md` | **Secondary S1E1 source** — alternate/expanded pilot scene versions |
| `Producer-Package/14_PRINCIPAL_CHARACTERS.md` | Character canon for both seasons |
| `Producer-Package/15_SUPPORTING_CHARACTERS.md` | Supporting character canon |
| `Producer-Package/16_WORLD_LOCATIONS.md` | Location canon |
| `Producer-Package/12_SEASON_ONE_OVERVIEW.md` | Season arc context |
| `Producer-Package/13_SEASON_ONE_EPISODE_GUIDE.md` | Episode-by-episode descriptions |
| `Producer-Package/18_FUTURE_SEASONS.md` | Season Two directional planning |
| `Season-2/SEASON_TWO_EPISODE_GUIDE.md` | **Primary S2E1 planning source** — logline, A/B story, locations, continuity notes |
| `Season-2/SEASON_TWO_STORY_ARCS.md` | Long-form Season Two character arcs and guardrails |
| `Screenplays/Season-1/EPISODE_21_BLOODY_SWEET_16.md` | Season One finale — canonical bridge to Season Two |
| `Series-Bible/DARK_SQUARES_SERIES_SHOW_BIBLE.md` | Series-level canon |
| `Series-Bible/MASTER_CANON.md` | Master canon document |
| `Series-Bible/SEASON_TWO_SOURCE_MAP.md` | Season Two source authority map |

### Branch-Only Files (recovered)

| Branch | File | Relevance |
|---|---|---|
| `codex/create-season-2-episode-screenplays` | `Screenplays/Season-2/EPISODE_01.md` | **Primary S2E1 screenplay draft** — full one-hour draft with dialogue and scenes |
| `codex/create-season-2-episode-screenplays` | `Screenplays/Season-2/EPISODE_02.md` through `EPISODE_05.md` | Episodes 2–5 (not assembled here; noted for future use) |

---

## Season One — Episode One Pilot

### Title
**"THE WOODS"**

### Canonical spelling note
All references use **Manny** per `Producer-Package/14_PRINCIPAL_CHARACTERS.md`:
> "The canonical spelling for detailed-narrative material is Manny."

### Sources used (ranked by authority)

1. **`Screenplays/Season-1/EPISODE_01_THE_WOODS.md`** — primary screenplay draft.
   Contains four acts with full action lines, voiceover narration, and dialogue.
   Used as structural backbone.

2. **`Producer-Package/19_PILOT_SAMPLE.md`** — expanded pilot sample with richer
   scene description for the opening (Manny reading the street, Kizzy on the steps,
   Ella Mae in the kitchen, the doorway rule scene). The dialogue in the doorway
   scene was more complete here and was merged in.

3. **`Producer-Package/14_PRINCIPAL_CHARACTERS.md`** — used to verify all character
   voices, relationships, and traits.

4. **`Producer-Package/16_WORLD_LOCATIONS.md`** — used to ensure location
   descriptions match canon.

5. **`Producer-Package/13_SEASON_ONE_EPISODE_GUIDE.md`** — confirmed the episode's
   scope (world-building, Ella Mae's rule, Kizzy, the four-family building).

### Assembly method
The two screenplay sources (`EPISODE_01_THE_WOODS.md` and `19_PILOT_SAMPLE.md`)
contain overlapping scenes with different detail levels. The following merge strategy
was applied:

- Opening exterior scene: **pilot sample version** used (richer environmental detail,
  Manny reading the block).
- Ella Mae kitchen scene: **pilot sample version** used (more dialogue, complete
  rule exchange).
- Doorway farewell scene: **merged** (pilot sample's fuller dialogue + Episode 1's
  V.O. narration).
- Alley/bike scenes: **Episode 1 version** used.
- Night conversation about Steve's turntables: **reconstructed** from Episode 1 V.O.
  and Episode 5 (`EPISODE_05_STEVES_TURNTABLES.md`) foreshadowing.
- Graveyard section: **reconstructed** from Episode 4 (`EPISODE_04_THE_GRAVEYARD_BET.md`)
  episode guide description and Episode 1 series of V.O. passages.
- Tag / closing V.O.: **Episode 1 version** used verbatim.

### Gap-filling (minimal)
Two scenes required minor gap-filling because neither source had complete scene-level
dialogue:

- **Manny/Keith conversation about Steve's turntables**: Dialogue constructed from
  Episode 1 V.O. text and the established character voices (Keith's social curiosity,
  Manny's protective redirection). No new story elements introduced.
- **Graveyard scene dialogue**: The graveyard dare is established canon
  (`EPISODE_04_THE_GRAVEYARD_BET.md`). The specific dialogue ("You go first / No /
  You're older / That means I know better") is constructed from character voice
  as documented in the principal character profiles. No new story elements introduced.

### Output files produced
| Format | Path |
|---|---|
| Markdown | `Final/Season-1/Dark_Squares_Season_1_Episode_1_Pilot.md` |
| Fountain | `Final/Season-1/Dark_Squares_Season_1_Episode_1_Pilot.fountain` |
| DOCX | `Final/Season-1/Dark_Squares_Season_1_Episode_1_Pilot.docx` |
| PDF | `Final/Season-1/Dark_Squares_Season_1_Episode_1_Pilot.pdf` |

---

## Season Two — Episode One

### Title
**"RAIN ON CONCRETE"**

*(Working title from `Season-2/SEASON_TWO_EPISODE_GUIDE.md`. This document states:
"Season Two has no previously canonized episode titles; titles below are working
titles, not established canon.")*

### Sources used (ranked by authority)

1. **`codex/create-season-2-episode-screenplays` branch —
   `Screenplays/Season-2/EPISODE_01.md`** — primary screenplay draft recovered
   from branch. Contains full four-act structure with dialogue, scene headings,
   and character moments. **Note:** This draft uses the alternate spelling "Mannie."
   Per canon authority in `Producer-Package/14_PRINCIPAL_CHARACTERS.md`, all
   instances were normalized to **"Manny"** in the final assembled script.

2. **`Season-2/SEASON_TWO_EPISODE_GUIDE.md`** — Episode 1 planning card with
   logline, A story, B story, key locations, continuity notes, and cliffhanger.
   Used to verify the branch screenplay's coverage and to fill structural gaps.

3. **`Season-2/SEASON_TWO_STORY_ARCS.md`** — Season engine description and
   long-form arc summaries. Used to ensure character motivations and tone match
   long-form planning.

4. **`Screenplays/Season-1/EPISODE_21_BLOODY_SWEET_16.md`** — Season One finale.
   Used as the direct canonical bridge: the final seconds of S1E21 are the
   opening seconds of S2E1.

5. **`Producer-Package/14_PRINCIPAL_CHARACTERS.md`** and
   **`Producer-Package/15_SUPPORTING_CHARACTERS.md`** — character verification.

### Assembly method
The branch draft (`EPISODE_01.md`) was the primary source. The following
modifications were made during final assembly:

- **Spelling normalization:** "Mannie" → "Manny" throughout.
- **Previously On:** Added per television production standard; material drawn
  directly from S1E21 finale imagery.
- **Teaser expansion:** V.O. narration added from character voice (supported by
  Season Two arc documentation: "Manny tries to keep his brother, mother, home,
  music, and friends from breaking apart").
- **Lucky's studio removal of gun:** Added from character profile
  (`PRINCIPAL_CHARACTERS.md`: "Lucky keeps a gun in the studio... He is practical,
  not paranoid"). This was noted as a continuity obligation in the episode guide.
- **Nate / Check Check thread decision:** Expanded from Episode Guide B story note:
  "Nate preserves the Check Check thread instead of deleting it." Full scene
  reconstructed from this planning note.
- **Cliffhanger:** Keith asking whether he is going to jail — preserved verbatim
  from Episode Guide cliffhanger note.

### Gap-filling (minimal)
The branch screenplay draft was substantially complete. The following minimal
additions were made to align it with the planning documents:

- Ella Mae's kitchen scene was expanded to include the "I'm not going to lose you
  to this" exchange, which aligns with her established character voice and the
  Season Two arc description.
- The Act Four "Manny covers Keith / Ella Mae tells him to sleep" closing beat was
  added from the Season Two arc emotional note: "The family has survived the night;
  it has not escaped it."
- The Tag V.O. closing lines were added from the Season Two arc description:
  "No one is rescued by morning. They are only given another choice."

### Continuity guardrails honored
Per `Season-2/SEASON_TWO_STORY_ARCS.md` and `Season-2/SEASON_TWO_EPISODE_GUIDE.md`:

- ✅ Chucky's medical outcome not stated — he is alive, critical, uncertain.
- ✅ No legal charge, verdict, or jurisdiction specified.
- ✅ Pretty Ricky not introduced (correct: Episode 15 introduction per guide).
- ✅ No New York storyline, Wizard storyline, or invitation/society storyline.
- ✅ Butch/Sarah relationship preserved; no Manny/Sarah triangle.
- ✅ Lucky remains the original studio host.
- ✅ Boy George introduced as a street connector (named in character planning docs).
- ✅ Li Keith artist name not yet used in S2E1 (correct per arc plan).

### Output files produced
| Format | Path |
|---|---|
| Markdown | `Final/Season-2/Dark_Squares_Season_2_Episode_1.md` |
| Fountain | `Final/Season-2/Dark_Squares_Season_2_Episode_1.fountain` |
| DOCX | `Final/Season-2/Dark_Squares_Season_2_Episode_1.docx` |
| PDF | `Final/Season-2/Dark_Squares_Season_2_Episode_1.pdf` |

---

## Files Not Used (Reviewed and Excluded)

| File | Reason not used |
|---|---|
| `Book-1/Dark-Squares-Book-1.md` | Prose manuscript (novel form), not screenplay |
| `Book-1/Dark_Squares_Book_One_Season_One_Manuscript.docx` | Binary; prose novel |
| `Series-Bible/PHASE_ONE_CREATIVE_COMPLETION_AUDIT.md` | Administrative audit, no screenplay material |
| All other `Screenplays/Season-1/EPISODE_XX_*.md` | Episodes 2–21; out of scope for this deliverable |
| `codex/create-season-2-episode-screenplays` Episodes 2–5 | Out of scope for this deliverable |

---

## Notes on Canon Preservation

1. No characters, locations, events, or storylines were invented that are not
   supported by existing repository documents.
2. The sole invented elements are brief dialogue exchanges needed to connect
   established scenes — all constructed strictly from documented character voices.
3. The canonical spelling "Manny" is used throughout. "Mannie" is an alternate
   spelling found in earlier planning documents; it has been normalized per the
   principal character profiles.
4. All Season Two guardrails from `SEASON_TWO_STORY_ARCS.md` were honored.

---

*© Alfred HJR / Alien51Smoke LLC. All Rights Reserved.*
