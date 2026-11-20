# Contributing to Antares Intelligence

Thank you for helping. This repository holds the ecosystem documentation and the shared brand for the Antares Intelligence projects. Code for Antares-LD, Antares-Atrium, and Antares-Stinger lives in each project's own repository, and changes to a project belong there.

## Ways to help

Open an issue when something is wrong, unclear, or missing: a sentence that overstates what a project does, a broken link, a logo that fails on some background, or a question the docs do not answer. Say where you found it and what you expected.

Open a pull request when you have a specific fix. Keep each pull request to one change, so it can be reviewed and reverted on its own. For anything larger than a correction (a new page, a restructure, a change to the brand), open an issue first so we can agree on the direction before you spend the time.

## Ground rules

These apply to every contribution, including examples inside issues.

1. **Synthetic data only.** Never include real personal, customer, or operational records in an example, test, screenshot, or bug report. Make the data up, and make it obviously made up.
2. **Every claim carries its evidence.** A statement about conformance, Scorpio compatibility, performance, or supported platforms must name the exact build, test suite, storage backend, and caveats it rests on. If the evidence is not public yet, the claim waits.
3. **Show what is missing.** When a comparison has failed, skipped, or unrun cases, report them alongside the passes.
4. **No implied dependencies.** Nothing here may suggest that a project needs a ScientixAI account, a particular cloud vendor, or another Antares component to work.
5. **Be specific about status.** Nothing is released yet. Antares-LD is a working prototype. Atrium and Stinger are in design. Do not describe a version, download, or platform as available until it is.

## Writing style

The documentation is read by engineers deciding whether to trust a project, so plain and exact beats persuasive.

Write in short, direct sentences. Use sentence case for headings ("Run it locally", not "Run It Locally"). Use straight quotes and the Oxford comma. Do not use em dashes; use a comma, parentheses, or a new sentence instead. Do not use emoji. Avoid marketing filler such as "seamless", "cutting-edge", "game-changing", or "unlock the power of"; say what the thing does.

Write the sponsor's name as ScientixAI in prose and Scientix.ai for the domain and legal entity. Never write "Scientix" on its own.

Keep code samples real and copyable, and run them before you submit them.

## Changing the logo

The horizontal lockups in `brand/logos/` (`antares-lockup-horizontal-*.svg`) are drawn as vector outlines and edited directly, as are the two mark files (`antares-mark-*.svg`). The stacked lockups (`antares-lockup-stacked-*.svg`) are generated. Do not edit them by hand.

To change a stacked lockup, edit the matching source file in `references/logo-source/`, then regenerate the outlined copies. The sources set the wordmark in Space Grotesk (ANTARES) and Host Grotesk (INTELLIGENCE), both at weight 700. The script converts that text to vector outlines so the production files need no web fonts.

You need Python 3, the `fonttools` package, and the two variable font files from the [google/fonts](https://github.com/google/fonts) repository (`ofl/spacegrotesk/SpaceGrotesk[wght].ttf` and `ofl/hostgrotesk/HostGrotesk[wght].ttf`). Keep the font files outside this repository.

```bash
python3 -m pip install fonttools
```

```bash
python3 references/logo-source/outline.py "path/to/SpaceGrotesk[wght].ttf" "path/to/HostGrotesk[wght].ttf" brand/logos references/logo-source/antares-lockup-stacked-*.svg
```

Open the results on both a dark and a light background before you submit, and include a screenshot of each in the pull request. Any change to the logo's shape, colors, or type needs an issue and a maintainer's agreement first.

## Pull request checklist

Before you open a pull request, check that:

- The change does one thing, and the description says what and why.
- Every new claim names its evidence, or there are no new claims.
- All example data is synthetic.
- Links work and code samples run.
- Stacked lockups in `brand/logos/` were regenerated with the script, not edited by hand.

## License

This repository is licensed under the [Apache License 2.0](LICENSE). As section 5 of that license states, any contribution you intentionally submit is licensed under the same terms, unless you explicitly say otherwise. Only submit work you have the right to license this way.
