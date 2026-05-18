import argparse
from pathlib import Path

import numpy as np

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
    description = "Analyze a numeric vector stored in a txt file."
)

    parser.add_argument(
    "vector_file",
    type=Path,
    help="Path to the input vector txt file.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default= "result.txt",
        help="Path to the output result txt file."
    )

    return parser.parse_args()

def load_vector(file_path: Path) -> np.ndarray:
    text = file_path.read_text(encoding="utf-8")
    values = text.split()

    numbers = []
    for value in values:
        numbers.append(float(value))
    return np.array(numbers)

def analyze_vector(vector: np.ndarray) -> dict:
    stats = {
        "count": len(vector),
        "mean": np.mean(vector),
        "std": np.std(vector),
        "min": np.min(vector),
        "max": np.max(vector),
        "sum": np.sum(vector)
    }
    return stats

def format_result(stats: dict) -> str:
    result = (
        f"Count: {stats['count']}\n"
        f"Mean: {stats['mean']:.2f}\n"
        f"Std: {stats['std']:.2f}\n"
        f"Min: {stats['min']:.2f}\n"
        f"Max: {stats['max']:.2f}\n"
        f"Sum: {stats['sum']:.2f}\n"
    )
    return result

def save_result(result_text: str, output_path: Path | str) -> None:
    output_path.write_text(result_text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    file_path = args.vector_file
    output_path = args.output

    if not file_path.exists():
        print(f"Error: file not found -> {file_path}")
        return

    if not file_path.is_file():
        print(f"Error: not a file -> {file_path}")
        return

    vector = load_vector(file_path)

    if len(vector) == 0:
        print("Error: empty vector.")
        return

    stats = analyze_vector(vector)
    result_text = format_result(stats)

    print(result_text)
    save_result(result_text, output_path)


if __name__ == "__main__":
    main()
