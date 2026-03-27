# Qi Wu — academic homepage

A GitHub Pages site for an academic profile and publications. This repository is based on the [AcademicPages Jekyll theme](https://github.com/academicpages/academicpages.github.io/) (MIT License). See `LICENSE.md`.

## Documentation

| Document | Contents |
|----------|----------|
| **[DEV.md](DEV.md)** | Project structure, configuration, how to add publications, venues, images, BibTeX copy button, and local development |
| [AcademicPages docs](https://academicpages.github.io/) | Upstream template behavior and markdown generator scripts |

## Run the site locally

Prerequisites: **Ruby 3.1.x** (or another version compatible with the `github-pages` gem), **Bundler**, and **Git**. This project uses GitHub Pages’ gem stack; Ruby 4.x is not supported by that stack.

```bash
cd /path/to/this/repo
bundle install
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000/`. For live reload, use:

```bash
bundle exec jekyll serve --livereload
```

**macOS (Homebrew):** Install Ruby 3.1 with `brew install ruby@3.1` and put it on your `PATH` before `bundle install`. See [DEV.md](DEV.md#local-development-quick-reference) for details.

**Linux (apt):** The upstream template often suggests `sudo apt install ruby-dev ruby-bundler nodejs`; adjust for your distribution.

If `bundle install` fails, see `Gemfile.lock` and try `bundle update` or regenerate the lockfile only after reading GitHub Pages’ [dependency versions](https://pages.github.com/versions/).

## Markdown / TSV generators

The `scripts/` folder contains utilities that convert TSV files (e.g. `talks.tsv`, `presentations.tsv`) into Markdown for the template. See the notebooks and comments in the AcademicPages repository for how to run them.

## Adding a publication

**Short version:** Add a new Markdown file under `_publications/`, set front matter (`title`, `venue`, `authors`, `date`, `preview`, …), add images under `images/pubs/` if needed, and optionally use `project_page` to link out instead of hosting the full page.

**Full checklist and field reference:** [DEV.md — Adding a new publication](DEV.md#adding-a-new-publication).
