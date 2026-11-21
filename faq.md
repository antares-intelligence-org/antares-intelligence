<!-- Generated from https://antares-intelligence.org/faq/ by build_agent_files.py. Edit the HTML, not this file. -->

# Straight answers, including the ones about what isn't ready

What the projects do, what you can run today, how Antares Core relates to Scorpio, and how to get involved. When something is a plan rather than a shipped capability, the answer says so.

## About Antares Intelligence

### What is Antares Intelligence?

Antares Intelligence is a family of three open-source projects for sharing context data under the ETSI NGSI-LD standard. Antares Core is a context broker that keeps current state and history. Antares-Atrium governs what each partner may share and receive. Antares-Stinger translates approved data between existing systems and NGSI-LD. Each organization keeps its own systems, vocabulary, and records; what crosses the boundary is the approved signal and a receipt.

### Who builds it?

The projects are built and sponsored by Scientix.ai Inc. None of them depends on a Scientix.ai account or service, and each one builds, tests, and runs without any private dependency.

### Is Antares only for healthcare or clinical research?

No. The projects are domain-neutral and work for any NGSI-LD use: cities, agriculture, energy, supply chain, manufacturing, finance, and health. The idea started from comparing smart-city operations with clinical research, which is why some of the examples come from health, but the homepage scenarios cover five industries.

### Is it free and open source?

Yes. The projects are licensed under the Apache License 2.0, so you can use, change, and redistribute them, including commercially. The license doesn't grant permission to use the Antares Intelligence name or logo as your own brand; you may use them to refer to these projects.

## Antares Core

### Is Antares Core ready for production?

No. Antares Core is a working prototype with no release yet. There is no released version number and no published binaries, and no platform is listed as supported until it has been verified.

### How is Antares Core different from Scorpio?

Antares Core is written in Rust and runs as a single binary with no database server, where Scorpio runs alongside a PostgreSQL database. Antares Core uses Scorpio as its behavioral reference and plans to publish a case-by-case comparison showing where the two brokers agree, where they differ, and which cases were not run. Where Scorpio departs from the NGSI-LD specification, Antares Core documents the spec-correct behavior instead of copying the difference.

### Can Antares Core replace Scorpio?

That's the decision the project is built to support, and it isn't one to make yet. The goal is that an engineer running Scorpio can install a verified build, run it against their own workflow, and decide from published evidence. Until there is a release and its comparison evidence, the honest answer is not yet.

### Does Antares Core conform to the NGSI-LD specification?

The project keeps three kinds of claims separate: conformance to the NGSI-LD specification, observed compatibility with Scorpio, and measured performance. No conformance score is published yet. When one is, it will name the exact build, test suite, storage backend, and caveats, and it will show missing and unrun cases rather than hide them.

### What storage does Antares Core use?

SQLite is the working storage path, and it serves the temporal API, so you can ask how an entity changed over time. An in-memory store exists for exploration and does not keep temporal history. PostgreSQL and PostGIS are not verified and are not supported today.

### What address does Antares Core listen on?

By default the prototype listens on `0.0.0.0:1026`, the same default port the Orion and Orion-LD brokers use. Set the `ANTARES_BIND` environment variable to change it.

## Atrium and Stinger

### Can I use Antares-Atrium or Antares-Stinger today?

Not yet. Both are in design and have not been released. The homepage scenarios show how they are designed to work, not features you can run today.

### What will Antares-Atrium do?

Atrium is the governance layer. It controls what each partner may share and receive, approves the vocabulary version (the JSON-LD @context) in use, and lets subscribers replay the changes they missed while offline.

### What will Antares-Stinger do?

Stinger is the interface translator. It translates approved data between source systems and NGSI-LD, so it can link an ERP, an existing IoT gateway, or a partner system, and it holds updates locally when the network goes down. The design goal is that existing systems keep working as they are, with no equipment replacement.

### Do I need all three projects?

No. Each project stands on its own. None requires another Antares component, a vendor account, or a private dependency to build, test, or run. You can use Antares Core by itself as an NGSI-LD broker.

## Sharing and data

### What is a receipt?

A receipt is the record that travels with shared information. Every receipt answers four questions: the source, what was observed or approved, who authorized it, and when. Sharing the signal with its receipt lets a partner act on it and audit it later, without ever seeing the record it came from.

### How do two organizations with different vocabularies share data?

They agree on a versioned JSON-LD @context, which maps each organization's terms to shared meanings. Each side keeps its own identifiers and field names inside its boundary and maps only approved information on the way out. A new @context version is a new approval, never a silent change to what gets sent.

### Does my data go to Scientix.ai or a central database?

No. You run the software, and each organization keeps its own records in its own broker. None of the projects depends on a Scientix.ai account or service, and the design has no central database that everyone feeds.

### Do the projects work with FIWARE?

Antares Core implements the NGSI-LD API, the same standard FIWARE context brokers use, and it can use shared data models such as Smart Data Models. The Antares projects are not official FIWARE components.

## Getting involved

### How can I contribute?

Issues and pull requests are welcome on [GitHub](https://github.com/antares-intelligence-org). Please use synthetic data in every example, test, and bug report, and never real personal or customer records. The [contributing guide](https://github.com/antares-intelligence-org/antares-intelligence/blob/main/CONTRIBUTING.md) covers the ground rules.

### How do I follow progress?

Watch the repositories in the [antares-intelligence-org](https://github.com/antares-intelligence-org) GitHub organization. Releases, comparison evidence, and status changes will appear there first.

### Can AI agents read this site?

Yes, and they're welcome to. The site publishes [llms.txt](https://antares-intelligence.org/llms.txt), a plain Markdown copy of every page, and a single [llms-full.txt](https://antares-intelligence.org/llms-full.txt) with the whole site in one file. The scenario boards on the homepage each have a full text transcript.

Have a question that isn't here? Open an issue on [GitHub](https://github.com/antares-intelligence-org/antares-intelligence/issues). This FAQ is also available as [plain Markdown](https://antares-intelligence.org/faq.md).
