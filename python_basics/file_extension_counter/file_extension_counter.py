import sys
from pathlib import Path

def get_target_path() -> Path:
    if len(sys.argv) < 2:
        print("Usage: python file_extension_counter.py <folder_path>")
        return None
    return Path(sys.argv[1])

def count_file_extensions(folder_path: Path | str) -> dict:
    extension_count = {}
    for file in folder_path.iterdir():
        if file.is_file():
            ext = file.suffix
            if ext in extension_count:
                extension_count[ext] += 1
            else:
                extension_count[ext] = 1
        else:
            continue
    return extension_count

def print_extension_counts(extension_count: dict):
    for key, value in extension_count.items():
        print(f"{key}: {value}")

def main():
    if (target_path := get_target_path()) is None:
        print("Error: No folder path provided.")
        return
    if not target_path.exists():
        print(f"Error: Folder not found -> {target_path}")
        return
    if not target_path.is_dir():
        print(f"Error: Provided path is not a folder -> {target_path}")
        return
    if not any(target_path.iterdir()):
        print(f"Error: Folder is empty -> {target_path}")
        return
    extension_count = count_file_extensions(target_path)
    print_extension_counts(extension_count)

if __name__ == "__main__":
    main()