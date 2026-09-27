#!/usr/bin/env python3
"""Take one daily snapshot of a public Google Scholar author profile."""

from __future__ import annotations

import json
import re
import csv
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
PROFILE_URL = "https://scholar.google.com/citations?user=PyRqpAsAAAAJ&hl=en&pagesize=100"
OUTPUT_FILE = ROOT / "assets" / "data" / "scholar.json"
HISTORY_FILE = ROOT / "assets" / "data" / "scholar-history.json"
SUMMARY_FILE = ROOT / "assets" / "data" / "scholar-daily.csv"
REPORT_FILE = ROOT / "assets" / "data" / "scholar-latest.md"
CHINA_TIME = timezone(timedelta(hours=8))


def parse_profile(source: str) -> tuple[dict[str, int], dict[str, dict]]:
    if "captcha" in source.lower() or "not a robot" in source.lower():
        raise ValueError("Google Scholar requested human verification")
    values = re.findall(r'class="gsc_rsb_std"[^>]*>\s*([\d,]+)', source)
    if len(values) < 5:
        raise ValueError("Google Scholar profile metrics are missing")
    metrics = {
        "citations": int(values[0].replace(",", "")),
        "hindex": int(values[2].replace(",", "")),
        "i10index": int(values[4].replace(",", "")),
    }
    papers = {}
    rows = re.findall(r'<tr\b[^>]*class="[^"]*\bgsc_a_tr\b[^"]*"[^>]*>(.*?)</tr>', source, re.S)
    for row in rows:
        title_match = re.search(r'<a\b([^>]*class="[^"]*\bgsc_a_at\b[^"]*"[^>]*)>(.*?)</a>', row, re.S)
        if not title_match:
            continue
        href_match = re.search(r'href="([^"]+)"', title_match.group(1))
        if not href_match:
            continue
        paper_id = parse_qs(urlparse(unescape(href_match.group(1))).query).get("citation_for_view", [None])[0]
        if not paper_id:
            continue
        title = unescape(re.sub(r'<[^>]+>', '', title_match.group(2))).strip()
        count_match = re.search(r'<a\b[^>]*class="[^"]*\bgsc_a_ac\b[^"]*"[^>]*>(.*?)</a>', row, re.S)
        count_text = re.sub(r'<[^>]+>', '', count_match.group(1)).strip() if count_match else ''
        if not title or (count_text and not re.fullmatch(r'[\d,]+', count_text)):
            continue
        papers[paper_id] = {"title": title, "citations": int(count_text.replace(',', '')) if count_text else 0}
    if not papers:
        raise ValueError("Google Scholar publication list is missing")
    return metrics, papers


def read_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_reports(days: list[dict], entry: dict) -> None:
    with SUMMARY_FILE.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["日期(北京时间)", "总引用", "相较上次记录变化", "H指数", "i10指数", "变化论文数"])
        for day in days:
            writer.writerow([day["date"], day["citations"], day["change"], day["hindex"],
                             day["i10index"], len(day["paper_changes"])])
    change_label = "首次记录" if entry["change"] is None else f"{entry['change']:+d}"
    lines = [f"# Google Scholar 引用日报：{entry['date']}", "",
             f"- 总引用：{entry['citations']:,}（相较上次成功记录：{change_label}）",
             f"- H 指数：{entry['hindex']}；i10 指数：{entry['i10index']}",
             f"- 引用数变化的论文：{len(entry['paper_changes'])} 篇", ""]
    if entry["paper_changes"]:
        lines.extend(["| 论文 | 上次 | 本次 | 变化 |", "|---|---:|---:|---:|"])
        for paper in entry["paper_changes"]:
            title = paper["title"].replace("|", "\\|")
            lines.append(f"| {title} | {paper['previous']} | {paper['current']} | {paper['change']:+d} |")
    else:
        lines.append("与上次成功记录相比，已读取论文的引用数没有变化。")
    lines.extend(["", "数据来自 Google Scholar 公开作者主页；记录日期是获取日期，不代表引用论文实际发表日期。", ""])
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def save_snapshot(metrics: dict, papers: dict, now: datetime) -> None:
    today = now.astimezone(CHINA_TIME).date().isoformat()
    history = read_json(HISTORY_FILE, {"profile": PROFILE_URL, "days": []})
    days = history["days"]
    previous = next((item for item in reversed(days) if item["date"] < today), None)
    previous_papers = previous.get("papers", {}) if previous else {}
    changes = [
        {"id": paper_id, "title": paper["title"], "previous": previous_papers[paper_id]["citations"],
         "current": paper["citations"], "change": paper["citations"] - previous_papers[paper_id]["citations"]}
        for paper_id, paper in papers.items()
        if paper_id in previous_papers and paper["citations"] != previous_papers[paper_id]["citations"]
    ]
    changes.sort(key=lambda item: (-item["change"], item["title"]))
    entry = {
        "date": today, "citations": metrics["citations"],
        "change": metrics["citations"] - previous["citations"] if previous else None,
        "hindex": metrics["hindex"], "i10index": metrics["i10index"],
        "papers": papers, "paper_changes": changes,
    }
    history["days"] = [item for item in days if item["date"] != today] + [entry]
    history["days"].sort(key=lambda item: item["date"])
    write_json(HISTORY_FILE, history)
    write_json(OUTPUT_FILE, {**metrics, "updated": now.replace(microsecond=0).isoformat().replace("+00:00", "Z")})
    write_reports(history["days"], entry)
    print(f"{today}: {metrics['citations']} citations; change {entry['change']}; {len(changes)} papers changed")


def main() -> None:
    request = Request(PROFILE_URL, headers={"User-Agent": "Mozilla/5.0 (compatible; academic-homepage-updater/1.0)"})
    try:
        with urlopen(request, timeout=30) as response:
            source = response.read().decode("utf-8", errors="replace")
        metrics, papers = parse_profile(source)
    except (OSError, ValueError) as error:
        print(f"Scholar unavailable; previous data preserved: {error}")
        return
    save_snapshot(metrics, papers, datetime.now(timezone.utc))


if __name__ == "__main__":
    main()
