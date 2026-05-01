from pathlib import Path
import sys

def get_arguments() -> tuple[Path, str] | None:
    if len(sys.argv) != 3:
        print("Usage: python log_keyword_counter.py <log_file_path> <keyword>")
        return None
    log_path = Path(sys.argv[1])
    keyword = sys.argv[2]
    return log_path, keyword

def count_keyword(log_path: Path, keyword: str) -> int:
    count = 0
    with log_path.open('r', encoding='utf-8') as file:
        for line in file:
            count += line.count(keyword)
    return count

def print_result(keyword: str, count: int) -> None:
    print(f"Keyword: {keyword}")
    print(f"Count: {count}")

def main() -> None:
    args = get_arguments()
    if args is None:
        return
    
    log_path, keyword = args

    if not log_path.exists():
        print(f"Error: {log_path} does not exist.")
        return
    if not log_path.is_file():
        print(f"Error: {log_path} is not a valid file.")
        return

    count = count_keyword(log_path, keyword)
    print_result(keyword, count)

if __name__ == "__main__":
    main()