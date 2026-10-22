#!/usr/bin/env python3
"""Mechanical checks for RU -> EN post translations.

Layer 1 of the translation check: cheap, reproducible signals of Russian
calques and stock AI phrasing, plus a glossary key checked against the
original. It does not judge meaning; completeness and fluency need a reader.

Usage: check_translation.py [EN_FILE ...]
Without arguments checks every content/**/index.md that has an index.ru.md.
Exits 1 if any file breaks a threshold.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = Path(__file__).resolve().parent / "translation-glossary.tsv"

# Thresholds are calibrated by hand on the fiat series; English essays by
# native authors sit well below them. Russian uses the dash as a copula and
# "не X, а Y" as everyday rhetoric, so both leak into translations.
MAX_DASHES_PER_100_WORDS = 0.5
MAX_NOT_BUT_PER_1000_WORDS = 1.5

# Stock phrasing that marks machine-written English. "leverage" is left out
# on purpose: in finance texts it is a term, not filler.
CLICHES = [
    r"delve", r"tapestry", r"testament to", r"it'?s worth noting",
    r"it is important to note", r"in today'?s", r"navigat(?:e|ing) the",
    r"landscape", r"realm", r"crucial", r"pivotal", r"seamless(?:ly)?",
    r"robust", r"underscore[sd]?", r"showcas(?:e|es|ing)", r"foster(?:s|ing)?",
    r"multifaceted", r"intricate", r"game[- ]changer", r"unlock(?:s|ing)?",
    r"embark", r"vibrant", r"furthermore", r"moreover", r"in conclusion",
    r"at its core", r"in essence", r"let'?s dive", r"here'?s the thing",
    r"the bottom line", r"plays? a (?:key|vital|crucial) role", r"a myriad",
    r"ever-evolving", r"stands as", r"serves as a",
]
CLICHE_RE = re.compile(r"\b(?:" + "|".join(CLICHES) + r")\b", re.IGNORECASE)

DASH_RE = re.compile(r"—|\s–\s|\s--\s")
NOT_BUT_RE = re.compile(r"\bnot\b[^.!?\n]{1,60}?(?:\bbut\b|—)", re.IGNORECASE)
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]*")


def prose(text):
    """Return prose lines as (line_no, text), without front matter and code.

    Double-quoted spans are blanked: they hold titles and quotations, which
    are not the translator's wording.
    """
    lines = text.splitlines()
    out = []
    in_front = lines[:1] == ["---"]
    in_code = False
    for no, line in enumerate(lines, 1):
        if in_front:
            if no > 1 and line == "---":
                in_front = False
            continue
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        line = re.sub(r"`[^`]*`", " ", line)
        line = re.sub(r"\]\([^)]*\)", "]", line)
        line = re.sub(r"[\"“][^\"”]*[\"”]", " ", line)
        out.append((no, line))
    return out


def word_count(lines):
    return sum(len(WORD_RE.findall(t)) for _, t in lines)


def load_glossary(path=GLOSSARY):
    """Rows of (ru_regex, en_regex). Lines starting with # are comments."""
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        ru, en = raw.split("\t")
        rows.append((re.compile(ru, re.IGNORECASE), re.compile(en, re.IGNORECASE)))
    return rows


def missing_terms(ru_text, en_text, glossary):
    """Glossary entries present in the original but absent in the translation."""
    return [en.pattern for ru, en in glossary
            if ru.search(ru_text) and not en.search(en_text)]


def check(en_path, ru_path, glossary):
    """Return (report_lines, ok) for one translation."""
    en_text = en_path.read_text(encoding="utf-8")
    lines = prose(en_text)
    words = max(word_count(lines), 1)
    dashes = sum(len(DASH_RE.findall(t)) for _, t in lines)
    not_but = [(no, m.group(0)) for no, t in lines for m in NOT_BUT_RE.finditer(t)]
    cliches = [(no, m.group(0)) for no, t in lines for m in CLICHE_RE.finditer(t)]

    dash_rate = dashes * 100 / words
    not_but_rate = len(not_but) * 1000 / words
    report = [f"{en_path.relative_to(ROOT)}  ({words} words)"]
    ok = True

    def metric(name, value, limit, unit):
        nonlocal ok
        bad = value > limit
        ok &= not bad
        report.append(f"  {'FAIL' if bad else 'ok  '} {name}: {value:.2f} {unit} (max {limit})")

    metric("dashes", dash_rate, MAX_DASHES_PER_100_WORDS, "per 100 words")
    metric("not X but Y", not_but_rate, MAX_NOT_BUT_PER_1000_WORDS, "per 1000 words")
    for no, frag in not_but:
        report.append(f"       {no}: {frag}")

    report.append(f"  {'FAIL' if cliches else 'ok  '} cliches: {len(cliches)}")
    ok &= not cliches
    for no, frag in cliches:
        report.append(f"       {no}: {frag}")

    if ru_path.exists():
        gaps = missing_terms(ru_path.read_text(encoding="utf-8"), en_text, glossary)
        report.append(f"  {'FAIL' if gaps else 'ok  '} glossary: {len(gaps)} missing")
        ok &= not gaps
        for term in gaps:
            report.append(f"       expected /{term}/")
    else:
        report.append("  skip glossary: no index.ru.md")
    return report, ok


def main(argv):
    if argv:
        targets = [Path(a).resolve() for a in argv]
    else:
        targets = sorted(p for p in (ROOT / "content").rglob("index.md")
                         if p.with_name("index.ru.md").exists())
    glossary = load_glossary()
    all_ok = True
    for en_path in targets:
        report, ok = check(en_path, en_path.with_name("index.ru.md"), glossary)
        print("\n".join(report), end="\n\n")
        all_ok &= ok
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
