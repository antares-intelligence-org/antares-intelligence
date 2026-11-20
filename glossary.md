<!-- Generated from https://antares-intelligence.org/glossary/ by build_agent_files.py. Edit the HTML, not this file. -->

# The words behind shared context

Plain-language definitions of the NGSI-LD terms you'll meet on this site and in the project repositories, plus the handful of words Antares uses in its own way. Terms marked Antares describe these projects; the rest come from the standard and its ecosystem.

### @context

The JSON-LD document that maps the short names in an NGSI-LD payload, such as `temperature`, to full, unambiguous URIs. Two organizations can use different words for the same thing and still mean the same thing, because the `@context` says what each word points to.

Versioning the `@context` is how organizations agree on a vocabulary. In the Antares scenarios, a new version is a new approval, never a silent change to what gets shared.

See also [JSON-LD](https://antares-intelligence.org/glossary/#json-ld), [Antares-Atrium](https://antares-intelligence.org/glossary/#antares-atrium).

### Antares-Atrium (Antares)

The governance layer of the Antares family. Atrium controls what each partner may share and receive, approves the vocabulary version in use, and lets subscribers replay what they missed. It's in design and has not been released.

Repository: [antares-intelligence-org/antares-atrium](https://github.com/antares-intelligence-org/antares-atrium).

### Antares-LD (Antares)

An open-source NGSI-LD context broker written in Rust. It runs as a single binary with no database server, keeps current state and history, and uses [Scorpio](https://antares-intelligence.org/glossary/#scorpio) as its behavioral reference. It's a working prototype with no release yet.

Repository: [antares-intelligence-org/antares-ld](https://github.com/antares-intelligence-org/antares-ld).

### Antares-Stinger (Antares)

The interface translator of the Antares family. Stinger translates approved data between source systems and NGSI-LD, so it can link an ERP, an existing IoT gateway, or a partner system, and it holds updates locally when the network goes down. It's in design and has not been released.

Repository: [antares-intelligence-org/antares-stinger](https://github.com/antares-intelligence-org/antares-stinger).

### Apache License 2.0

The permissive open-source license the Antares Intelligence projects use. You can use, change, and redistribute the code, including commercially. It doesn't grant the right to use the Antares Intelligence name or logo as your own brand.

### Context broker

A server that stores context information and serves it through the NGSI-LD API. Other systems ask it what's true now, look back through its history, or subscribe to be told when something changes. [Antares-LD](https://antares-intelligence.org/glossary/#antares-ld), [Scorpio](https://antares-intelligence.org/glossary/#scorpio), Orion-LD, and Stellio are context brokers.

### Context information

What is known about things in the world (a parking space, a pallet, a room, a sample), their properties, and how they relate to each other, both right now and over time.

### Context source

Any system that provides context information to a broker, either by sending updates or by registering with the broker so it can be asked on demand.

### Edge

The places where data is produced, close to devices, machines, and people. Networks at the edge are often slow or drop out, so software there has to hold data safely until it can be delivered.

### Entity

The basic unit of NGSI-LD: a thing with an identifier and a type, described by [properties](https://antares-intelligence.org/glossary/#property) and linked to other entities by [relationships](https://antares-intelligence.org/glossary/#relationship). A parking space, a shipment, and a hospital room can each be an entity.

### ETSI ISG CIM

The ETSI Industry Specification Group for cross-cutting Context Information Management. It publishes and maintains the NGSI-LD specifications, including the API specification, GS CIM 009.

### Federation

Brokers in different organizations answering requests together while each keeps its own data. Nobody hands their records to a central database. Each side shares only what it has approved, and in the Antares scenarios every exchange carries a [receipt](https://antares-intelligence.org/glossary/#receipt).

### FIWARE

An open-source ecosystem, stewarded by the FIWARE Foundation, whose components share context through the NGSI-LD API. Several context brokers, including Scorpio and Orion-LD, are FIWARE components. The Antares projects implement the same standard but are not official FIWARE components.

### GeoProperty

A special NGSI-LD property that holds a location as GeoJSON, so a broker can answer questions like "which entities are within 500 meters of this point."

### JSON-LD

A W3C standard for writing linked data in ordinary JSON. Every NGSI-LD payload is JSON-LD, which is what lets an [@context](https://antares-intelligence.org/glossary/#context) give each field a precise meaning.

### NGSI-LD

An open standard from ETSI for describing things, their relationships, and how they change over time. It defines an information model built on [entities](https://antares-intelligence.org/glossary/#entity), [properties](https://antares-intelligence.org/glossary/#property), and [relationships](https://antares-intelligence.org/glossary/#relationship), and an HTTP API for creating, querying, and subscribing to that information. Smart cities, agriculture, energy, manufacturing, and health all use it.

### Notification

The message a broker sends to a subscriber when context it [subscribed](https://antares-intelligence.org/glossary/#subscription) to changes.

### Property

A named value that describes an entity, such as a temperature reading or a status. A property can record when it was observed, which is what makes history possible.

### Provenance

The record of where a piece of information came from and what happened to it on the way. It's how someone later answers "what did we know, and when did we know it."

### Receipt (Antares)

In the Antares scenarios, the record that travels with shared information. Every receipt answers the same four questions: the source, what was observed or approved, who authorized it, and when. The signal and its receipt cross the boundary; the underlying record stays where it belongs.

### Relationship

A link from one NGSI-LD entity to another, such as a sample that belongs to a batch, or a sensor that sits in a room.

### Replay

Delivering the changes a downstream system missed while it was offline, in order and without duplicate effects, so every accepted change can be accounted for after it comes back.

### Scorpio

An open-source NGSI-LD context broker in the FIWARE ecosystem. It runs alongside a PostgreSQL database. [Antares-LD](https://antares-intelligence.org/glossary/#antares-ld) uses Scorpio as its behavioral reference and plans to publish a case-by-case comparison of where the two agree and differ.

### Smart Data Models

An open, collaborative library of shared data models for NGSI-LD and other formats, covering domains from cities and energy to agriculture and manufacturing. Using a shared model means two organizations describe the same kind of thing the same way.

### SQLite

An embedded database that lives in a single file. Antares-LD uses it as its working storage path, which is why the broker needs no separate database server.

### Subscription

A standing request to a broker to be [notified](https://antares-intelligence.org/glossary/#notification) when matching context changes. Subscriptions are how one system reacts to another without polling.

### Synthetic data

Made-up data that has the shape of real records but describes no real person or customer. Every Antares example, test, and demonstration uses it.

### Temporal API

The part of NGSI-LD that answers how an entity changed over a period of time, not just its current state. In Antares-LD, the SQLite store serves the temporal API.

Missing a term? Open an issue on [GitHub](https://github.com/antares-intelligence-org/antares-intelligence/issues). This glossary is also available as [plain Markdown](https://antares-intelligence.org/glossary.md).
