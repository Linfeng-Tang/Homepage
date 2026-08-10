#!/usr/bin/env python3
"""Fetch the public Scholar profile and write the website's small data snapshot."""

import json
import re
from datetime import UTC, datetime
from pathlib import Path
from urllib.request import Request, urlopen


PROFILE_URL = "https://scholar.google.com/citations?user=PyRqpAsAAAAJ&hl=en"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "assets" / "data" / "scholar.json"


def main() -> None:
    request = Request(PROFILE_URL, headers={"User-Agent": "Mozilla/5.0 (compatible; academic-homepage-updater/1.0)"})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")

    values = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', html)
    if len(values) < 3:
        raise RuntimeError("Could not find Google Scholar profile metrics")

    payload = {
        "citations": int(values[0].replace(",", "")),
        "hindex": int(values[2].replace(",", "")),
        "i10index": int(values[4].replace(",", "")) if len(values) >= 5 else 0,
        "updated": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    }
    content = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if OUTPUT_FILE.exists() and OUTPUT_FILE.read_text(encoding="utf-8") == content:
        print("Scholar data is unchanged.")
        return
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"Updated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
