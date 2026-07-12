#!/usr/bin/env python3
"""
Computer Familiarity Ranking

Reads responses.csv (from the Welcome Questionnaire Google Form) and computes
a single familiarity score (0–100) per student based on a weighted points
rubric across programming, AI, technical background, and computer usage.

Rubric (theoretical max = 130 points, normalized to a 0–100 scale for display):

    Programming Knowledge (max 52)
        Knows any programming language?            Yes = 10
        Self-rated programming familiarity:
            Just starting out  =  3
            Beginner           =  5
            Advanced           = 15
            Super Advanced     = 20
        Languages known (2 pts each, capped at 10)
        Programs written:
            Only one =  2
            A few    =  5
            A lot    = 10
            A ton    = 12

    AI / LLM Familiarity (max 25)
        Used an LLM?           Yes = 5
        Number of LLMs used (2 pts each, capped at 10)
        Self-rated AI familiarity (1–10 scale, capped at 10)

    AI Usage Sophistication (max 5)
        Uses LLMs for programming?  Yes = 3
        Uses LLMs for planning?     Yes = 2
        Other LLM uses (1 pt each, capped with above at 5)

    AI Critical Evaluation (max 5)
        Review all AI output                 = 5
        Sometimes review output             = 3
        Only review unfamiliar output       = 1
        Rarely / never double check         = 0

    Technical Background (max 28)
        Took a computer class?           Yes = 10
        Hardware projects (Pi/Arduino)?  Yes = 10
        Math topics taken (2 pts each, capped at 8, but code cap of 10 for safety)

    Computer Usage (max 15)
        Uses computer for programming?  Yes = 8
        Number of activity types (capped at 7)

Questionnaire source: Welcome Questionnaire.pdf
"""

import argparse
import csv
import sys
from collections import OrderedDict
from typing import Optional


# ── Column names from the Google Form ──────────────────────────────────
# These must match the CSV header exactly.  Update if the form changes.
COL_NAME           = "Name (First + Last)"
COL_KNOWS_LANG     = "Do you know any programming languages?"
COL_FAMILIARITY    = "How familiar would you say you are with programming?"
COL_LANGUAGES      = "What programming languages do you know"
COL_PROGRAMS       = "How many programs have you written?"
COL_USED_LLM       = "Have you used a Large Language Model (LLM) or AI?"
COL_WHICH_LLM      = "Which LLMs have you used?"
COL_LLM_USES       = "What do you use LLMs for?"
COL_AI_FAMILIARITY = "How familiar are you with using AI tools?"
COL_AI_REVIEW      = "When you use AI how do you use it?"
COL_MATH_TOPICS    = "What math topic have you taken?"
COL_COMP_CLASS     = "Have you taken a computer class in school or at camp?"
COL_OS             = "If you have a computer at home, what operating system does it use?"
COL_HARDWARE       = "Have you done any hardware projects (Raspberry Pi / Arduino)"
COL_USAGE          = "What do you normally use a computer for?"

ALL_COLUMNS = [
    COL_NAME, COL_KNOWS_LANG, COL_FAMILIARITY, COL_LANGUAGES, COL_PROGRAMS,
    COL_USED_LLM, COL_WHICH_LLM, COL_LLM_USES, COL_AI_FAMILIARITY, COL_AI_REVIEW,
    COL_MATH_TOPICS, COL_COMP_CLASS, COL_OS, COL_HARDWARE, COL_USAGE,
]


def parse_list_field(value: str) -> list[str]:
    """Split a comma-separated field into a cleaned list."""
    if not value.strip():
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def score_row(row: dict) -> dict:
    """Return a dict with 'total', per-category breakdown, and any warnings."""

    warnings: list[str] = []
    missing: list[str] = []

    prog_knows       = 0   # knows a language
    prog_familiarity = 0   # self-rated level
    prog_lang_count  = 0   # languages known
    prog_written     = 0   # programs written
    ai_used          = 0   # used LLM
    ai_llm_count     = 0   # number of LLMs used
    ai_llm_uses      = 0   # sophistication of LLM usage
    ai_familiarity   = 0   # self-rated AI familiarity
    ai_review        = 0   # AI output review habits (critical evaluation)
    tech_class       = 0   # took computer class
    tech_hardware    = 0   # hardware projects
    tech_math        = 0   # math topics
    usage_prog       = 0   # uses computer for programming
    usage_breadth    = 0   # number of activities

    # ── Helper: detect blank / missing fields ──────────────────────
    def is_blank(key: str) -> bool:
        return row.get(key, "").strip() == ""

    # ── Programming Knowledge (max 47) ─────────────────────────────
    if is_blank(COL_KNOWS_LANG):
        missing.append(COL_KNOWS_LANG)
    elif row[COL_KNOWS_LANG].strip().lower() == "yes":
        prog_knows = 10

    # Self-rated familiarity — options from the actual questionnaire
    if is_blank(COL_FAMILIARITY):
        # Only flag if they said "Yes" to knowing languages (Q4→Q5 skip logic)
        if prog_knows:
            missing.append(COL_FAMILIARITY)
    else:
        fam = row[COL_FAMILIARITY].strip().lower()
        if fam == "just starting out":
            prog_familiarity = 3
        elif fam == "beginner":
            prog_familiarity = 5
        elif fam == "advanced":
            prog_familiarity = 15
        elif fam == "super advanced":
            prog_familiarity = 20
        else:
            warnings.append(f"Unrecognized familiarity value: '{row[COL_FAMILIARITY].strip()}'")

    # Languages known (2 pts each, capped at 10)
    languages = parse_list_field(row.get(COL_LANGUAGES, ""))
    prog_lang_count = min(len(languages) * 2, 10)

    # Cross-field checks
    if not prog_knows and languages:
        warnings.append("Said 'No' to knowing languages but listed: " + ", ".join(languages))
    if prog_knows and not languages:
        warnings.append("Said 'Yes' to knowing languages but listed none")

    # Programs written — options from the actual questionnaire
    if is_blank(COL_PROGRAMS):
        if prog_knows:
            missing.append(COL_PROGRAMS)
    else:
        progs = row[COL_PROGRAMS].strip().lower()
        if progs == "only one":
            prog_written = 2
        elif progs == "a few":
            prog_written = 5
        elif progs == "a lot":
            prog_written = 10
        elif progs == "a ton":
            prog_written = 12
        else:
            warnings.append(f"Unrecognized programs-written value: '{row[COL_PROGRAMS].strip()}'")

    # ── AI / LLM Familiarity (max 25) ─────────────────────────────
    if is_blank(COL_USED_LLM):
        missing.append(COL_USED_LLM)
    elif row[COL_USED_LLM].strip().lower() == "yes":
        ai_used = 5

    llms = parse_list_field(row.get(COL_WHICH_LLM, ""))
    ai_llm_count = min(len(llms) * 2, 10)

    # Cross-field checks
    if not ai_used and llms:
        warnings.append("Said 'No' to using LLMs but listed: " + ", ".join(llms))
    if ai_used and not llms:
        warnings.append("Said 'Yes' to using LLMs but listed no LLMs")

    # AI familiarity (1–10 scale)
    ai_raw = row.get(COL_AI_FAMILIARITY, "").strip()
    if ai_raw == "":
        if ai_used:
            missing.append(COL_AI_FAMILIARITY)
    else:
        try:
            ai_fam = int(ai_raw)
            ai_familiarity = min(max(ai_fam, 1), 10)  # clamp to 1–10 range
        except ValueError:
            warnings.append(f"Non-numeric AI familiarity: '{ai_raw}'")

    # ── AI Usage Sophistication (max 5) ────────────────────────────
    # What do they use LLMs for? Programming & planning are higher-signal.
    llm_uses = parse_list_field(row.get(COL_LLM_USES, ""))
    if llm_uses:
        for use in llm_uses:
            use_lower = use.lower()
            if "programming" in use_lower:
                ai_llm_uses += 3
            elif "planning" in use_lower:
                ai_llm_uses += 2
            else:
                ai_llm_uses += 1
        ai_llm_uses = min(ai_llm_uses, 5)

    # Cross-field check: claims to use LLMs for programming but no languages?
    has_prog_use = any("programming" in u.lower() for u in llm_uses)
    if has_prog_use and not prog_knows and not languages:
        warnings.append("Uses LLMs for programming but says they don't know any languages")

    # ── AI Critical Evaluation (max 5) ─────────────────────────────
    # How do they review AI output?
    ai_review_raw = row.get(COL_AI_REVIEW, "").strip()
    if ai_review_raw:
        review_lower = ai_review_raw.lower()
        if "review all" in review_lower:
            ai_review = 5
        elif "sometimes review" in review_lower:
            ai_review = 3
        elif "only review" in review_lower:
            ai_review = 1
        # "rarely double check" / "always use what it outputs" → 0 (default)

    # ── Technical Background (max 30) ─────────────────────────────
    if is_blank(COL_COMP_CLASS):
        missing.append(COL_COMP_CLASS)
    elif row[COL_COMP_CLASS].strip().lower() == "yes":
        tech_class = 10

    if is_blank(COL_HARDWARE):
        missing.append(COL_HARDWARE)
    elif row[COL_HARDWARE].strip().lower() == "yes":
        tech_hardware = 10

    math_topics = parse_list_field(row.get(COL_MATH_TOPICS, ""))
    tech_math = min(len(math_topics) * 2, 10)

    # ── Computer Usage (max 15) ───────────────────────────────────
    activities = parse_list_field(row.get(COL_USAGE, ""))
    if any("programming" in a.lower() for a in activities):
        usage_prog = 8
        # Cross-field check: claims programming usage but doesn't know languages
        if not prog_knows and not languages:
            warnings.append("Checked 'Programming' as computer activity but says they don't know any languages")

    usage_breadth = min(len(activities), 7)

    # ── Computer Access (warnings only, no points) ────────────────
    os_raw = row.get(COL_OS, "").strip()
    if os_raw:
        os_lower = os_raw.lower()
        if "no computer" in os_lower:
            warnings.append("Reports no computer at home — potential access/equity concern")
        if "not sure" in os_lower:
            warnings.append("Unsure about home computer OS — possible limited access")

    raw_total = (
        prog_knows + prog_familiarity + prog_lang_count + prog_written
        + ai_used + ai_llm_count + ai_llm_uses + ai_familiarity + ai_review
        + tech_class + tech_hardware + tech_math
        + usage_prog + usage_breadth
    )

    return {
        "total": raw_total,
        "prog_knows_lang": prog_knows,
        "prog_familiarity": prog_familiarity,
        "prog_lang_count": prog_lang_count,
        "prog_programs_written": prog_written,
        "ai_used_llm": ai_used,
        "ai_llm_count": ai_llm_count,
        "ai_llm_uses": ai_llm_uses,
        "ai_familiarity": ai_familiarity,
        "ai_critical_eval": ai_review,
        "tech_class": tech_class,
        "tech_hardware": tech_hardware,
        "tech_math": tech_math,
        "usage_programming": usage_prog,
        "usage_breadth": usage_breadth,
        "_warnings": warnings,
        "_missing": missing,
    }


def validate_columns(reader: csv.DictReader) -> None:
    """Check that all expected columns are present in the CSV."""
    available = set(reader.fieldnames or [])
    for col in ALL_COLUMNS:
        if col not in available:
            print(f"WARNING: Expected column not found in CSV: '{col}'", file=sys.stderr)


def main(input_path: str, output_path: str):
    # ── Read ───────────────────────────────────────────────────────
    try:
        with open(input_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            validate_columns(reader)
            rows = list(reader)
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if not rows:
        print("ERROR: No data rows found in input file.", file=sys.stderr)
        sys.exit(1)

    # ── Score ──────────────────────────────────────────────────────
    results = []
    all_warnings: dict[str, list[str]] = {}
    all_missing: dict[str, list[str]] = {}

    for row in rows:
        name = row.get(COL_NAME, "Unknown").strip()
        breakdown = score_row(row)
        # Pull warnings/missing out to display, but keep them separate from score
        w = breakdown.pop("_warnings", [])
        m = breakdown.pop("_missing", [])
        if w:
            all_warnings[name] = w
        if m:
            all_missing[name] = m
        results.append((name, breakdown))

    # ── Sort & Print ───────────────────────────────────────────────
    results.sort(key=lambda x: x[1]["total"], reverse=True)

    MAX_THEORETICAL = 130  # sum of all category maxima (see docstring)

    print(f"{'Rank':<6}{'Name':<25}{'Raw':>6}  {'Scored/130':>10}")
    print("-" * 52)
    for rank, (name, breakdown) in enumerate(results, start=1):
        raw = breakdown["total"]
        print(f"{rank:<6}{name:<25}{raw:>6}  {raw / MAX_THEORETICAL * 100:>9.1f}%")

    # ── Summary ────────────────────────────────────────────────────
    scores = [b["total"] for _, b in results]
    print(f"\n{'─' * 40}")
    print(f"Students:           {len(scores)}")
    print(f"Max theoretical:    {MAX_THEORETICAL} (≈100% scale)")
    print(f"Highest raw:        {max(scores)}")
    print(f"Lowest raw:         {min(scores)}")
    print(f"Average raw:        {sum(scores) / len(scores):.1f}")

    # ── Warnings ───────────────────────────────────────────────────
    if all_warnings:
        print(f"\n{'─' * 40}")
        print("⚠  Consistency Warnings:")
        for name, warns in all_warnings.items():
            for w in warns:
                print(f"   [{name}] {w}")

    if all_missing:
        print(f"\n{'─' * 40}")
        print("⚠  Missing / Skipped Fields:")
        for name, fields in all_missing.items():
            unique = sorted(set(fields))
            print(f"   [{name}] {', '.join(unique)}")

    # ── Write CSV ──────────────────────────────────────────────────
    fieldnames = [
        "Rank", "Name", "Raw", "Pct",
        "prog_knows_lang", "prog_familiarity", "prog_lang_count", "prog_programs_written",
        "ai_used_llm", "ai_llm_count", "ai_llm_uses", "ai_familiarity", "ai_critical_eval",
        "tech_class", "tech_hardware", "tech_math",
        "usage_programming", "usage_breadth",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank, (name, breakdown) in enumerate(results, start=1):
            total = breakdown["total"]    # read, DON'T pop — was destructive before
            row_out = {
                "Rank": rank,
                "Name": name,
                "Raw": total,
                "Pct": f"{total / MAX_THEORETICAL * 100:.1f}",
            }
            row_out.update({k: v for k, v in breakdown.items() if k != "total"})
            writer.writerow(row_out)

    print(f"\nSaved breakdown to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rank student computer familiarity from survey responses."
    )
    parser.add_argument(
        "-i", "--input",
        default="responses.csv",
        help="Input CSV path (default: responses.csv)",
    )
    parser.add_argument(
        "-o", "--output",
        default="familiarity_scores.csv",
        help="Output CSV path (default: familiarity_scores.csv)",
    )
    args = parser.parse_args()
    main(args.input, args.output)
