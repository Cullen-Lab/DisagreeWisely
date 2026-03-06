# Board Onboarding Site — Disagree Wisely, Inc.

> **Note (Feb 2026):** This folder has been superseded by the `Website/` directory, which contains two sites:
> - **`Website/board-onboarding/`** — Slim, self-contained onboarding guide for new board members
> - **`Website/board-reference/`** — Comprehensive reference with all detail, operational notes, and document downloads
>
> Each site is self-contained with its own CSS/JS. Edit the files under `Website/` going forward.

An internal onboarding guide for new board members.

## Structure

```
board-onboarding/
├── index.html              Main page — hero, action items, TOC, loads sections
├── css/
│   └── style.css           All styling (dark theme matching disagreewisely.org)
├── js/
│   └── main.js             Section loading, collapsibles, TOC scroll-spy, mobile nav
├── sections/
│   ├── about.html          About Disagree Wisely — mission, traction, 501(c)(3) status
│   ├── board.html          Board members, decision-making process, terms
│   ├── governance.html     Governance policies — bylaws, COI, financial auth, retention, anti-harassment
│   ├── insurance.html      D&O and cyber/tech insurance details + bylaws indemnification
│   ├── finances.html       Revenue sources, cash position, financial controls
│   ├── history.html        Timeline of key milestones and board resolutions
│   └── documents.html      Reference links to all downloadable documents
└── README.md               This file
```

## How It Works

`index.html` is the entry point. All section content is inlined directly in the HTML for maximum compatibility (works when opened as a `file://` URL without a local server).

**No build tools are needed.** Everything is plain HTML, CSS, and vanilla JS. Just open `index.html` in a browser.

The standalone section files in `sections/` are kept as reference copies but are not loaded at runtime. If you edit content, update both `index.html` (the runtime file) and the corresponding `sections/*.html` file.

### Hosting

When ready to host online, upload the `board-onboarding/` directory to any static host. Document download links use relative paths like `../Governance/Bylaws/...`, so the parent directory (the full Disagree Wisely document collection) must be accessible. If hosting separately from the document collection, update the download link paths accordingly.

## Editing Content

Each section is a standalone HTML fragment in `sections/`. To update a section:

1. Open the relevant file in `sections/`
2. Edit the HTML content
3. Refresh the browser

### Adding a New Section

1. Create a new `.html` file in `sections/` (follow the pattern of existing files — wrap in a `.section` div with a unique `id`)
2. Add a `<div data-section-src="sections/your-new-section.html"></div>` in `index.html` where you want it to appear
3. Add a TOC link in `index.html`'s `.toc-nav`

### Updating Document Links

Download links use relative paths from `board-onboarding/` up to the parent directory. Pattern: `../Folder/Subfolder/filename.pdf`. If the document collection is reorganized, update the `href` attributes in the section files.

## Design System

The site uses CSS custom properties defined at the top of `style.css`:

| Variable | Value | Purpose |
|---|---|---|
| `--color-bg` | `#000` | Page background |
| `--color-text` | `rgba(249,249,249,0.9)` | Body text |
| `--color-accent` | `#6b9eff` | Links, highlights, active states |
| `--color-bg-card` | `#141414` | Card/subsection backgrounds |
| `--font-serif` | `Georgia, ...` | All text |
| `--max-width` | `820px` | Content column width |

### Component Classes

- `.section` / `.section-header` / `.section-body` — Top-level collapsible sections
- `.subsection` / `.subsection-header` / `.subsection-body` — Nested collapsibles
- `.info-card` — Highlighted content card
- `.note` / `.note.warning` — Callout boxes (blue or amber)
- `.download-link` — Styled file download button
- `.timeline` / `.timeline-item` — Vertical timeline
- `.board-grid` / `.board-card` — Board member cards grid
- `.kv-list` — Key-value pair list
- `.action-banner` — Prominent action items box
- `.table-wrap` > `table` — Responsive tables

### Keyboard Shortcuts

- `Ctrl/Cmd + E` — Expand all sections
- `Ctrl/Cmd + Shift + E` — Collapse all sections

## Document Version Policy

Where multiple versions of a document exist (e.g., original + amended Financial Authorization Resolution), the site links to the **most current version**. See the plan file or code comments for the full version resolution table. When updating documents, ensure the links point to the latest adopted version.

## Responsive Behavior

- **Desktop (>900px):** Fixed TOC sidebar on the left, content on the right
- **Mobile (≤900px):** TOC hidden, accessible via floating hamburger button (bottom-right). TOC slides in from the left with an overlay.
- **Print:** All sections expand, TOC hides, colors invert to black-on-white.
