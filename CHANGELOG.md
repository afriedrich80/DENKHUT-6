# Changelog

Alle nennenswerten Änderungen an DENKHUT-6 werden in dieser Datei dokumentiert.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
und das Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [0.1.2] – 2026-06-04 – Spezifikations-Konsistenz

### Changed

- **Blau-Synthese hat jetzt EINE kanonische Form:** Die Synthese steht im Top-Level-Feld `synthese`, `eintraege` bleibt leer (`[]`). Zuvor war es uneinheitlich (ein Beispiel nutzte `eintraege[0]`, eins das Feld `synthese`). `Synthese` ist daher nicht mehr Teil des `eintraege`-`oneOf` in `hut-output.schema.json`; Schema, Blau-Agent und beide Beispiele sind angeglichen.

### Fixed

- **Changelog-Korrektur:** Der 0.1.1-Eintrag behauptete fälschlich, `--strict` sei grün – tatsächlich behandelt `--strict` die `CLAUDE.md`-Root-Warnung als Fehler. Formulierung berichtigt.
- **`phase_nr`-Untergrenze** in `DATENMODELL.md` von `≥ 0` auf `≥ 1` korrigiert (Schema und Beispiele sind 1-basiert).
- **Command-Nachlauf beseitigt:** Beispiel im Orchestrator-Skill nutzt jetzt `/denkhut-6:denkhut`; Verweis im Blau-Agent auf den Skill als **denkhut-6** (statt `/denkhut-6`) entschärft die Verwechslung mit dem alten Slash-Command.
- **DATENMODELL/Schema-Unschärfe bei Blau behoben:** Doku beschreibt nun exakt `problem`+`sequenz` (Eröffnung) bzw. `synthese` (Abschluss) bei leerem `eintraege`.

## [0.1.1] – 2026-06-04 – Korrekturen & Klarstellungen

### Fixed

- **YAML-Frontmatter aller sechs Hut-Subagents repariert.** Unquotete `description:`-Werte mit `Trigger: "…"` brachen die YAML-Parse; die Agenten luden zur Laufzeit mit leeren Metadaten. Beschreibungen jetzt korrekt in Quotes (`claude plugin validate` meldet keine Agent-Fehler mehr; unter `--strict` bleibt nur die bewusst tolerierte `CLAUDE.md`-Root-Warnung).
- **ID-Konvention in den Agent-Mini-Beispielen** von `G1/G2/G3` auf schema-konforme `I1/I2/I3` (`^I[0-9]+$`) korrigiert (Grün, Gelb, Schwarz, Blau).
- **Schema deckt den Blauen Hut jetzt ab:** `hut-output.schema.json` erhält optionale Felder `problem`+`sequenz` (Eröffnung) und `synthese` (Abschluss) sowie ein `Problem`-`$def`; die Beispiel-JSONs validieren damit gegen das Envelope-Schema.
- **`iteration_begruendung`** (aus `templates/entscheidungsvorlage.md`) ins Synthese-Schema aufgenommen (beide Schemas).
- **Command-Notation vereinheitlicht:** als Plugin `/denkhut-6:denkhut` (namespaced), lokal ohne Plugin `/denkhut` – in README, HANDBUCH, CLAUDE.md korrigiert.
- **Sequenzregel präzisiert:** Weiß steht vor den faktenbasierten Hüten (Grün/Gelb/Schwarz); Rot darf je nach Sequenz früher stehen (z. B. `bewertung`). Vorher widersprüchlich formuliert.

### Added

- README-Abschnitt „Wofür eignet sich DENKHUT-6?" – stellt klar, dass die Methode auch für **Ideen- und Produktentwicklung** geeignet ist (nicht nur Probleme), mit Use-Case-/Sequenz-Zuordnung.
- Zweites durchgespieltes Beispiel `beispiel/software-produktidee/` (SaaS-Produktidee, Sequenz `ideenfindung`, Grün früh/breit, Rot vor Gelb/Schwarz).

## [0.1.0] – 2026-06-04 – Initiale Veröffentlichung

### Added

- Multiagentensystem nach De Bonos *Six Thinking Hats* als Claude-Code-Plugin.
- Sechs Hut-Subagents in `agents/`: `weisser-hut`, `roter-hut`, `schwarzer-hut`, `gelber-hut`, `gruener-hut`, `blauer-hut`.
- Blauer-Hut-Orchestrator, der die Hüte über das Agent-Tool steuert (isolierte Kontexte, parallele Hüte).
- Skills in `skills/`: `denkhut-6` (Orchestrator), `denkhut-sequenz`, `denkhut-protokoll`.
- Slash-Command `/denkhut-6:denkhut` (`commands/denkhut.md`).
- Vier Sequenzen: `entscheidung` (Default), `bewertung`, `ideenfindung`, `schnell-review`.
- Datenmodell mit Output-Envelope und typisierten Einträgen (Fakt, Idee, Emotion, Nutzenpunkt, Risiko, Synthese, Logeintrag); JSON-Schemas in `schemas/`.
- Output-Vorlagen in `templates/` und Ausgabekonvention `denkhut-sitzungen/<slug>/`.
- Vollständige Beispielsitzung in `beispiel/4-tage-woche/`.
- Dokumentation: `README.md`, `METHODIK.md`, `DATENMODELL.md`, `HANDBUCH.md`, `CONVENTIONS.md`, `CLAUDE.md`.
- Plugin-Manifest, MIT-Lizenz und `.gitignore`.
- Marketplace-Manifest `.claude-plugin/marketplace.json` für die Ein-Befehl-Installation aus GitHub (`/plugin marketplace add afriedrich80/DENKHUT-6` → `/plugin install denkhut-6@denkhut-6`).

[0.1.2]: https://github.com/afriedrich80/DENKHUT-6/releases/tag/v0.1.2
[0.1.1]: https://github.com/afriedrich80/DENKHUT-6/releases/tag/v0.1.1
[0.1.0]: https://github.com/afriedrich80/DENKHUT-6/releases/tag/v0.1.0
