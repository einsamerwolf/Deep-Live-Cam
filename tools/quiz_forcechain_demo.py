#!/usr/bin/env python3
"""Kleiner CLI-Tester für Quiz-Force-Ketten (Q001 -> Q001a -> Q001b)."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Question:
    question_id: str
    prompt: str
    options: list[str]
    correct_index: int
    alt_question_id: str


def load_questions(csv_path: Path) -> list[Question]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    required = {
        "question_id",
        "prompt",
        "option_a",
        "option_b",
        "option_c",
        "correct_option",
        "alt_question_id",
    }
    missing = required - set(reader.fieldnames or [])
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise ValueError(f"CSV-Header unvollständig, fehlt: {missing_text}")

    questions: list[Question] = []
    for row in rows:
        correct_letter = (row["correct_option"] or "").strip().upper()
        correct_index = ["A", "B", "C"].index(correct_letter)
        questions.append(
            Question(
                question_id=row["question_id"].strip(),
                prompt=row["prompt"].strip(),
                options=[row["option_a"].strip(), row["option_b"].strip(), row["option_c"].strip()],
                correct_index=correct_index,
                alt_question_id=(row["alt_question_id"] or "").strip(),
            )
        )
    return questions


def run_quiz(questions: list[Question], answers: list[int], start_id: str | None) -> None:
    by_id = {q.question_id: q for q in questions}
    order = [q.question_id for q in questions]
    primary_order = [qid for qid in order if is_primary(qid)]

    current_id = start_id or primary_order[0]
    answer_pos = 0

    print("Start Quiz-Test")
    while current_id:
        question = by_id[current_id]
        print(f"\n[{question.question_id}] {question.prompt}")
        print(f"  A) {question.options[0]}")
        print(f"  B) {question.options[1]}")
        print(f"  C) {question.options[2]}")

        if answer_pos < len(answers):
            choice = answers[answer_pos]
            answer_pos += 1
            print(f"  -> Simulierte Antwort: {['A', 'B', 'C'][choice]}")
        else:
            try:
                raw = input("  Deine Antwort (A/B/C, Enter=Ende): ").strip().upper()
            except EOFError:
                print("Quiz beendet (keine weiteren Eingaben).")
                return
            if not raw:
                print("Quiz beendet.")
                return
            choice = ["A", "B", "C"].index(raw)

        if choice == question.correct_index:
            print("  Ergebnis: richtig")
            next_id = next_primary(primary_order, root_id(current_id))
        else:
            print("  Ergebnis: falsch")
            if question.alt_question_id:
                next_id = question.alt_question_id
                print(f"  Force-Kette aktiv -> nächste Frage: {question.alt_question_id}")
            else:
                next_id = next_primary(primary_order, root_id(current_id))

        current_id = next_id

    print("\nQuiz komplett durchlaufen.")


def is_primary(question_id: str) -> bool:
    return question_id and question_id[-1].isdigit()


def root_id(question_id: str) -> str:
    index = len(question_id)
    while index > 0 and question_id[index - 1].isalpha():
        index -= 1
    return question_id[:index]


def next_primary(primary_order: list[str], current_root_id: str) -> str | None:
    index = primary_order.index(current_root_id)
    if index + 1 < len(primary_order):
        return primary_order[index + 1]
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Force-Ketten-Quiz lokal testen")
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path("docs/data/quiz100_forcechains_demo.csv"),
        help="Pfad zur Quiz-CSV-Datei",
    )
    parser.add_argument(
        "--start-id",
        default=None,
        help="Optionale Startfrage (z. B. Q001a)",
    )
    parser.add_argument(
        "--answers",
        default="",
        help="Kommagetrennte simulierte Antworten als A/B/C, z. B. B,B,A,C",
    )
    return parser.parse_args()


def to_answer_indexes(text: str) -> list[int]:
    if not text.strip():
        return []
    letters = [part.strip().upper() for part in text.split(",") if part.strip()]
    return [["A", "B", "C"].index(letter) for letter in letters]


def main() -> None:
    args = parse_args()
    questions = load_questions(args.csv)
    answers = to_answer_indexes(args.answers)
    run_quiz(questions, answers, args.start_id)


if __name__ == "__main__":
    main()
