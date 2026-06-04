# Changelog

Alle nennenswerten Änderungen an DENKHUT-6 werden in dieser Datei dokumentiert.

Das Format orientiert sich an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/),
und das Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [0.1.0] – 2026-06-04 – Initiale Veröffentlichung

### Added

- Multiagentensystem nach De Bonos *Six Thinking Hats* als Claude-Code-Plugin.
- Sechs Hut-Subagents in `agents/`: `weisser-hut`, `roter-hut`, `schwarzer-hut`, `gelber-hut`, `gruener-hut`, `blauer-hut`.
- Blauer-Hut-Orchestrator, der die Hüte über das Agent-Tool steuert (isolierte Kontexte, parallele Hüte).
- Skills in `skills/`: `denkhut-6` (Orchestrator), `denkhut-sequenz`, `denkhut-protokoll`.
- Slash-Command `/denkhut-6` (`commands/denkhut.md`).
- Vier Sequenzen: `entscheidung` (Default), `bewertung`, `ideenfindung`, `schnell-review`.
- Datenmodell mit Output-Envelope und typisierten Einträgen (Fakt, Idee, Emotion, Nutzenpunkt, Risiko, Synthese, Logeintrag); JSON-Schemas in `schemas/`.
- Output-Vorlagen in `templates/` und Ausgabekonvention `denkhut-sitzungen/<slug>/`.
- Vollständige Beispielsitzung in `beispiel/4-tage-woche/`.
- Dokumentation: `README.md`, `METHODIK.md`, `DATENMODELL.md`, `HANDBUCH.md`, `CONVENTIONS.md`, `CLAUDE.md`.
- Plugin-Manifest, MIT-Lizenz und `.gitignore`.
- Marketplace-Manifest `.claude-plugin/marketplace.json` für die Ein-Befehl-Installation aus GitHub (`/plugin marketplace add afriedrich80/DENKHUT-6` → `/plugin install denkhut-6@denkhut-6`).

[0.1.0]: https://github.com/afriedrich80/DENKHUT-6/releases/tag/v0.1.0
