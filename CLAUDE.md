# CLAUDE.md – DENKHUT-6

Regeln für Claude Code in **diesem** Repo. Verbindlich beim Arbeiten am bzw. mit dem Plugin.

## Was ist DENKHUT-6

Ein Claude-Code-Plugin, das Edward de Bonos *Six Thinking Hats* als Multiagentensystem umsetzt: sechs Hut-Subagents (`agents/`) plus Blauer-Hut-Orchestrator. Slash-Command: `/denkhut-6`. Version 0.1.0, Lizenz MIT.

## Kernkonventionen

- **Subagents via Agent-Tool.** Jeder Hut ist ein echter Subagent mit isoliertem Kontext. Der Blaue Hut orchestriert ausschließlich über das Agent-Tool – er argumentiert nicht inhaltlich mit.
- **Ein Hut = ein Modus, strikt.** Kein Hut verlässt seinen Denkmodus. Weiß wertet nicht; Rot begründet nicht; Schwarz schlägt nicht vor; Gelb nennt keine Risiken; Grün bewertet nicht. Verstöße sind Fehler.
- **Minimaler Kontext.** Jeder Hut bekommt nur den relevanten Vor-Kontext (siehe `DATENMODELL.md` §Kontextflüsse). Gelb und Schwarz sehen die Ausgabe des jeweils anderen nicht; Rot sieht keine Pro/Contra.
- **Parallelität.** Gelb und Schwarz laufen parallel. Blau steht immer zuerst und zuletzt. Weiß vor Grün/Gelb/Schwarz/Rot.
- **Feldnamen exakt.** Output-Envelope und Entity-Felder folgen `DATENMODELL.md` / `schemas/` ohne Abweichung (z. B. `wissensluecke`, `eintrittswahrscheinlichkeit`, `gegenmassnahme_moeglich`).
- **Ausgabeordner.** Jede Sitzung nach `denkhut-sitzungen/<slug>/` mit einer Datei pro Schritt (`00-problem.md`, `10-weiss.md`, `20-gruen.md`, `30-gelb.md`, `40-schwarz.md`, `50-rot.md`, `90-synthese.md`) plus `protokoll.md`.
- **Protokollpflicht.** Jeder Schritt erzeugt einen Logeintrag (`schritt_nr`, `hut`, `zeit`, `input_referenz`, `output_referenz`).
- **Sequenzen.** Default `entscheidung`; weiter `bewertung`, `ideenfindung`, `schnell-review` (Reihenfolgen in `DATENMODELL.md`).

## Verweise

- Methode/Theorie: `METHODIK.md`
- Datenstrukturen: `DATENMODELL.md`, Schemas in `schemas/`
- Bedienung: `HANDBUCH.md`
- Tool-neutrale Spec: `CONVENTIONS.md`
- Beispiel: `beispiel/4-tage-woche/`
