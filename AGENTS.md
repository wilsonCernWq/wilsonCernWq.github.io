# Repository Guidelines

## Project Structure & Module Organization

This is a Jekyll/GitHub Pages academic site. Top-level content lives in `_pages/`; each paper is a Markdown record in `_publications/`. Liquid templates and reusable partials are in `_layouts/` and `_includes/`. Site data such as navigation and venue names belongs in `_data/`. Theme styles live in `_sass/`, with `assets/css/main.scss` as the entry point; JavaScript, fonts, and the CV are under `assets/`. Store publication figures and thumbnails in `images/pubs/`. Jekyll generates `_site/`; never edit or commit that directory.

## Build, Test, and Development Commands

Use Ruby 3.1.x and Bundler 2.3.x, matching the GitHub Pages dependency stack.

- `bundle install` installs the locked Ruby dependencies.
- `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml` runs the site at `http://127.0.0.1:4000/` with local overrides and live reload.
- `bundle exec jekyll build` performs a production-style build into `_site/` and catches YAML, Liquid, and rendering errors.

`package.json` contains legacy theme dependencies but defines no npm scripts.

## Coding Style & Naming Conventions

Use two-space indentation in YAML, Liquid/HTML, SCSS, and JavaScript. Follow nearby code: JavaScript generally uses single quotes, semicolons, and camelCase; SCSS uses underscore-prefixed partials, hyphenated class names, and existing BEM-style selectors. No formatter or linter is configured, so keep diffs focused and preserve surrounding style.

Name publication files with stable lowercase, hyphenated slugs, for example `_publications/eurovis2024-beyond-exabrick.md`. Keep front matter complete and reference venue keys from `_data/venues.yml` and images relative to `images/` (for example, `pubs/paper-preview.png`).

## Testing Guidelines

There is no automated test suite or coverage target. Before submitting, run `bundle exec jekyll build`, then serve the site and visually inspect every affected route at desktop and mobile widths. For publication changes, check both `/publications/` and `/publications/<basename>/`, including links, images, and BibTeX copying when present.

## Commit & Pull Request Guidelines

Recent history favors concise, action-oriented subjects such as `add code url` or `Improve scientific paper project pages`; Conventional Commit prefixes are not used. Prefer an imperative subject that names the affected page or feature and avoid vague messages.

Pull requests should summarize the change, list affected routes, link relevant issues, and state local build results. Include before/after screenshots for layout, styling, or thumbnail changes. Explain any `Gemfile` or `Gemfile.lock` updates and confirm compatibility with GitHub Pages.
