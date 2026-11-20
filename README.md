<picture>
  <source media="(prefers-color-scheme: dark)" srcset="brand/logos/antares-lockup-horizontal-dark.svg">
  <img alt="Antares Intelligence" src="brand/logos/antares-lockup-horizontal-light.svg" width="480">
</picture>

# Antares Intelligence

Antares Intelligence is a family of three open-source projects for working with context data under the ETSI NGSI-LD standard. Each project stands on its own. None of them requires another Antares component, a vendor account, or a private dependency to build, test, or inspect.

This repository holds the ecosystem documentation and the shared brand for the family. It will become the source for the umbrella site at antares-intelligence.org. The code for each project lives in its own repository.

## The projects

| Project | Job | Status |
| --- | --- | --- |
| Antares-LD | Holds and serves context. An NGSI-LD context broker written in Rust, shipped as a single binary with no database server. | Working prototype. No release yet. |
| Antares-Atrium | Moves context reliably between systems. An integration harness. | In design. |
| Antares-Stinger | Captures context at the edge. An optional edge collector. | In design. |

Antares-LD uses Scorpio as its behavioral reference. The project will publish a case-by-case comparison showing where the two brokers agree and where they differ, so an engineer running Scorpio today can decide from evidence whether to switch.

## How we make claims

Nothing here is released yet, so this repository makes no claims about versions, supported platforms, or performance. When those claims arrive, they follow five rules:

1. Lead with what someone can run today, not with a score.
2. Every claim names its build, test suite, storage backend, and caveats. Missing and unrun cases are shown, not hidden.
3. Each project stands alone, with no required account, service, or private dependency.
4. Where Scorpio departs from the NGSI-LD specification, Antares-LD documents the spec-correct difference instead of copying the defect.
5. Synthetic data only. No personal or customer data appears anywhere in these projects, their tests, or their demonstrations.

## What is in this repository

| Path | Contents |
| --- | --- |
| `brand/logos/` | Production logo files: horizontal and stacked lockups for dark and light backgrounds, plus the symbol on its own. The wordmark is converted to outlines, so the files need no web fonts. |
| `references/logo-source/` | Editable sources for the stacked lockups, which use live fonts, and `outline.py`, the script that converts them to outlines. |

## Using the logo

Use `antares-lockup-horizontal-dark.svg` or `antares-lockup-stacked-dark.svg` on dark backgrounds, and the `-light` versions on light ones. Use the mark files where the full lockup will not fit. Below 32 pixels, the star in the crossbar becomes hard to see, and a dedicated small-size mark is still to come. Please do not recolor, stretch, or redraw the files.

The wordmark is set in Space Grotesk and Host Grotesk, both released under the SIL Open Font License.

## Contributing

Issues and pull requests are welcome. Please use synthetic data in any example, test, or bug report, and never real personal or customer records. [CONTRIBUTING.md](CONTRIBUTING.md) covers the ground rules, writing style, and how to change the logo.

## License

The contents of this repository are licensed under the [Apache License 2.0](LICENSE). As section 6 of that license states, it does not grant permission to use the Antares Intelligence name or logo as your own brand. You may use them to refer to these projects.

Built and sponsored by [Scientix.ai](https://scientixai.com). None of the projects depends on a Scientix.ai account or service.
