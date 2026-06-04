#!/usr/bin/env python3
"""
DENKHUT-6 Konsistenz-Check.

Prüft das gesamte Repo gegen die eigene Spezifikation:
  1. JSON-Syntax aller Manifeste und Schemas.
  2. Alle ```json```-Blöcke in Markdown, die ein Hut-Envelope sind
     (Feld "hut"), gegen schemas/hut-output.schema.json.
  3. Kanonische Blau-Form: hut == "blau" -> eintraege == [].
  4. ID-Referenzen: bezug_idee / basiert_auf verweisen auf existierende
     Ideen-IDs (I*) im selben Verzeichnis.

Voraussetzung: pip install jsonschema
Aufruf:        python3 scripts/validate.py
Exit-Code:     0 = alles grün, 1 = mindestens ein Problem.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("FEHLER: 'jsonschema' nicht installiert. -> pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
JSON_BLOCK = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)
errors: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)
    print(f"  ✘ {msg}")


def md_json_blocks(path: Path):
    for raw in JSON_BLOCK.findall(path.read_text(encoding="utf-8")):
        try:
            yield json.loads(raw), None
        except json.JSONDecodeError as e:
            yield None, str(e)


def main() -> int:
    # 1) Manifeste & Schemas: reine JSON-Syntax
    print("» Manifeste & Schemas")
    manifests = [
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        "schemas/hut-output.schema.json",
        "schemas/sitzung.schema.json",
    ]
    for rel in manifests:
        p = ROOT / rel
        try:
            json.loads(p.read_text(encoding="utf-8"))
            print(f"  ✔ {rel}")
        except Exception as e:  # noqa: BLE001
            err(f"{rel}: ungültiges JSON ({e})")

    # Schema laden
    env_schema = json.loads((ROOT / "schemas/hut-output.schema.json").read_text(encoding="utf-8"))
    Draft7Validator.check_schema(env_schema)
    validator = Draft7Validator(env_schema)

    # 2)+3) Envelopes je Markdown
    print("» Hut-Envelopes (Markdown ```json```)")
    envelope_count = 0
    # Ideen-IDs je Verzeichnis sammeln (für ID-Referenz-Check)
    ideas_by_dir: dict[Path, set[str]] = {}
    refs_by_dir: dict[Path, list[tuple[str, str, str]]] = {}

    for md in sorted(ROOT.rglob("*.md")):
        if "denkhut-sitzungen" in md.parts:
            continue
        for inst, jerr in md_json_blocks(md):
            if jerr:
                err(f"{md.relative_to(ROOT)}: JSON-Block nicht parsebar ({jerr})")
                continue
            if not isinstance(inst, dict) or "hut" not in inst:
                continue
            envelope_count += 1
            rel = md.relative_to(ROOT)
            for e in sorted(validator.iter_errors(inst), key=lambda e: list(e.path)):
                err(f"{rel}: {list(e.path)} -> {e.message}")
            if inst.get("hut") == "blau" and inst.get("eintraege") not in ([], None):
                err(f"{rel}: Blau-Envelope muss 'eintraege': [] haben (kanonische Form).")
            # IDs sammeln
            d = md.parent
            ideas = ideas_by_dir.setdefault(d, set())
            refs = refs_by_dir.setdefault(d, [])
            for it in inst.get("eintraege", []) or []:
                if not isinstance(it, dict):
                    continue
                iid = it.get("id", "")
                if isinstance(iid, str) and re.fullmatch(r"I[0-9]+", iid):
                    ideas.add(iid)
                if "bezug_idee" in it:
                    refs.append((str(rel), iid or "?", it["bezug_idee"]))
                for b in it.get("basiert_auf", []) or []:
                    refs.append((str(rel), iid or "?", b))

    print(f"  ✔ {envelope_count} Envelope(s) gegen hut-output.schema.json geprüft")

    # 4) ID-Referenzen
    print("» ID-Referenzen (bezug_idee / basiert_auf -> Idee)")
    ref_count = 0
    for d, refs in refs_by_dir.items():
        known = ideas_by_dir.get(d, set())
        for src, owner, target in refs:
            ref_count += 1
            if target not in known:
                err(f"{src}: Referenz '{target}' (von {owner}) zeigt auf keine bekannte Idee in {d.relative_to(ROOT)}/")
    print(f"  ✔ {ref_count} Referenz(en) geprüft")

    print()
    if errors:
        print(f"ERGEBNIS: {len(errors)} Problem(e). ✘")
        return 1
    print("ERGEBNIS: alles grün. ✔")
    return 0


if __name__ == "__main__":
    sys.exit(main())
