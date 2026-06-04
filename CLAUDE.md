# CLAUDE.md – DENKHUT-6

Regeln für Claude Code in **diesem** Repo. Verbindlich beim Arbeiten am bzw. mit dem Plugin.

## Was ist DENKHUT-6

Ein Claude-Code-Plugin, das Edward de Bonos *Six Thinking Hats* als Multiagentensystem umsetzt: sechs Hut-Subagents (`agents/`) plus Blauer-Hut-Orchestrator. Slash-Command als Plugin: `/denkhut-6:denkhut` (namespaced); bei lokaler Kopie ohne Plugin: `/denkhut`. Version 0.1.3, Lizenz MIT.

## Kernkonventionen

- **Subagents via Agent-Tool.** Jeder Hut ist ein echter Subagent mit isoliertem Kontext. Der Blaue Hut orchestriert ausschließlich über das Agent-Tool – er argumentiert nicht inhaltlich mit.
- **Ein Hut = ein Modus, strikt.** Kein Hut verlässt seinen Denkmodus. Weiß wertet nicht; Rot begründet nicht; Schwarz schlägt nicht vor; Gelb nennt keine Risiken; Grün bewertet nicht. Verstöße sind Fehler.
- **Minimaler Kontext.** Jeder Hut bekommt nur den relevanten Vor-Kontext (siehe `DATENMODELL.md` §Kontextflüsse). Gelb und Schwarz sehen die Ausgabe des jeweils anderen nicht; Rot sieht keine Pro/Contra.
- **Reihenfolge & Parallelität.** Weiß steht vor den faktenbasierten Hüten (Grün/Gelb/Schwarz); Rot (Bauchgefühl) ist faktenunabhängig und darf je nach Sequenz früher stehen (z. B. `bewertung`: Rot vor Weiß). Gelb und Schwarz laufen parallel. Blau steht immer zuerst und zuletzt.
- **Feldnamen exakt.** Output-Envelope und Entity-Felder folgen `DATENMODELL.md` / `schemas/` ohne Abweichung (z. B. `wissensluecke`, `eintrittswahrscheinlichkeit`, `gegenmassnahme_moeglich`).
- **Ausgabeordner.** Jede Sitzung nach `denkhut-sitzungen/<slug>/` mit einer Datei pro Schritt (`00-problem.md`, `10-weiss.md`, `20-gruen.md`, `30-gelb.md`, `40-schwarz.md`, `50-rot.md`, `90-synthese.md`) plus `protokoll.md`.
- **Protokollpflicht.** Jeder Schritt erzeugt einen Logeintrag (`schritt_nr`, `hut`, `zeit`, `input_referenz`, `output_referenz`).
- **Sequenzen.** Default `entscheidung`; weiter `bewertung`, `ideenfindung`, `schnell-review` (Reihenfolgen in `DATENMODELL.md`).

## Validierung (vor jedem Release)

- `python3 scripts/validate.py` – extrahiert alle JSON-Blöcke aus Markdown, validiert die Hut-Envelopes gegen `schemas/hut-output.schema.json`, prüft ID-Referenzen (`bezug_idee`/`basiert_auf` → existierende Ideen) und die Manifeste. Braucht `jsonschema` (`pip install jsonschema`).
- `claude plugin validate .claude-plugin/plugin.json` und `… marketplace.json` – Plugin-/Marketplace-Manifeste.
- **Strict-Entscheidung:** Diese `CLAUDE.md` am Repo-Root ist **bewusst** Contributor-Kontext, kein Plugin-User-Kontext. Die `--strict`-Warnung dazu ist akzeptiert; CI und Release-Check nutzen den Validator **ohne** `--strict`. Soll `--strict` grün sein, müsste der Inhalt in einen Skill wandern – derzeit nicht gewünscht.

## Verweise

- Methode/Theorie: `METHODIK.md`
- Datenstrukturen: `DATENMODELL.md`, Schemas in `schemas/`
- Bedienung: `HANDBUCH.md`
- Tool-neutrale Spec: `CONVENTIONS.md`
- Beispiel: `beispiel/4-tage-woche/`
