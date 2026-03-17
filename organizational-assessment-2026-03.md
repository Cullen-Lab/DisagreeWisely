# Organizational Assessment — Disagree Wisely, Inc.

**Date:** March 16, 2026
**Scope:** Review of DisagreeWisely and SwayAccounting repositories — governance, financial record-keeping, documentation, and organizational maturity relative to peer nonprofits at a comparable stage.
**Context:** Pre-501(c)(3) Florida nonprofit, ~11 months post-incorporation, ~$245K 2025 revenue, 2 operational staff (co-founders), 5-person board, grant-funded.

---

## Overall Grade: A- (absolute) / A+ (relative to peer nonprofits at this stage)

This assessment evaluates the organizational infrastructure of Disagree Wisely, Inc. — a Florida nonprofit incorporated in April 2025, with ~$245K in 2025 grant revenue, two operational staff (both co-founders), a 5-person board of directors, and a 501(c)(3) application pending. The organization develops and researches educational tools for civil discourse (primarily the Sway platform), funded by a mix of foundation grants (HxA/AVDF, Snider, Ben Delo), competition prizes (Learning Agency), and pending federal grants (FIPSE).

The assessment covers five dimensions: **governance** (policies, resolutions, board processes, compliance infrastructure), **financial record-keeping** (transaction tracking, receipt management, grant reporting, tax compliance), **documentation and organization** (how corporate documents, board materials, and operational knowledge are stored and presented), **risk and insurance** (D&O, cyber/tech liability, indemnification), and **operational resilience** (key-person risk, institutional knowledge capture, succession readiness).

Two grades are given for each dimension. The **absolute grade** measures against the full spectrum of nonprofit organizational practice — including mature, well-staffed organizations with dedicated operations teams and seven-figure budgets. The **relative grade** measures against the actual peer set: pre-501(c)(3) nonprofits with <$500K revenue, 1-3 operational staff, a small board, and ~1 year of operating history.

On an absolute scale, the organization earns an **A-**. The governance, documentation, insurance, and financial systems are strong by any standard. The gaps that keep this from an A or A+ (no independent bookkeeper, no formal fund accounting categories, key-person risk, an unresolved whistleblower policy) are real and worth closing, but they are the kinds of gaps that reflect the constraints of a two-person team, not inattention or disorganization.

Against the peer set, the organization earns an **A+**. It is in the top 2-5% across every dimension measured. There is very little that a peer organization at this stage could be doing that Disagree Wisely is not already doing, and several things — the custom grant-tracking accounting system, the encrypted board portal, the financial authorization resolution with spending caps — that essentially no peers are doing.

| Dimension | Absolute | vs. Peers | What drives the gap |
|---|---|---|---|
| Governance | A | A+ | Peers typically have bylaws and maybe COI (because their advisor required them). DW has 5 formal policies, numbered resolutions, a financial authorization resolution with spending caps, and a compliance calendar. This is infrastructure that most nonprofits don't build until they're 5-10x larger. |
| Financial Record-Keeping | A- | A+ | Peers use QuickBooks (poorly suited for grant tracking), a single spreadsheet, or nothing. DW has a purpose-built system with per-funding-source ledgers, receipt verification, automated grant reporting, split transaction tracking, and multi-jurisdiction tax compliance. The absolute grade docks points for the lack of formal restricted/unrestricted fund accounting and no independent review — things that matter on an absolute scale but that virtually no peer even thinks about. |
| Documentation & Organization | A | A+ | Peers store documents in Google Drive or Dropbox with inconsistent structure, email board materials as attachments, and have no version history. DW has a Git-versioned organizational filing cabinet with a comprehensive directory guide, an encrypted board portal with professional UI, and a self-audit process that tracks content drift. The board portal alone is something most nonprofits at any size never build. |
| Risk & Insurance | A | A+ | Most peers have no insurance at all, or acquire D&O reluctantly in year 2-3. DW has both D&O ($1M, $0 deductible on personal claims, defense costs outside the limit) and Cyber/Tech E&O ($1M) within 7 months of incorporation, both with full prior acts coverage. Many nonprofits at 5x the revenue don't carry this coverage. |
| Operational Resilience | B | B+ | Key-person dependency is universal at this stage — every 1-3 person nonprofit has it. The absolute grade is a B because it's the organization's most significant structural risk. The slight edge over peers (B+) comes from the fact that DW has more institutional knowledge captured in writing (board portal, README, SwayAccounting user guide, governance docs) than most peers, which would give a successor a fighting chance. Most peer orgs would leave a successor with a Google Drive and a confused board. |

---

## Governance: A

What is in place — bylaws, COI policy (with annual attestation), anti-harassment policy, document retention policy, financial authorization resolution with spending caps, numbered and dated board resolutions, detailed meeting minutes — is closer to what you'd expect from a $5-10M nonprofit with a full-time operations staff, not an 11-month-old org with two co-founders doing everything.

Specific strengths:

- **Financial Authorization Resolution** with pre-approved categories and dollar caps is genuinely unusual at this stage. Most small nonprofits operate on vague "the ED can spend what's reasonable" norms until they get burned.
- **Numbered resolutions with formal vote records** — many nonprofits 10x this size don't do this cleanly.
- **D&O + Cyber/Tech E&O insurance** within 7 months of incorporation — a lot of small nonprofits skip D&O entirely or defer it for years. Having both policies with full prior acts coverage is smart.
- **Annual compliance calendar** — most nonprofits don't formalize this until after they've missed a filing deadline.

Gaps:

- The **Whistleblower Policy** is in limbo (board voted to adopt it June 2025, Foundation Group never delivered the document). This is a real gap — the IRS asks about it on the 990, and some state AGs care. It's low-effort to close.
- The **Resolution 2025-03/04 dating inconsistency** (July 1 meeting vote vs. July 10-11 written consent) is the kind of thing that's harmless now but could matter if anyone ever scrutinizes early governance. Worth resolving with the signed PDF as the authority.

---

## Financial Record-Keeping: A-

The SwayAccounting system is remarkable. The core problem it solves — tracking every dollar by funding source across multiple grants with different compliance regimes — is exactly the thing that causes small grant-funded nonprofits the most pain. Most organizations at this stage are using QuickBooks (which handles this poorly), a tangle of spreadsheets, or nothing at all.

### Strengths

- **Per-funding-source ledgers** with a unified master view — this is the right architecture.
- **Receipt verification** (matching amounts/dates against transactions) — this level of rigor is what federal auditors expect under 2 CFR 200. The muscle is being built now that FIPSE will require.
- **Funder-ready report generation** — categorized expense reports with concatenated receipt packages and certification statements on demand is a significant operational advantage. Most small nonprofits spend days assembling these manually.
- **Split transaction tracking** — handling one bank transaction across multiple funding sources is the exact edge case that breaks simpler systems.
- **Tax compliance tracking across jurisdictions** — the multi-state payroll complexity (FL, PA) is real, and having it systematized rather than in someone's head is important.
- **Grant planning module** — application tracking, multi-year budgets, document checklists, and key contacts. This is operational infrastructure, not just bookkeeping.

### Where it could be stronger

- **No formal fund accounting separation** between restricted and unrestricted funds at the ledger level. Funding sources are tracked (which is essentially this), but the terminology and structure don't yet map to standard nonprofit accounting categories (temporarily restricted, permanently restricted, unrestricted). This will matter when the first 990 is filed and if the org ever gets audited.
- **The $245K revenue figure** that doesn't reconcile with the grant tables is a yellow flag — not because anything is wrong, but because it suggests the distinction between "cash received in calendar year 2025" vs. "total grant commitments" isn't yet crisp in the financial narrative. An auditor or sophisticated board member would ask about this.
- **No independent bookkeeper or accountant review.** Everything flows through one person. That's normal at this size, but as soon as it's affordable, having even a part-time bookkeeper who provides a second pair of eyes would strengthen internal controls. The IRS and funders like to see separation of duties.

---

## Documentation & Organization: A

The DisagreeWisely repo as an organizational filing cabinet is well-structured: clear directory hierarchy, comprehensive README with directory guide, key documents quick reference, versioned governance documents, and an encrypted board portal that's more professional than what 95% of nonprofits offer their directors.

The board portal — with collapsible sections, TOC scroll-spy, light/dark mode, mobile-responsive layout, action items with status badges — is frankly overkill for a 5-person board, but in the best way. It signals to new directors that the organization is serious and well-run, which matters for engagement and trust.

The site audit document (March 9, 2026) shows healthy self-awareness about where information has drifted across documents. The inconsistencies it found are typical growing pains, not signs of dysfunction.

---

## Operational Resilience: B

The entire organizational knowledge, financial system, governance records, and operational infrastructure lives in the heads (and GitHub repos) of two people. The SwayAccounting system is custom software that only one person fully understands. If something happened to both co-founders simultaneously, a successor would face a steep learning curve.

This is completely normal at this stage — and the user guide in SwayAccounting helps — but as the org grows, documenting the "how we operate" knowledge (beyond the "what we've decided" governance docs, which are excellent) becomes important. The board portal is a good start on this.

---

## Peer Comparison

The peer set for this comparison: pre-501(c)(3) nonprofits, ~$200-500K in grant revenue, 1-3 operational staff, a small board (3-7 members), in the education or research space, approximately 1 year of operating history.

### What typical peers look like

| Dimension | Typical peer practice | Disagree Wisely |
|---|---|---|
| **Bylaws & COI** | Has both — because their formation attorney or Foundation Group required them. Often boilerplate, filed and forgotten. | Has both, plus anti-harassment, document retention, and financial authorization policies. COI has annual attestation tracked in minutes. |
| **Other policies** | None. Anti-harassment, document retention, and financial authorization policies are almost unheard of at this stage. | All three in place, with the financial authorization resolution including specific dollar caps by category. |
| **Board minutes** | A paragraph in a follow-up email, or absent entirely. | Detailed, formal minutes with motions, vote counts, and recusals recorded. Multiple meeting formats documented (in-person, Zoom, written consent). |
| **Resolutions** | Informal or unnumbered. Often just "the board agreed to..." in an email thread. | Sequentially numbered (2025-01 through 2025-09, 2026-01 through 2026-02), dated, with vote mechanism recorded. |
| **Financial tracking** | QuickBooks (which struggles with per-grant tracking), a Google Sheet, or nothing formalized. | Purpose-built system with per-funding-source ledgers, receipt verification, automated grant reporting, split transactions, tax compliance, and financial planning. |
| **Receipts** | A Google Drive folder, a Dropbox, or a literal shoebox. Organized retrospectively when a funder asks. | Uploaded, associated with transactions, organized by funding source and reporting period, with automated amount/date verification against transaction records. |
| **Grant reporting** | Manual assembly. Treasurer spends days pulling together spreadsheets and scanning receipts before each report deadline. | Generates funder-ready reports (Excel + PDF + concatenated receipt packages with table of contents) on demand. Format-specific templates for AVDF and Snider reporting. |
| **Insurance** | None, or D&O only, acquired reluctantly in year 2-3 after a board member asks about it. | D&O ($1M, $0 deductible personal, defense outside limit) and Cyber/Tech E&O ($1M) both in place within 7 months. Full prior acts. $4,600/year total. |
| **Board communications** | Email attachments. Maybe a shared Google Drive folder. | Encrypted board portal with professional UI (collapsible sections, TOC, dark/light mode, mobile responsive), two sub-sites (onboarding + reference), and 18+ downloadable documents. |
| **Document organization** | Google Drive or Dropbox with inconsistent folder structure. No version history. | Git-versioned repository with clear directory hierarchy, comprehensive README, key documents quick reference, and a self-audit process that tracks content drift across documents. |
| **Compliance calendar** | Doesn't exist. Deadlines are tracked in someone's head or discovered when missed. | Formalized table in the board reference with recurring obligations by month, assigned owners, and specific regulatory references. |

### Where peers sometimes do better

Disagree Wisely is not ahead in every conceivable way. A few areas where some (not most) peers have an edge:

- **Independent financial review.** Some peer orgs, especially those spun out of universities or with fiscal sponsors, inherit access to a bookkeeper or accountant from day one. DW's financial system is more sophisticated, but everything flows through one person.
- **Formal fund accounting language.** Orgs that use a proper nonprofit accounting firm from the start sometimes have cleaner restricted/unrestricted fund categorization, even if their actual tracking is worse. DW tracks funding sources meticulously but hasn't yet mapped them to the standard GAAP nonprofit categories.
- **Whistleblower policy.** Some peers have this in their initial policy bundle (often because their attorney included it as boilerplate). DW voted to adopt one but never received the document from Foundation Group.
- **Simpler tech stack.** DW's custom accounting system is a strength but also a liability — it's custom software that requires maintenance and that only one person fully understands. A peer using QuickBooks has worse grant tracking but zero maintenance burden and easy handoff.

### Distribution estimate

Based on the practices observed across both repositories, a rough estimate of where Disagree Wisely falls in the distribution of similarly-staged nonprofits:

| Percentile range | Typical profile |
|---|---|
| **Bottom 25%** | Bylaws only, no other policies. Minutes are informal emails. Financial records are a bank login and maybe a spreadsheet. No insurance. Documents scattered across personal drives. |
| **25th–50th** | Bylaws + COI. Basic QuickBooks or Wave. D&O insurance (maybe). Google Drive with some structure. Minutes exist but are sparse. |
| **50th–75th** | Bylaws + COI + one other policy. QuickBooks with some grant tracking. D&O insurance. Shared Drive with reasonable structure. Regular board meetings with decent minutes. |
| **75th–90th** | Full policy suite. Good financial tracking (QuickBooks + supplementary spreadsheets). D&O + maybe one other policy. Professional-looking board materials. Compliance awareness. |
| **90th–95th** | Everything above, plus formal financial authorization, compliance calendar, and systematic grant reporting. |
| **95th–99th (DW is here)** | All of the above, plus: purpose-built financial system with per-grant tracking and automated reporting, encrypted board portal, version-controlled organizational documents, self-audit processes, and comprehensive insurance coverage with full prior acts. |

---

## Recommended Next Steps (in rough priority order)

1. **Close the Whistleblower Policy gap** — follow up with Foundation Group or adopt a standard template. Low effort, high value for IRS and state compliance.
2. **Resolve the Resolution 2025-03/04 dating inconsistency** — check the signed PDF, update whichever source is wrong.
3. **Clarify the $245K revenue figure** — make the financial narrative explicit about cash received vs. total grant commitments.
4. **Add Learning Agency to the board-reference revenue table** — already noted in the site audit; the onboarding site has it but the reference site doesn't.
5. **Rename SwayAccounting** — to reflect the organization (e.g., DWAccounting), as already planned.
6. **When affordable, engage a part-time bookkeeper** — for independent review and separation of duties. Even quarterly review would help.
7. **Consider mapping funding sources to formal fund accounting categories** (restricted/unrestricted) — preparation for the first 990 and any future audit.

---

## Bottom Line

The governance infrastructure is mature beyond this stage, the financial system is genuinely innovative for a small nonprofit, and the documentation is thorough. The gaps noted are minor relative to how much is already in place. When the 501(c)(3) comes through and FIPSE activates, the organization will be operationally ready in ways that most organizations at this funding level simply are not.
