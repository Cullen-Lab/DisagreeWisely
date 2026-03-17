# Disagree Wisely, Inc.

Florida nonprofit corporation focused on civil discourse research and education. Incorporated April 2, 2025.

---

## Repository Structure

This repo serves three purposes:

1. **Public website** — `index.html` and `CNAME` at the repo root are deployed via GitHub Pages to [www.disagreewisely.org](https://www.disagreewisely.org).
2. **Password-protected board portal** — `board/` contains the encrypted board sites, live at [www.disagreewisely.org/board/](https://www.disagreewisely.org/board/). HTML pages are encrypted with [StatiCrypt](https://github.com/robinmoisson/staticrypt) (AES-256); PDFs are password-protected with AES-256 via pikepdf. All use the same password.
3. **Organizational documents** — Everything under `Disagree Wisely, Inc./` (governance, financials, grants, board websites, etc.).

---

## At a Glance

| | |
|---|---|
| **EIN** | 33-5034018 |
| **State** | Florida (Doc #N25000004307) |
| **Incorporated** | April 2, 2025 |
| **Address** | 7901 4th St N, Suite 300, St. Petersburg, FL 33702 |
| **Registered Agent** | Northwest Registered Agent LLC |
| **501(c)(3) Status** | Pending (application in progress with Foundation Group) |
| **Website** | [disagreewisely.org](https://www.disagreewisely.org) |

---

## Board of Directors

| Name | Role |
|---|---|
| **Dr. Simon Cullen** | President & CEO. Co-founder; PhD Philosophy (Princeton). Leads research and organizational strategy. |
| **Dr. Nicholas DiBella** | Secretary, Treasurer & CTOO. Co-founder; PhD Philosophy (Stanford), BS (MIT). Leads technology, operations, and financial oversight. |
| **Dr. Neil Thomason** | Director. Professor Emeritus, University of Melbourne. Pioneer in analytical reasoning pedagogy and argument mapping. |
| **Ken Stern** | Director. Attorney, author, Director of the Bard Center for the Study of Hate. |
| **Dr. Barbara Oakley** | Director. Distinguished Professor of Engineering, Oakland University. Co-creator of "Learning How to Learn." |

**Advisory (non-voting):** Cristina Koppel (founding member).

---

## Staff

| Name | Role | Reports To |
|---|---|---|
| Dr. Simon Cullen | President & CEO | Board of Directors |
| Dr. Nicholas DiBella | CTOO (Chief Technology and Operations Officer) | Board of Directors |
| Rachel Sipser | Director of Communications (Sway Project), part-time | Nicholas DiBella |

---

## Directory Guide

| Path | Description |
|---|---|
| `index.html` | Public homepage deployed to disagreewisely.org via GitHub Pages. |
| `CNAME` | GitHub Pages custom domain configuration. |
| `board/` | Password-protected board portal (encrypted HTML + PDFs), deployed at disagreewisely.org/board/. |
| `Disagree Wisely, Inc./Website/` | Board-facing websites (unencrypted source files). |
| `Disagree Wisely, Inc./Governance/` | Bylaws, policies (COI, document retention, anti-harassment, intern NDA), board resolutions, meeting minutes. |
| `Disagree Wisely, Inc./Incorporation and Tax/` | Florida incorporation filings, federal EIN/tax docs, Pennsylvania tax registrations. |
| `Disagree Wisely, Inc./Financials/` | Bank statements, banking setup, expense tracking. |
| `Disagree Wisely, Inc./501c3 Application (Foundation Group)/` | 501(c)(3) application materials: Form 1023 full application (received March 16, 2026), cross-reference analysis, narratives, job descriptions, budgets, Form 1023 drafts, research organizer. |
| `Disagree Wisely, Inc./Insurance/` | Active D&O policy (Carolina Casualty) and Cyber/E&O policy (CFC/Lloyd's). Both effective 11/14/2025. |
| `Disagree Wisely, Inc./Legal/` | Attorney invoices and correspondence (Dentons). |
| `Disagree Wisely, Inc./Personnel/` | Employee documents organized by person. |
| `Disagree Wisely, Inc./Branding/` | Logo files (SVG, PNG) and letterhead template. |
| `Disagree Wisely, Inc./Grants/` | Grant agreements and applications: HxA-AVDF, Snider Foundations, ECI/Wake Forest, FIPSE, NewSchools, TWCF. |
| `Disagree Wisely, Inc./Misc/` | Bank verification letter, transcripts, workspace notes. |
| `Disagree Wisely, Inc./Archive/` | Superseded documents organized by original source. |
| `organizational-assessment-2026-03.md` | Organizational assessment (March 2026): governance, financial record-keeping, documentation graded absolute and relative to peer nonprofits. |
| `action-items-2026-03-16.html` | Comprehensive action items compiled from both repos, organized by deadline, topic, and compliance calendar. |
| `site-audit-2026-03-09.html` | Board site audit: inconsistencies, stale content, structural issues, and questions. |

See [`Disagree Wisely, Inc./FOLDER-ORGANIZATION.md`](Disagree%20Wisely%2C%20Inc./FOLDER-ORGANIZATION.md) for the complete directory tree.

---

## Board Portal

The board portal is live at **[www.disagreewisely.org/board/](https://www.disagreewisely.org/board/)** and password-protected.

- **Landing page** — Links to both sites below.
- **Onboarding Guide** — Slim overview for new board members.
- **Board Reference** — Comprehensive reference with governance policies, financials, operational notes, and 18 downloadable documents.

**Security:** All HTML pages are encrypted with StatiCrypt (AES-256, decrypted client-side). All PDFs are password-protected (AES-256). Board members enter the password once; the browser remembers it for 30 days.

**To view locally:** Open `Disagree Wisely, Inc./Website/index.html` in a browser (unencrypted source files).

### Updating the board site

When content changes in `Disagree Wisely, Inc./Website/`, you must re-encrypt and redeploy:

The board portal password is stored in `.board-password` (gitignored). All commands below read from that file.

**HTML pages** (StatiCrypt AES-256, decrypted client-side):
```bash
PASSWORD=$(cat .board-password | tr -d '[:space:]')

# Copy source files to temp location, encrypt, then deploy to board/
cp "Disagree Wisely, Inc./Website/index.html" /tmp/dw_index.html
cp "Disagree Wisely, Inc./Website/board-onboarding/index.html" /tmp/dw_onboarding.html
cp "Disagree Wisely, Inc./Website/board-reference/index.html" /tmp/dw_reference.html

# Encrypt each (uses password_template.html for the login screen)
npx staticrypt /tmp/dw_index.html -p "$PASSWORD" -d /tmp/dw_out --remember 30 --short \
  --template board/password_template.html --template-title "Board Portal" \
  --template-instructions "Resources for the Board of Directors." \
  --template-placeholder "Password" --template-error "Wrong password." \
  --template-toggle-show "Show" --template-toggle-hide "Hide"
# Repeat for onboarding and reference (change --template-title accordingly)

# Deploy
cp /tmp/dw_out/dw_index.html board/index.html
cp /tmp/dw_out/dw_onboarding.html board/board-onboarding/index.html
cp /tmp/dw_out/dw_reference.html board/board-reference/index.html
```

**PDF documents** (pikepdf AES-256):
```python
import pikepdf
# Read password from .board-password
password = open('.board-password').read().strip()
pdf = pikepdf.open('source.pdf')
pdf.save('board/board-reference/docs/output.pdf',
         encryption=pikepdf.Encryption(owner=password, user=password, aes=True, R=6))
```

**Shared assets** (CSS/JS): Copy `Disagree Wisely, Inc./Website/shared/` to `board/shared/`.

**PDF generation** (for minutes etc.): Use Chrome headless with `--no-pdf-header-footer` to avoid browser-generated headers/footers:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-sandbox \
  --print-to-pdf="output.pdf" --no-pdf-header-footer "file:///path/to/source.html"
```

Then commit and push. GitHub Pages will deploy automatically.

---

## Key Documents Quick Reference

| Document | Path |
|---|---|
| Bylaws (signed) | `Disagree Wisely, Inc./Governance/Bylaws/Revised BYLAWS - Non Member Standard signed.pdf` |
| Conflict of Interest Policy (signed) | `Disagree Wisely, Inc./Governance/Policies/Conflict of Interest/ConflictofInterest-General signed.pdf` |
| Articles of Incorporation | `Disagree Wisely, Inc./Incorporation and Tax/Florida Incorporation/disagree wisely articles of incorporation.pdf` |
| EIN Letter | `Disagree Wisely, Inc./Incorporation and Tax/Federal Tax/05-20-25 -  - EIN Letter - Disagree Wisely Inc.pdf` |
| D&O Insurance Policy | `Disagree Wisely, Inc./Insurance/Active Policies/IT2-Policy_DDP-2315240-P1.pdf` |
| Cyber/E&O Insurance Policy | `Disagree Wisely, Inc./Insurance/Active Policies/SST-ESO0040579703.pdf` |
| Financial Authorization (current) | `Disagree Wisely, Inc./Governance/Board Resolutions/Financial Authorization (Amended 12.13.2025).md` |
| Board Resolutions (Jul 2025) | `Disagree Wisely, Inc./Governance/Board Resolutions/DW Board Resolutions Jul 2025.pdf` |
| Form 1023 (501(c)(3) application) | `Disagree Wisely, Inc./501c3 Application (Foundation Group)/Form 1023 full application DW.pdf` |
| Form 1023 Cross-Reference | `Disagree Wisely, Inc./501c3 Application (Foundation Group)/form-1023-cross-reference.html` |

---

## Current Status (March 2026)

- **Board:** First full board meeting held March 6, 2026 (all 5 directors present via Zoom, ~1h46m). Officers re-elected unanimously: Cullen (President), DiBella (Secretary/Treasurer), Thomason (Director). Board briefed on all major items below. [Minutes in board-reference site.](Disagree%20Wisely%2C%20Inc./Website/board-reference/index.html#minutes-2026-03-06)
- **501(c)(3):** Form 1023 draft received from Foundation Group on March 16, 2026. Cross-referenced against all internal records ([analysis](Disagree%20Wisely%2C%20Inc./501c3%20Application%20%28Foundation%20Group%29/form-1023-cross-reference.html)). Requesting 509(a)(2) public charity classification. Two items raised with FG: Q10 foreign operations answer and officer appointment language in activity narrative. Standard IRS review (not expedited).
- **FIPSE grant:** ~$800K consortium grant (through University of Notre Dame) awaiting 501(c)(3) approval. Year 1 is a ramp-up year (~$60K to DW); larger amounts in subsequent years. Funds disbursed yearly to Notre Dame. FIPSE funds cannot be used for programming/coding — only research, education, infrastructure, training, and support staff.
- **Learning Agency:** ~$125K Tools Competition funds retained in DW; reallocation in progress (LA expressed "no concerns regarding reallocation"). Funds restricted to nonprofits — cannot be redirected to PBC. Simon meeting with LA again to finalize.
- **HxA-AVDF:** Phase 2 services agreement active (Jan-Nov 2026). Amending to remove development language not feasible per HxA ED; development costs will continue through May/June 2026 (net cost to DW: zero).
- **Snider Foundations:** Two grants ($50K + $25K) received in 2025.
- **ECI/Wake Forest:** Grant application submitted (~$233K over 3 years).
- **TWCF:** Request for Ideas submitted (Feb 2026).
- **Growth:** 80+ institutions, ~10,000 students, ~130 instructors (up from ~30 institutions / ~2,000 students at start of 2025). University-level adoption talks with U of Michigan (potentially 8,000 students), SUNY, Columbia, CUNY, MIT.
- **CMU IP dispute:** CMU asserts joint ownership of Sway IP. Co-founders' position: educational courseware exemption (CMU IP Policy 3-6-1). Board advised seeking independent legal counsel; Ken Stern offered introduction to Laura Ellsworth (Jones Day).
- **PBC:** For-profit Public Benefit Corporation not yet incorporated. Will hold Sway IP; can be done for ~$50 in Delaware.
