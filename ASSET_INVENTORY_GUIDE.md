# DARK SQUARES — ASSET INVENTORY SPREADSHEET
**Location:** Google Sheets (recommended for collaborative management)  
**Document Type:** Digital Asset & Media Inventory  
**Date Created:** July 17, 2026  
**Status:** Live Tracking

---

## GOOGLE SHEETS SETUP INSTRUCTIONS

### Create New Google Sheet

1. **Go to:** [Google Sheets](https://sheets.google.com)
2. **Create New Spreadsheet** and name it: `Dark-Squares-Asset-Inventory-v1`
3. **Share Settings:**
   - Share with: Production team members
   - Permissions: Editor (for team members), Viewer (for stakeholders)
   - Link: Make document accessible to hjr808 team

---

## SPREADSHEET STRUCTURE

### Sheet 1: MASTER INVENTORY

**Column Headers:**
```
A: Asset ID
B: Asset Type
C: Asset Name
D: Description
E: Source/Location
F: Format
G: Resolution/Specs
H: File Size
I: Date Created
J: Version
K: Status
L: Owner/Creator
M: Usage Rights
N: Approved
O: Approval Date
P: Notes
Q: Archive Location
```

**Data Type Details:**

| Column | Type | Example | Purpose |
|--------|------|---------|---------|
| A | Text | AST-001-P | Unique identifier for tracking |
| B | Dropdown | Poster / Character Photo / Logo / Artwork | Category classification |
| C | Text | Primary Full Moon Poster | Descriptive asset name |
| D | Text | Main theatrical poster with silhouettes | Brief description |
| E | Link | Producer_Edition_FINAL.pdf (Page 1-3) | File location or source |
| F | Dropdown | PDF / JPG / PNG / AI / PSD | File format |
| G | Text | 27" x 40" @ 300 DPI | Technical specifications |
| H | Number | 45.2 MB | File size in MB |
| I | Date | 06/27/2026 | Date created/generated |
| J | Text | v1 (Final) | Version number and status |
| K | Dropdown | Completed / In Progress / Pending / Archived | Current status |
| L | Text | ReportLab / Production Team | Who created/maintains |
| M | Dropdown | Approved / Internal Only / Restricted | Usage permissions |
| N | Checkbox | ✓ | Approved for distribution |
| O | Date | 07/17/2026 | Date of approval |
| P | Text | Ready for printing / Needs color correction | Additional notes |
| Q | Link | Archive/Posters/Primary_v1_FINAL | Storage location |

---

### Sheet 2: POSTERS

**Focus:** All poster assets from Producer Edition

**Column Headers:**
```
A: Poster ID
B: Poster Title
C: Type (Primary/Ensemble/Character/Urban)
D: Primary Subject
E: Characters Featured
F: Colors Used
G: Dimensions
H: Resolution
I: Print-Ready
J: Digital-Ready
K: Social Media Adapted
L: File Path - Print Version
M: File Path - Digital Version
N: File Path - Social Version
O: Approval Status
P: Date Approved
Q: Last Updated
R: Notes
```

**Sample Entries:**
```
POSTER-001 | Primary Full Moon | Primary | Silhouettes/Gate/Moon | All cast silhouettes | Black/Silver/Blue | 27"x40" | 300 DPI | Yes | Yes | In Progress | ... | ... | ... | Approved | 07/16/2026 | 07/17/2026 | Ready for theatrical distribution

POSTER-002 | Ensemble Cast Grid | Ensemble | Character grid arrangement | Mannie, Keith, Butch, Sarah, Boy George | Black/Gray | 27"x40" | 300 DPI | Yes | Yes | Completed | ... | ... | ... | Approved | 07/16/2026 | 07/17/2026 | Use for investor deck

POSTER-003 | Character Portrait - Mannie | Character | Urban street setting | Mannie (lead) | Black/Metallic accents | 24"x36" | 300 DPI | Yes | Yes | Completed | ... | ... | ... | Approved | 07/16/2026 | 07/17/2026 | Individual character series
```

---

### Sheet 3: CHARACTER ASSETS

**Focus:** All character-related visual materials

**Column Headers:**
```
A: Character ID
B: Character Name
C: Asset Type
D: Asset Description
E: Visual Elements
F: File Format
G: Resolution
H: Color Graded
I: Ready for Use
J: Multiple Variations
K: Costume/Styling Notes
L: Location/Setting
M: File Path
N: Backup Path
O: Created Date
P: Last Updated
Q: Owner
R: Status
S: Notes
```

**Sample Entries:**
```
CHAR-001 | Mannie | Portrait | Individual character headshot | Lead character, street wear, dramatic lighting | JPG | 1920x2880 px | Yes | Yes | 3 variations | Black hoodie, gold chain | Urban street at night | Dark-Squares-Assets/Characters/Mannie_Portrait_v1_FINAL.jpg | Archive/Characters/Mannie_Portrait_v1_FINAL.jpg | 06/27/2026 | 07/17/2026 | Photography Team | Approved | Primary character reference

CHAR-002 | Keith | Ensemble | Group photo with motorcycle | Keith with motorcycle, supporting position | JPG | 2400x3200 px | Yes | Yes | 2 variations | Urban casual, jacket | Street corner | Dark-Squares-Assets/Characters/Keith_Motorcycle_Group_v1.jpg | Archive/... | 06/27/2026 | 07/17/2026 | Photography Team | Approved | Part of street culture visual

CHAR-003 | Sarah | Character Reference Sheet | Full-body reference | Multiple poses, costume details | PSD + PDF Export | 1200x1600 px | Yes | Pending | 5 variations | Professional styling | Studio reference | Dark-Squares-Assets/Characters/Sarah_ReferenceSheet_v1.psd | Archive/... | 06/20/2026 | 07/16/2026 | Design Team | In Progress | For production costume department
```

---

### Sheet 4: PROMOTIONAL MATERIALS

**Focus:** Marketing and promotional assets

**Column Headers:**
```
A: Promo ID
B: Material Type
C: Item Name
D: Dimensions/Specs
E: Format
F: Quantity Produced
G: Distribution Channel
H: Target Audience
I: Launch Date
J: File Path - Master
K: File Path - Export 1
L: File Path - Export 2
M: Print Vendor
N: Production Status
O: Cost
P: Approval Status
Q: Notes
```

**Sample Entries:**
```
PROMO-001 | Social Media Kit | Character Portrait Pack | 1080x1350px, 1200x1200px, 1080x1920px | JPG + PNG | 5 variations per character | Instagram, Facebook, Twitter | General Audience | 08/01/2026 | Dark-Squares-Assets/Social/CharacterPack_v1_FINAL | Instagram_1080x1350 | TikTok_1080x1920 | N/A | Ready | $0 | Approved | High-res versions ready; format variations complete

PROMO-002 | Email Campaign | Newsletter Header | 600x200px, 800x267px | JPG | 2 layouts | Email newsletters | Subscriber list | 07/20/2026 | Dark-Squares-Assets/Email/NewsletterHeader_v1 | Version_600x200 | Version_800x267 | N/A | Ready | $0 | Approved | A/B test layouts prepared

PROMO-003 | Merchandise | T-Shirt Design | Front: 8"x10", Back: 4"x6" | AI + PDF | 50 units (initial run) | Store / Comic Con | Fans/Collectors | 08/15/2026 | Dark-Squares-Assets/Merch/TShirt_Design_v1_FINAL | Print_Ready_Front | Print_Ready_Back | Custom Apparel Co. | In Production | $8.50/unit | Approved by Network | Rush order for SDCC
```

---

### Sheet 5: PRODUCTION ARTWORK

**Focus:** Behind-the-scenes, concept art, and production reference

**Column Headers:**
```
A: Artwork ID
B: Category
C: Title
D: Subject Matter
E: Artist/Designer
F: Medium/Format
G: File Type(s)
H: Resolution
I: Purpose
J: Used In
K: Location
L: Backup Location
M: Date Created
N: Last Modified
O: Production Department
P: Reference Notes
Q: Status
```

**Sample Entries:**
```
ART-001 | Scene Concept | Urban Street - Daytime | Residential street scene with storefronts | Production Design | Digital Painting | PSD + JPG | 3840x2160 px | Location reference for production design | TV episodes 1-3 | Dark-Squares-Assets/ProductionArt/UrbanStreet_Concept_v2 | Archive/ProductionArt/... | 05/15/2026 | 07/10/2026 | Production Design | Provides color palette and architectural reference | Approved

ART-002 | Lighting Study | Night Street Lighting | Streetlight and neon accent study | Cinematography | Lighting render | AI + JPG | 1920x1080 px | Establish lighting approach for night scenes | All night sequences | Dark-Squares-Assets/ProductionArt/LightingStudy_Night_v1 | Archive/... | 04/20/2026 | 06/15/2026 | Cinematography | Reference for gaffer; specific Kelvin temperatures noted | Approved

ART-003 | Character Design | Costume Mood Board | Character silhouette studies and costume options | Costume Design | Mood board (images + swatches) | PDF + AI | 1800x2400 px | Establish costume aesthetic for all characters | TV pilot and series | Dark-Squares-Assets/ProductionArt/CostumeMoodBoard_v3 | Archive/... | 03/01/2026 | 07/05/2026 | Costume Department | Approved silhouettes; waiting final textile selections | Approved with Notes
```

---

### Sheet 6: LOGO & BRANDING

**Focus:** Logo files and brand identity assets

**Column Headers:**
```
A: Brand Asset ID
B: Asset Name
C: Type (Wordmark/Icon/Full Logo/Variation)
D: Color Version
E: Format
F: File Format(s)
G: Minimum Size
H: Clear Space Req.
I: Design File
J: Print Export
K: Digital Export
L: Web Export
M: Designer
N: Version
O: Date Finalized
P: Usage Guidelines Link
Q: Approval Status
R: Notes
```

**Sample Entries:**
```
BRAND-001 | DARK SQUARES Main Wordmark | Full Logo | Metallic Silver on Black | Primary | AI, PDF, PNG, EPS | 2" minimum | 0.25" | Brand_Assets/Logo/DarkSquares_Wordmark_v1_FINAL.ai | Brand_Assets/Logo/Export_Print/DarkSquares_Wordmark_Print_v1.pdf | Brand_Assets/Logo/Export_Digital/DarkSquares_Wordmark_Web_v1.png | Brand_Assets/Logo/Export_Web/DarkSquares_Wordmark_Web_Optimized_v1.png | Design Studio | v1 Final | 07/16/2026 | BRAND_GUIDELINES.md | Approved | Primary use all applications

BRAND-002 | DARK SQUARES Icon Mark | Icon Version | Metallic Silver on Black | Secondary | AI, PNG, SVG | 0.5" minimum | 0.125" | Brand_Assets/Logo/DarkSquares_Icon_v1_FINAL.ai | N/A | Brand_Assets/Logo/Export_Digital/DarkSquares_Icon_v1.png | Brand_Assets/Logo/Export_Web/DarkSquares_Icon_Web_v1.svg | Design Studio | v1 Final | 07/16/2026 | BRAND_GUIDELINES.md | Approved | Social media profiles, favicons

BRAND-003 | Color Palette Reference | Swatch Set | Full palette (Black, Silver, Blue, Gray) | Reference | Adobe ASE, PDF, PNG | N/A | N/A | Brand_Assets/Colors/DarkSquares_Palette_v1.ase | Brand_Assets/Colors/Palette_Print_Reference_v1.pdf | Brand_Assets/Colors/Palette_Digital_v1.png | Brand_Assets/Colors/Palette_Web_v1.png | Design Studio | v1 Final | 07/17/2026 | BRAND_GUIDELINES.md | Approved | Distributed to all creative departments
```

---

### Sheet 7: DIGITAL ASSETS

**Focus:** Web, social media, and digital files

**Column Headers:**
```
A: Digital Asset ID
B: Platform
C: Asset Name
D: Dimensions (WxH)
E: Format
F: File Size
G: Upload Date
H: Performance Metrics
I: File Path
J: Backup Path
K: URL/Link
L: Scheduled Posts
M: Engagement Tracking
N: Status
O: Notes
```

**Sample Entries:**
```
DIG-001 | Instagram | Character Portrait - Mannie | 1080x1350px | JPG | 2.3 MB | 07/17/2026 | 1.2K likes, 84 comments (avg) | Dark-Squares-Social/Instagram/Mannie_Portrait_071726.jpg | Archive/Social/Instagram/... | https://instagram.com/darksequares/... | Posted 07/17/2026 | High engagement expected | Live | Primary feed post

DIG-002 | Facebook | Ensemble Poster | 1200x628px | JPG | 1.8 MB | 07/15/2026 | 523 shares (3 days) | Dark-Squares-Social/Facebook/Ensemble_Poster_Optimized_071526.jpg | Archive/Social/Facebook/... | https://facebook.com/darksequares/... | Scheduled 08/01/2026 | Tracking shares and comments | Scheduled | Boost ad pending network approval

DIG-003 | Twitter | Teaser Quote | 1024x512px | PNG | 0.9 MB | 07/10/2026 | 2.4K retweets, 8.7K likes | Dark-Squares-Social/Twitter/Teaser_Quote_071026.png | Archive/Social/Twitter/... | https://twitter.com/darksequares/... | Posted 07/10/2026 | Strong organic reach | Live | Quote: "Every generation receives an omen"

DIG-004 | Website | Homepage Banner | 1920x500px | JPG | 3.2 MB | 07/01/2026 | 15.8K impressions (2 weeks) | Dark-Squares-Web/Homepage_Banner_v1_FINAL.jpg | Archive/Web/... | https://darksequares.com/index | Rotating banner (2-week cycle) | Page analytics | Live | Primary website visual

DIG-005 | Email | Newsletter Template | 600x800px | HTML + JPG | 1.5 MB | 06/20/2026 | 34% open rate, 12% CTR | Dark-Squares-Email/Newsletter_Template_v2.html | Archive/Email/... | Internal use only | Bi-weekly distribution | Subscriber engagement tracking | Active | A/B tested; winner selected
```

---

### Sheet 8: VIDEO/MOTION ASSETS

**Focus:** Video files, motion graphics, sequences

**Column Headers:**
```
A: Video ID
B: Content Type
C: Title
D: Duration
E: Resolution
F: Frame Rate
G: Codec
H: File Size
I: Location
J: Backup Location
K: Production Date
L: Post-Production Date
M: Creator
N: Status
O: Usage Rights
P: Scheduled Use
Q: Notes
```

**Sample Entries:**
```
VID-001 | Opening Sequence | Title Card Animation | 8 seconds | 1920x1080 px | 24 fps | H.264 | 145 MB | Dark-Squares-Video/Title_Sequence_v1_FINAL.mp4 | Archive/Video/Title_Sequences/... | 06/01/2026 | 06/25/2026 | Motion Graphics Team | Approved | TV/Streaming Approved | Episodes 1-10, Season 1 | Color graded; ready for broadcast

VID-002 | Social Media Teaser | 30-Sec Character Spot | 30 seconds | 1080x1920 px (9:16) | 30 fps | H.264 | 28 MB | Dark-Squares-Video/Social/Character_Teaser_Mannie_30s_v1.mp4 | Archive/Video/Social/... | 07/01/2026 | 07/12/2026 | Social Media Team | Ready to Post | Platform License | Schedule 08/01-08/05/2026 | Optimized for Instagram Reels/TikTok

VID-003 | Behind-the-Scenes | Production Reel | 2 minutes | 1920x1080 px | 24 fps | H.264 | 250 MB | Dark-Squares-Video/BTS/Production_Reel_Cut_01_v2.mp4 | Archive/Video/BTS/... | 06/15/2026 | 07/10/2026 | Production Team | Final Review | Internal/Convention Use | San Diego Comic-Con 2026 panel | High-energy cut; ready for screening
```

---

### Sheet 9: ARCHIVE & VERSIONING

**Focus:** Previous versions and archived materials

**Column Headers:**
```
A: Archive ID
B: Original Asset ID
C: Asset Name
D: Version
E: Reason for Archive
F: Original Location
G: Archive Location
H: Date Archived
I: Replaced By
J: Retention Policy
K: Purge Date (if applicable)
L: Owner
M: Notes
```

**Sample Entries:**
```
ARCH-001 | POSTER-001 | Primary Full Moon Poster | v0 (Beta) | Replaced by v1 Final | Dark-Squares-Assets/Posters/Primary_FullMoon_v0_BETA.pdf | Archive/Posters/Rejected_Versions/Primary_FullMoon_v0_BETA.pdf | 07/16/2026 | POSTER-001 v1 Final | Keep 24 months | 07/16/2028 | Design Team | Early concept; color not finalized

ARCH-002 | CHAR-001 | Mannie Portrait | v0 (Rough) | Lighting issues, replaced by v1 | Dark-Squares-Assets/Characters/Mannie_Portrait_v0.jpg | Archive/Characters/Rejected/Mannie_Portrait_v0_rough.jpg | 07/10/2026 | CHAR-001 v1 Final | Keep 12 months | 07/10/2027 | Photography Team | Test shoot; kept for reference only

ARCH-003 | BRAND-001 | Logo Wordmark | v0.5 (Proof) | Client feedback incorporated, v1 approved | Dark-Squares-Assets/Logo/DarkSquares_Wordmark_v0.5_ProofA.ai | Archive/Logo/Proofs/DarkSquares_Wordmark_v0.5_ProofA.ai | 07/15/2026 | BRAND-001 v1 Final | Keep 36 months | 07/15/2029 | Design Studio | Client chose v1 over this version
```

---

### Sheet 10: USAGE TRACKING

**Focus:** Where assets are being used

**Column Headers:**
```
A: Usage ID
B: Asset Used
C: Campaign/Project
D: Start Date
E: End Date
F: Usage Type
G: Platform(s)
H: Impressions
I: Engagement
J: Performance Notes
K: Approval Status
L: Cost/Budget Used
M: Responsible Party
N: Status
```

**Sample Entries:**
```
USE-001 | POSTER-001 (Primary Full Moon) | Network Announcement Campaign | 08/01/2026 | 08/31/2026 | Press Release + Digital Marketing | Social Media, Email, Web | 142,000 | 8.2% engagement rate | Strong organic reach on Instagram | Approved | $5,000 (ad spend) | Marketing Director | Active

USE-002 | Character Portraits (All 5) | Comic-Con Promotional Event | 07/20/2026 | 07/24/2026 | In-booth signage, merchandise | SDCC Convention, Online | 8,500 (in-person), 45,000 (online) | 12.4% booth traffic conversion | Positive fan feedback; merchandise sold out | Approved | $3,200 (production) | Events Team | Completed

USE-003 | Ensemble Poster | Investor Pitch Deck | 07/17/2026 | Ongoing | Presentation asset | Private meetings | 15 investors | Strong reaction; 2 follow-up meetings | Used as cover slide | Approved | $0 | Producer | Active
```

---

## CONDITIONAL FORMATTING SUGGESTIONS

### Apply to Status Columns
- **Approved** → Green background (#00B050)
- **In Progress** → Yellow background (#FFC000)
- **Pending** → Blue background (#4472C4)
- **Archived** → Gray background (#808080)
- **Rejected** → Red background (#FF0000)

### Apply to Approval Status
- **Approved** → Green checkmark
- **Pending** → Orange exclamation mark
- **Rejected** → Red X

### Data Validation Dropdowns
- **Asset Type:** Poster, Character Photo, Logo, Artwork, Merchandise, Social Media, Video, etc.
- **Format:** PDF, JPG, PNG, PSD, AI, SVG, MP4, etc.
- **Status:** Completed, In Progress, Pending, Archived
- **Approval Status:** Approved, Pending, Rejected
- **Usage Rights:** Approved, Internal Only, Restricted

---

## FORMULAS & AUTOMATED TRACKING

### Suggested Formulas

**Count Total Assets by Type:**
```
=COUNTIF(Sheet1!B:B,"Poster")
```

**Calculate Days Since Approval:**
```
=TODAY()-O2
```

**Flag Overdue Approvals (>7 days pending):**
```
=IF(AND(K2="Pending",TODAY()-I2>7),"URGENT","OK")
```

**Sum Total File Size:**
```
=SUM(H:H)
```

**Track Asset Usage Frequency:**
```
=COUNTIF('Usage Tracking'!B:B,A2)
```

---

## SHARING & COLLABORATION SETTINGS

### Recommended Access Levels

| Role | Access Level | Sheets Access |
|------|--------------|----------------|
| Producer | Editor | All sheets |
| Design Team | Editor | All sheets (except Archive) |
| Marketing Team | Editor | Master, Promotional, Digital, Usage Tracking |
| Finance/Accounting | Viewer | Promotional (cost tracking only) |
| Network Stakeholders | Viewer | Master Inventory, Promotional Materials |
| Archivists | Editor | Archive & Versioning sheet only |

### Sharing Link Format
```
https://docs.google.com/spreadsheets/d/[SHEET_ID]/edit?usp=sharing
```

---

## MAINTENANCE SCHEDULE

### Weekly
- Update status of in-progress assets
- Log new assets added
- Track usage and engagement metrics

### Monthly
- Full audit of inventory
- Archive completed projects
- Generate performance report

### Quarterly
- Review and update asset valuations
- Purge outdated versions (per retention policy)
- Update category tags and organization

---

## SETUP CHECKLIST

- [ ] Create Google Sheet
- [ ] Name: "Dark-Squares-Asset-Inventory-v1"
- [ ] Add all 10 sheets (tabs)
- [ ] Add column headers to each sheet
- [ ] Set up conditional formatting rules
- [ ] Create data validation dropdowns
- [ ] Add formulas for automated tracking
- [ ] Set sharing permissions
- [ ] Invite team members
- [ ] Document sheet update responsibilities
- [ ] Create backup (monthly export to CSV)
- [ ] Share link in PRODUCER_MASTER_PACKAGE.md

---

## GOOGLE SHEETS LINK (TO BE POPULATED)

**Asset Inventory Spreadsheet:**
```
[INSERT GOOGLE SHEETS LINK HERE AFTER CREATION]
```

**Access Code:** [To be shared with team]

---

**END OF ASSET INVENTORY DOCUMENTATION**

*This spreadsheet is the central hub for all Dark Squares assets, tracking, and management. Update regularly for accuracy.*
