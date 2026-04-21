import string
from pathlib import Path
import sys

def count_characters(text):
    return len(text)


def extract_words(text):
    words = text.split()
    cleaned_words = []

    for word in words:
        cleaned_word = word.strip(string.punctuation).lower()
        if cleaned_word:
            cleaned_words.append(cleaned_word)

    return cleaned_words


def count_word_frequency(words_list):
    freq = {}
    for word in words_list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def format_result(character_count, word_count, unique_word_count, top_5_words):
    result = f"Character count: {character_count}\nWord count: {word_count}\nUnique word count: {unique_word_count}\nTop 5 most frequent words:\n"
    for word, count in top_5_words:
        result += f"{word}: {count}\n"
    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_stats.py <file_path>")
        return

    file_name = sys.argv[1]
    path = Path(__file__).parent / file_name

    if not path.exists():
        print(f"Error: file not found -> {path}")
        return

    text = path.read_text(encoding="utf-8")

    character_count = count_characters(text)
    words_list = extract_words(text)
    word_count = len(words_list)
    unique_word_count = len(set(words_list))

    freq = count_word_frequency(words_list)
    top_5_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:5]

    result = format_result(character_count, word_count, unique_word_count, top_5_words)

    print(result, end = "")

    result_path = Path(__file__).parent / "result.txt"
    result_path.write_text(result, encoding="utf-8")

if __name__ == "__main__":
    main()