# Developer guide

This document describes how this site is structured and how to add or change content—especially **publications**. It complements the upstream [AcademicPages](https://academicpages.github.io/) documentation.

## Stack and tooling

| Piece | Role |
|--------|------|
| **Jekyll** | Static site generator (via `github-pages` gem, pinned in `Gemfile`) |
| **Minimal Mistakes–style theme** | SCSS under `_sass/`, compiled to `assets/css/main.css` |
| **Bootstrap 5** | Loaded in `_includes/head.html` for layout utilities |
| **Clipboard.js** | Used by `assets/js/bibtex-copy.js` for “copy BibTeX” on publication pages |

**Ruby:** This project is tested with **Ruby 3.1.x** and **Bundler 2.3.x** (see `Gemfile.lock`). GitHub Pages’ gem set does **not** support Ruby 4.x; use Homebrew `ruby@3.1` (or rbenv) locally.

---

## Repository layout

```
homepage/
├── _config.yml              # Site URL, collections, defaults, plugins
├── _config.dev.yml          # Optional overrides for local development (e.g. url)
├── Gemfile / Gemfile.lock   # Ruby dependencies (github-pages stack)
│
├── _data/
│   └── venues.yml           # Long names for venues referenced as @KEY in front matter
│
├── _includes/               # Partials (masthead, head, scripts, archive cards, …)
├── _layouts/                # Page templates (default, publication, archive, …)
├── _pages/                  # Top-level pages (e.g. publications index, about)
├── _publications/           # One Markdown file per publication (Jekyll collection)
├── _sass/                   # Theme SCSS sources (variables, syntax, bibtex-copy, …)
│
├── assets/
│   ├── css/main.scss        # Entry point: @imports theme + custom partials
│   └── js/bibtex-copy.js    # Adds copy button to ```bibtex``` blocks
│
├── images/                  # Static images (previews, teasers, figures)
│   └── pubs/                # Publication thumbnails (referenced as pubs/… in front matter)
│
└── scripts/                 # Optional TSV → Markdown generators (talks, presentations)
```

**Generated output:** Jekyll writes the built site to `_site/` (ignored by git). Do not edit `_site/` by hand.

---

## Collections and URLs

In `_config.yml`, the `publications` collection is enabled with:

```yaml
collections:
  publications:
    output: true
    permalink: /:collection/:path
```

So a file `_publications/egpgv2022-streaming-volume.md` is served at:

`/publications/egpgv2022-streaming-volume`

Defaults assign the **`publication`** layout to all items in this collection (see `defaults` → `type: publications`).

The publications **index** is `_pages/publications.md` (`permalink: /publications/`), which loops `site.publications` in **reverse chronological order** (`reversed`) and renders each row with `_includes/archive-single-publication.html`.

---

## Venues (`_data/venues.yml`)

In publication front matter, `venue` can be either:

1. **A plain string** — shown as-is on the list and detail page, or  
2. **`@KEY`** — looks up `venues.yml[KEY].name` (e.g. `venue: "@EuroVis"`).

To add a new venue key, edit `_data/venues.yml`:

```yaml
MYCONF:
  name: "Full Conference Name (MYCONF)"
```

Then use `venue: "@MYCONF"` in the publication file.

---

## Adding a new publication

### 1. Choose a filename

Use a **unique, stable** basename (no spaces), for example:

`venue-year-short-title.md`  
Examples: `eurovis2024-beyond-exabrick.md`, `cgf2026-cowe.md`

The basename becomes the URL path segment after `/publications/`.

### 2. Add images (optional but typical)

- **Preview** (list thumbnail): place under `images/pubs/` and reference as `pubs/your-file.png` in front matter.
- **Teaser** (optional, on the detail page): same folder, set `teaser` and optionally `teaser_caption`.

Paths in front matter are usually **relative to `images/`** (the theme prepends `/images/` when building URLs).

### 3. Front matter fields

Minimal required fields:

| Field | Required | Description |
|--------|----------|-------------|
| `title` | Yes | Paper title |
| `venue` | Yes | `@KEY` from `venues.yml` or free text |
| `authors` | Yes | Author string; `Qi Wu` is bolded on the listing |
| `date` | Yes | Used for year display and sort order |
| `collection` | Yes | Must be `"publications"` |
| `preview` | Recommended | Thumbnail under `images/pubs/` → `pubs/....png` |

Common optional fields:

| Field | Description |
|--------|-------------|
| `preprint_url` | PDF link (shown as “PDF”) |
| `arxiv_url` | arXiv link |
| `official_url` | Publisher / DOI page |
| `code` | GitHub or code URL |
| `blog` | Blog post URL |
| `project_page` | **External** project URL; see below |
| `award` | Shown in coral on the list |
| `teaser` | Larger figure on detail page |
| `teaser_caption` | Caption under teaser |

#### `project_page`: internal page vs external link

- **If `project_page` is set** (e.g. NVIDIA project URL):  
  The listing’s “Project Page” link goes **to that URL**. The Markdown body under `---` can be **empty**; you normally do not duplicate abstract/BibTeX on this site.

- **If `project_page` is omitted**:  
  “Project Page” points to **`/publications/<basename>/`**. Put abstract, figures, supplementary embeds, and BibTeX in the Markdown body.

This behavior is implemented in `_includes/archive-single-publication.html`.

### 4. Body content (detail page only)

When you host the full page on this site, typical sections are:

- `### Abstract`
- Figures (`<figure>`, `<img>`, `<figcaption>`)
- `### Supplementary Video` (optional)
- `### BibTex` with a fenced block:

````markdown
```bibtex
@article{...,
  ...
}
```
````

Use the language tag **`bibtex`** so the BibTeX copy script can find the block (see below).

### 5. Build and check

```bash
bundle exec jekyll serve
```

Open `/publications/` for the list and `/publications/your-file-basename/` for the detail page.

---

## BibTeX “copy to clipboard”

- **Styles:** `_sass/_bibtex-copy.scss` (imported from `assets/css/main.scss`).
- **Script:** `assets/js/bibtex-copy.js`, included from `_includes/scripts.html`.
- **Requirement:** Code blocks must use ` ```bibtex ` (Rouge renders them as `.language-bibtex`).

Clipboard.js is loaded before `bibtex-copy.js`. No extra setup is needed beyond using the `bibtex` fenced block.

---

## Styling and theme customization

- **Global tokens:** `_sass/_variables.scss` (fonts, colors, type scale, breakpoints).
- **Syntax highlighting:** `_sass/_syntax.scss` (code blocks, Solarized-like theme).
- **BibTeX UI:** `_sass/_bibtex-copy.scss`.

After changing SCSS, run Jekyll so `main.css` is regenerated.

---

## Local development quick reference

```bash
# Use Ruby 3.1.x (example: Homebrew)
export PATH="/opt/homebrew/opt/ruby@3.1/bin:$PATH"

cd /path/to/homepage
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000/
```

Optional: `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml` if you use `_config.dev.yml` for local URL overrides.

---

## GitHub Pages

The site is intended to deploy like a standard **user/org GitHub Pages** repo (`Gemfile` uses `github-pages`). Push to the configured branch; GitHub builds with its supported Jekyll version. Keep `Gemfile` / lockfile compatible with [Pages dependency versions](https://pages.github.com/versions/).

---

## Further reading

- Upstream template: [AcademicPages](https://github.com/academicpages/academicpages.github.io/)
- Optional generators: `scripts/` and TSV files for talks/presentations (see upstream docs)
