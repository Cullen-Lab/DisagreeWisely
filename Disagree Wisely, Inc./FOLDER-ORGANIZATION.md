# Disagree Wisely, Inc. — Folder Organization

Last updated: 2026-03-06

This document describes the reorganized folder structure for the Disagree Wisely, Inc. document collection.

---

## Directory Tree

```
Disagree Wisely, Inc./
├── Website/                           # Board websites (self-contained, GitHub Pages-ready)
│   ├── index.html                     # Landing page linking to both sites
│   ├── board-planning.html            # Meeting agenda + site review notes
│   ├── .gitignore
│   ├── shared/                        # Consolidated CSS/JS (used by both sites)
│   │   ├── css/style.css
│   │   └── js/main.js
│   ├── board-onboarding/
│   │   └── index.html
│   ├── board-reference/
│   │   ├── index.html
│   │   └── docs/                      # 18 bundled PDFs (normalized kebab-case names)
│   │       ├── anti-harassment-policy.pdf
│   │       ├── articles-of-incorporation.pdf
│   │       ├── board-minutes-2025-06-07.pdf
│   │       ├── board-minutes-2025-07-01.pdf
│   │       ├── board-resolutions-jul-2025.pdf
│   │       ├── bylaws-signed.pdf
│   │       ├── coi-acknowledgment-simon-cullen-signed.pdf
│   │       ├── coi-acknowledgment-simon-cullen.pdf
│   │       ├── coi-policy-signed.pdf
│   │       ├── document-retention-policy.pdf
│   │       ├── ein-letter.pdf
│   │       ├── election-stern-oakley.pdf
│   │       ├── financial-authorization-amendment-dec-2025.pdf
│   │       ├── financial-authorization-current.pdf
│   │       ├── insurance-cyber-tech-policy.pdf
│   │       ├── insurance-do-policy.pdf
│   │       ├── intern-nda.pdf
│   │       └── rachel-sipser-offer-amendment-feb-2026.pdf
│   └── internal/                      # Internal planning files (not linked from sites)
│       ├── Board Meeting - March 6 2026.pdf          # Meeting slides PDF
│       ├── Board Meeting - March 6 2026 - Transcript.pdf  # Meeting transcript (when available)
│       ├── generate_slides.py
│       └── meeting-slides.html
├── board-onboarding/          # DEPRECATED — superseded by Website/board-onboarding/
├── Governance/
│   ├── Bylaws/
│   │   ├── Revised BYLAWS - Non Member Standard signed.pdf
│   │   ├── Revised BYLAWS - Non Member Standard.pdf
│   │   └── Revised BYLAWS - Non Member Standard.docx
│   ├── Policies/
│   │   ├── Conflict of Interest/
│   │   │   ├── ConflictofInterest-General signed.pdf
│   │   │   ├── ConflictofInterest-General.pdf
│   │   │   ├── ConflictofInterest-General.docx
│   │   │   ├── signed_Conflict-of-Interest-Acknowledgment-Simon-Cullen.pdf
│   │   │   └── Conflict-of-Interest-Acknowledgment-Simon-Cullen.pdf
│   │   ├── Document Retention/
│   │   │   └── DW Document retention policy.pdf
│   │   ├── Anti-Harassment and Discrimination/
│   │   │   ├── Anti-Harassment and Anti-Discrimination Policy - Disagree Wisely, Inc..pdf
│   │   │   ├── Anti-Harassment-and-Anti-Discrimination-Policy.html
│   │   │   ├── Anti-Harassment-and-Anti-Discrimination-Policy.md
│   │   │   ├── Board-Email-Anti-Harassment-Policy.md
│   │   │   ├── Platform-Community-Guidelines.html
│   │   │   └── Platform-Community-Guidelines.md
│   │   └── Intern NDA/
│   │       └── Disagree Wisely - Intern NDA.pdf
│   ├── Board Resolutions/
│   │   ├── Amendment to Financial Authorization Board Resolution.pdf
│   │   ├── Election of Kenneth Stern and Barbara Oakley as Directors.md
│   │   ├── Email - Personnel Hiring Amendment.txt
│   │   ├── Financial Authorization (9.28.2025).md
│   │   ├── Financial Authorization (Amended 12.13.2025).md
│   │   ├── Personnel Hiring Amendment (Draft).md
│   │   ├── Rachel Sipser - Offer Letter (Nov 2025).md
│   │   ├── Rachel Sipser - Offer Letter Amendment (Feb 2026).md
│   │   ├── Rachel Sipser - Offer Letter Amendment (Feb 2026).pdf
│   │   ├── Rachel Sipser job offer.pdf
│   │   ├── Rachel Sipser job offer_Rachel Signed 12262025.pdf
│   │   ├── DW Board Resolutions Jul 2025.gdoc
│   │   └── DW Board Resolutions Jul 2025.pdf
│   ├── Board Meeting Follow-Up Emails/
│   │   └── 2026-03-06 Board Meeting Follow-Up.rtf     # Draft email + attachments (COI, Bylaws, Minutes PDFs)
│   └── Board Meeting Minutes/
│       ├── 2025-06-07/
│       │   └── 2025-06-07 Board Meeting Minutes.docx
│       ├── 2025-09-22/
│       │   ├── Financial Authorization Board Resolution - Minimal Audit Updates.md
│       │   ├── expense_checker.py
│       │   └── expense_corrections.py
│       └── Next Board Meeting/
│           ├── README-Board-Process.md
│           ├── auto_convert.sh
│           ├── Jobs and Salaries/
│           ├── Markdown files/
│           └── PDFs/
│
├── Incorporation and Tax/
│   ├── Florida Incorporation/
│   │   ├── 04-23-25 - FL - Initial Filing - Disagree Wisely Inc.pdf
│   │   ├── 4-17-25 - FL - Formation Document - Disagree Wisely Inc.pdf
│   │   ├── Instructions and Articles.pdf
│   │   ├── disagree wisely articles of incorporation.pdf
│   │   ├── signed_Revised Instructions and Articles copy.pdf
│   │   └── 07-28-25 - FL - State Notice - Disagree Wisely Inc.pdf
│   ├── Federal Tax/
│   │   ├── 05-20-25 -  - EIN Letter - Disagree Wisely Inc.pdf
│   │   ├── EFTPS enrollment.pdf
│   │   ├── EFTPS. 07-15-25 - FL - State Notice - Disagree Wisely Inc.pdf
│   │   └── EIN - Disagree Wisely Inc.pdf
│   └── Pennsylvania Tax/
│       ├── (15 files including tax forms, registration, etc.)
│       └── Jordan Tax stuff/
│
├── Financials/
│   ├── Bank Statements/
│   │   ├── 20251008-statements-5324-.pdf
│   │   ├── statement_2025_5.pdf through statement_2025_10.pdf
│   │   └── bluevine_statement_2025_6.pdf
│   ├── Banking Setup/
│   │   ├── Bluevine.png
│   │   ├── axos disclosure and consent form.pdf
│   │   └── axos submission info.pdf
│   └── EXPENSES draft LKH.xlsx
│
├── 501c3 Application (Foundation Group)/
│   ├── Narratives/
│   │   ├── disagree wisely narrative.docx
│   │   ├── disagree wisely narrative (revised).docx
│   │   └── narrative-changes.html
│   ├── Job Descriptions/
│   │   ├── CEO job description (revised).docx
│   │   ├── CEO job description (revised).pdf
│   │   ├── CTOO job description (revised).docx
│   │   ├── CTOO job description (revised).pdf
│   │   └── job-description-changes.html
│   ├── Research/
│   │   ├── ICDC grant ND.md
│   │   ├── Questions for Ren.md
│   │   ├── Research Organizer changelog.html
│   │   ├── Research Organizer submission draft.md
│   │   ├── Scientific Research Organizer - Revised Draft.md
│   │   └── TWCF_Complete_Submission.pdf
│   ├── Budgets/
│   │   ├── New Budget Template LKH.xlsx
│   │   ├── New Budget Template LKH 2.xlsx
│   │   └── EXPENSES new LKH (Ren comments).xlsx
│   ├── IP Documents/
│   │   ├── Potential of a 501c3 developing key insiders IP.docx
│   │   └── SAMPLE Long term IP Agreement.docx
│   ├── Personal Sites Review/
│   │   ├── Nick/
│   │   └── Simon/
│   ├── Correspondence/
│   │   ├── Message to Ren - request call.txt
│   │   └── Chats (from website)/
│   ├── Form 1023 Drafts/
│   │   ├── Form 1023 Part IV.md
│   │   ├── Form 1023 Part IV v2.md
│   │   └── Form 1023 Part IV v3.md
│   ├── Situation Summary - DW Restructuring Issues.md
│   └── Tools Competition Funds - Compliance Notes.md
│
├── Insurance/
│   ├── Active Policies/
│   │   ├── IT2-Policy_DDP-2315240-P1.pdf          # D&O policy (Carolina Casualty, $1M, $820.13/yr)
│   │   ├── SST-ESO0040579703.pdf                   # Cyber/E&O policy (CFC/Lloyd's, $1M, $3,780/yr)
│   │   └── Gallagher Go Client User Guide for Small Business (3).pdf
│   ├── Emails/
│   │   ├── Gmail - Disagree Wisely, Inc..pdf                                    # Full email thread (Jul–Nov 2025)
│   │   ├── Gmail - Disagree Wisely, Inc_EXDO, PFEO_Insurance Proposal.pdf       # Proposal & Q&A thread
│   │   ├── Gmail - Urgent - RE: Disagree Wisely, Inc_EXDO, PFEO_Insurance Proposal.pdf  # D&O premium increase
│   │   └── Gmail - COVERAGE BOUND Effective 11:14:2025 — Disagree Wisely.pdf    # Final binding confirmation
│   ├── D&O/
│   │   ├── Endrosements.pdf
│   │   ├── Quote.pdf
│   │   ├── Required App.pdf
│   │   └── Specimen.pdf
│   ├── Cyber and Professional Liability/
│   │   ├── No Claims Declaration.pdf
│   │   ├── Quote.pdf
│   │   └── Specimen.pdf
│   └── Application/
│       ├── Balance Sheet.xlsx
│       ├── Dapp_NonProfit_Directors_Officers.pdf
│       ├── Income Statement.xlsx
│       └── Tech Cyber EO App.pdf
│
├── Legal/
│   └── Dentons/
│       ├── Cullen and DiBella 40864 809062.pdf
│       └── Simon Cullen and Nicholas DiBella 40864.0001 810180.pdf
│
├── Personnel/
│   └── Nick DiBella/
│       ├── DW employment letter for nick (not signed).pdf
│       ├── DW employment letter.pdf
│       ├── DiBella_Employment_Letter.html
│       ├── DiBella_Employment_Letter.md
│       ├── ICPD employment letter.pdf
│       ├── pets.docx
│       └── pets.pdf
│
├── Branding/
│   ├── Logo/
│   │   ├── (PNG, SVG logo files)
│   │   └── icons/
│   └── Letterhead/
│       └── Disagree_Wisely_Inc_Letterhead.docx
│
├── Grants/
│   ├── HxA-AVDF/
│   │   ├── Sway - HxA and Disagree Wisely Services Agreement V2 2025.pdf  # Phase 1 (May–Dec 2025)
│   │   ├── Sway - HxA and Disagree Wisely Services Agreement V2 2026.pdf  # Phase 2 (Jan–Nov 2026)
│   │   └── Sway Classroom Grant Agreement.docx - signed.pdf               # $13,171 restricted grant (Nov 2025–Jul 2026)
│   ├── Snider Foundations/
│   │   ├── Craig-Snider-Foundation-Disagree Wisely Grant Agreement.pdf     # $50K, signed Jun 6, 2025
│   │   └── Lindy-Snider-Foundation-Disagree Better Grant Agreement 6.18.pdf  # $25K, signed Jun 18, 2025
│   ├── ECI/
│   │   ├── ECI Narrative.pdf                                              # Full narrative for Wake Forest ECI grant
│   │   ├── Statement of Work_Sway ECI grant.pdf                          # DW statement of work
│   │   ├── DW Budget ECI.xlsx                                            # DW budget (~$233K over 3 years)
│   │   └── Signed_ECI_letter_.pdf                                        # Signed letter of support
│   ├── FIPSE/
│   │   └── ICDC grant ND.md                                               # Grant narrative ($4M consortium, ~$800K to DW)
│   ├── NewSchools/
│   │   └── NewSchools Application.docx                                    # Sway Classroom grant application
│   ├── TWCF/
│   │   └── TWCF_Complete_Submission.pdf                                   # Request for Ideas (Feb 2026, $5M+ if invited to full app)
│   ├── Sway-Disagree-Wiselly-Grants.gdoc
│   └── Copy of (DH) TLA Tools Competition Invoice - Installment 2 | 2025 Tools (Revised).gsheet
│
├── Misc/
│   ├── Bluevine bank verification letter 20250730.pdf
│   ├── Gusto ConversationTranscript.pdf
│   ├── Email-Template-Pre-Meeting.pdf
│   ├── Sway workspace-2.md
│   ├── Sway workspace-3.md
│   └── Sway workspace-4.md
│
├── Archive/
│   ├── Business Expenses (migrated to SwayAccounting)/
│   │   └── (entire folder preserved as-is from SwayAccounting migration)
│   ├── Old Bluevine Data/
│   │   ├── sorted_expenses.csv
│   │   └── transactions-20092025.csv
│   ├── Old Board Materials/
│   │   ├── Financial Authorization Board Resolution (OLD).md
│   │   ├── expense_checker.py
│   │   └── CTOO-salary-justification-detailed-board-documentation.md
│   ├── Old Foundation Group/
│   │   ├── (6 old budget/expense/email files from Foundation Group materials)
│   │   ├── (9 old CEO/CTOO job description drafts)
│   │   └── (5 old Research Organizer drafts)
│   ├── Old Financial Documents/
│   │   └── (4 old financial files: invoice, budget CSV, screenshot, Upwork report)
│   ├── Old Insurance/
│   │   └── (25 old insurance proposal/quote/email files)
│   └── Old Misc/
│       ├── ConflictofInterest-General copy.docx
│       ├── CTOO job description.docx
│       ├── TOS.md
│       ├── Old EIN screenshot.pdf
│       ├── signed_Revised Instructions and Articles.pdf
│       ├── Budget for Snider.xlsx
│       └── 05_22_2025-bulk-summary-invoice/
│
└── FOLDER-ORGANIZATION.md
```

---

## Section Descriptions

### Governance/
Core organizational governance documents: bylaws, board-adopted policies, board resolutions, meeting minutes, and board follow-up emails (with attachments). This is the primary reference for board members.

### Incorporation and Tax/
State incorporation filings (Florida), federal EIN and tax documents, and Pennsylvania state tax registrations and filings.

### Financials/
Bank statements, banking setup documents, and expense tracking spreadsheets.

### 501c3 Application (Foundation Group)/
All materials related to the 501(c)(3) application, prepared with Foundation Group (the nonprofit consulting firm): narratives, job descriptions, research organizer drafts, budgets, IP agreements, Form 1023 drafts, and correspondence.

### Insurance/
Active insurance policies (D&O via Carolina Casualty, Cyber/E&O via CFC/Lloyd's), email correspondence with Gallagher (the broker), initial quotes and application materials, and the Gallagher client guide. Both policies effective 11/14/2025, claims-made with full prior acts coverage. See `Archive/Old Insurance/insurance-issues-explained.md` for a record of issues raised and resolved during the binding process.

### Legal/
Attorney invoices and correspondence (currently Dentons only).

### Personnel/
Employee-related documents organized by person.

### Branding/
Logo files (SVGs, PNGs) and letterhead template.

### Grants/
Grant-related documents and invoices.
- **`HxA-AVDF/`** — Services agreements between Disagree Wisely and Heterodox Academy (HxA) for the Arthur Vining Davis Foundations grant. HxA is the grant recipient and fiscal sponsor; DW executes programmatic work and invoices HxA for cost reimbursement (up to ~$142K per phase). Phase 1 covers platform development and initial deployment (May–Dec 2025); Phase 2 covers scaling, evaluation, and dissemination (Jan–Nov 2026).

### Website/
Two board-facing websites with shared CSS/JS, self-contained and GitHub Pages-ready. Open `index.html` in a browser or host via GitHub Pages.
- **`index.html`** — Landing page linking to both sites.
- **`board-planning.html`** — Meeting agenda and site review notes (at the Website root, not in internal/).
- **`shared/`** — Consolidated CSS and JS used by both sites.
- **`board-onboarding/`** — Slim onboarding guide for new board members. Contains only essential information (governance summaries, insurance overview, financial snapshot).
- **`board-reference/`** — Comprehensive reference with all detail: full governance policies with download links, operational notes, complete financial breakdown, history timeline, and document index.
  - **`docs/`** — 18 bundled PDFs with normalized kebab-case filenames. These are copies of key documents from elsewhere in the repo, included so the website is self-contained.
- **`internal/`** — Internal planning files not linked from the public sites (board meeting slides PDF, meeting transcript, slide generator, meeting slides HTML).

### board-onboarding/ (deprecated)
Original onboarding website. Superseded by `Website/board-onboarding/` and `Website/board-reference/`. Kept for reference; edit the files under `Website/` going forward.

### Misc/
Items that don't fit elsewhere: bank verification letter, conversation transcripts, workspace notes, and the board invitation email sent to Barbara Oakley (`Gmail - Invitation to join Board of Directors.pdf`; a similar one was sent to Ken Stern).

### Archive/
Historical/superseded documents organized by original source. Business expenses were migrated to the SwayAccounting repo. Other subfolders contain old drafts, superseded versions, and historical records.
