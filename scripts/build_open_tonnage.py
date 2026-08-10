#!/usr/bin/env python3
"""Convert the published Google Sheet (TSV) into open-tonnage.json.

Column headers are matched by name, not position, so reordering or adding
columns in the sheet will not break the site. If the sheet is unreachable or
malformed the script exits non-zero WITHOUT touching the existing JSON, so the
website keeps serving the last good data.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

SHEET_URL = os.environ["SHEET_URL"]
OUT_PATH = "open-tonnage.json"
MAX_ROWS = 30
MAX_FIELD = 400

ALIASES = {
    "vessel":      ["vessel", "vesselname", "name", "ship", "shipname"],
    "openPort":    ["openport", "port", "openarea", "position"],
    "openDate":    ["opendate", "date", "open", "eta", "laycan"],
    "lastCargoes": ["lastcargoes", "lastcargo", "cargoes", "cargo", "lastcargos"],
    "note":        ["note", "notes", "remark", "remarks", "comment"],
    "status":      ["status", "state"],
    "updated":     ["updated", "updatedat", "lastupdated", "updateddate"],
}


def normalise(header):
    return re.sub(r"[^a-z0-9]", "", str(header or "").lower())


def clean(value):
    out = str(value or "").strip()
    if len(out) > 1 and out[0] == '"' and out[-1] == '"':
        out = out[1:-1].replace('""', '"')
    return out[:MAX_FIELD]


def main():
    req = urllib.request.Request(SHEET_URL, headers={"User-Agent": "hdmaritime-sync/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        text = resp.read().decode("utf-8-sig")

    lines = [l for l in re.split(r"\r\n|\n|\r", text) if l.strip()]
    if len(lines) < 2:
        sys.exit("Sheet has no data rows - keeping previous JSON.")

    headers = [normalise(h) for h in lines[0].split("\t")]
    col = {}
    for field, names in ALIASES.items():
        for i, h in enumerate(headers):
            if h in names:
                col[field] = i
                break

    if "vessel" not in col or "openPort" not in col:
        sys.exit('Sheet is missing a "vessel" or "open_port" column - keeping previous JSON.')

    rows = []
    for line in lines[1:]:
        if len(rows) >= MAX_ROWS:
            break
        cells = line.split("\t")
        row = {}
        for field, idx in col.items():
            row[field] = clean(cells[idx]) if idx < len(cells) else ""
        if row.get("vessel"):
            rows.append(row)

    if not rows:
        sys.exit("No valid vessel rows found - keeping previous JSON.")

    payload = {
        "schema": 1,
        "syncedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "rows": rows,
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Wrote %s with %d vessel(s)." % (OUT_PATH, len(rows)))


if __name__ == "__main__":
    main()
