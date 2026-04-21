# Text Statistics Tool

This is a simple Python tool for analyzing text files.

## Functions
- Read a `.txt` file
- Count characters
- Count words
- Count unique words
- Show the top 5 most frequent words
- Save the result to `result.txt`

## How to Run

```bash
python test_stats.py sample.txt
```

## Example Input

File: `sample.txt`

```text
Machine learning is useful.
Machine learning is powerful and useful.
Robots need control and perception.
```

## Example Output

File: `result.txt`

```text
Character count: 104
Word count: 15
Unique word count: 10
Top 5 most frequent words:
and: 2
is: 2
learning: 2
machine: 2
useful: 2
```