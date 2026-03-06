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
| **Dr. Neil Thomason** | Independent Director. Professor Emeritus, University of Melbourne. Pioneer in analytical reasoning pedagogy and argument mapping. |
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
| `Disagree Wisely, Inc./501c3 Application (Foundation Group)/` | 501(c)(3) application materials: narratives, job descriptions, budgets, Form 1023 drafts, research organizer. |
| `Disagree Wisely, Inc./Insurance/` | Active D&O policy (Carolina Casualty) and Cyber/E&O policy (CFC/Lloyd's). Both effective 11/14/2025. |
| `Disagree Wisely, Inc./Legal/` | Attorney invoices and correspondence (Dentons). |
| `Disagree Wisely, Inc./Personnel/` | Employee documents organized by person. |
| `Disagree Wisely, Inc./Branding/` | Logo files (SVG, PNG) and letterhead template. |
| `Disagree Wisely, Inc./Grants/` | Grant agreements and applications: HxA-AVDF, Snider Foundations, ECI/Wake Forest, FIPSE, NewSchools, TWCF. |
| `Disagree Wisely, Inc./Misc/` | Bank verification letter, transcripts, workspace notes. |
| `Disagree Wisely, Inc./Archive/` | Superseded documents organized by original source. |

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

When content changes in `Disagree Wisely, Inc./Website/`:

1. Copy updated files into `board/`
2. Re-encrypt HTML: `npx staticrypt board/*.html board/board-onboarding/index.html board/board-reference/index.html -p "PASSWORD" -d board -r --remember 30`
3. Re-encrypt PDFs if changed (using pikepdf with the same password)
4. Commit and push

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

---

## Current Status (March 2026)

- **501(c)(3):** Application in progress with Foundation Group; expected IRS submission by mid-April 2026.
- **FIPSE grant:** ~$800K consortium grant (through University of Notre Dame) awaiting 501(c)(3) approval before funds can be disbursed.
- **HxA-AVDF:** Phase 2 services agreement active (Jan-Nov 2026).
- **Snider Foundations:** Two grants ($50K + $25K) received in 2025.
- **ECI/Wake Forest:** Grant application submitted (~$233K over 3 years).
- **TWCF:** Request for Ideas submitted (Feb 2026).
