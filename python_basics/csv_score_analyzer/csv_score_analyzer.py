import sys
import csv
from pathlib import Path

def get_csv_path() -> Path | None:
    if len(sys.argv) < 2:
        print("Usage: python csv_score_analyzer.py <csv_file_path>")
        return None
    return Path(sys.argv[1])

def read_scores(csv_path: Path) -> list[float]:
    scores = []
    
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            score = float(row["score"])
            scores.append(score)
    return scores

def analyze_scores(scores: list[float]) -> dict[str, int | float]:
    student_count = len(scores)
    average_score = sum(scores) / student_count if student_count > 0 else 0
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0

    fail_count = 0
    for score in scores:
        if score < 60:
            fail_count += 1

    result = {
        "count": student_count,
        "score": average_score,
        "max": max_score,
        "min": min_score,
        "fail_count": fail_count
    }
    return result

def print_result(result: dict[str, int | float]) -> None:
    print(f"Student count: {result['count']}")
    print(f"Average score: {result['score']:.2f}")
    print(f"Max score: {result['max']}")
    print(f"Min score: {result['min']}")
    print(f"Fail count: {result['fail_count']}")

def main():
    csv_path = get_csv_path()
    if csv_path is None:
        return
    
    if not csv_path.exists():
        print(f"Error: File '{csv_path}' does not exist.")
        return
    if not csv_path.is_file():
        print(f"Error: '{csv_path}' is not a file.")
        return
    
    scores = read_scores(csv_path)
    if not scores:
        print("No scores found in the CSV file.")
        return
    
    result = analyze_scores(scores=scores)
    print_result(result)

if __name__ == "__main__":
    main()