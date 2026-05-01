# csv_score_analyzer / CSV 成绩分析工具

这是一个用于读取 CSV 文件并统计学生成绩信息的简单 Python 工具.  
This is a simple Python tool for reading a CSV file and analyzing student score information.

## 功能 / Functions

- 读取包含学生成绩的 `.csv` 文件 / Read a `.csv` file containing student scores
- 统计学生总数 / Count the total number of students
- 计算平均分 / Calculate the average score
- 统计最高分和最低分 / Find the maximum and minimum scores
- 统计不及格人数 / Count the number of failing students

## 运行方式 / How to Run

```bash
python csv_score_analyzer.py scores.csv
```

## 示例输入 / Example Input

文件: `scores.csv`  
File: `scores.csv`

```csv
name,score
Alice,85
Bob,72
Cindy,90
David,58
Eric,66
```

## 示例输出 / Example Output

```text
Student count: 5
Average score: 74.20
Max score: 90
Min score: 58
Fail count: 1
```