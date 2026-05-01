# robot / 机器人学习总仓库

这是一个用于记录我在人工智能, 机器人与具身智能方向长期学习过程的仓库.  
This repository records my long-term learning process in artificial intelligence, robotics, and embodied intelligence.

我当前的主学习路线是:  
My current main learning route is:

Python 工程基础 → Linux / ROS 2 → 移动机器人仿真 → 控制与规划 → 机械臂与具身智能扩展  
Python engineering fundamentals → Linux / ROS 2 → mobile robot simulation → control and planning → manipulator and embodied intelligence extension

## 仓库结构 / Repository Structure

```text
robot/
├── README.md
└── python_basics/
    ├── text_statistics_tool/
    ├── file_extension_counter/
    └── csv_score_analyzer/
        ├── csv_score_analyzer.py
        ├── scores.csv
        └── README.md
```

## 当前项目 / Current Projects

### 1. text_statistics_tool / 文本统计工具

位置: `python_basics/text_statistics_tool/`  
Location: `python_basics/text_statistics_tool/`

这是一个简单的 Python 文本分析工具, 可以:  
This is a simple Python text analysis tool that can:

- 读取 `.txt` 文件 / Read a `.txt` file
- 统计字符数 / Count characters
- 统计单词数 / Count words
- 统计唯一单词数 / Count unique words
- 输出出现频率最高的 5 个单词 / Show the top 5 most frequent words
- 将结果保存到 `result.txt` / Save the result to `result.txt`

### 2. file_extension_counter / 文件扩展名统计工具

位置: `python_basics/file_extension_counter/`  
Location: `python_basics/file_extension_counter/`

这是一个简单的 Python 工具, 用于统计指定文件夹中不同文件扩展名的数量.  
This is a simple Python tool for counting different file extensions in a specified folder.

它目前支持:  
It currently supports:

- 统计当前目录下不同扩展名文件的数量 / Count the number of files with different extensions in the current folder
- 不递归统计子文件夹 / Count files without scanning subfolders recursively
- 在终端中输出统计结果 / Print the counting results in the terminal

### 3. csv_score_analyzer / CSV 成绩分析工具

位置: `python_basics/csv_score_analyzer/`  
Location: `python_basics/csv_score_analyzer/`

这是一个简单的 Python 工具, 用于读取 CSV 文件并统计学生成绩信息.  
This is a simple Python tool for reading a CSV file and analyzing student score information.

它目前支持:  
It currently supports:

- 读取包含学生成绩的 `.csv` 文件 / Read a `.csv` file containing student scores
- 统计学生总数 / Count the total number of students
- 计算平均分 / Calculate the average score
- 统计最高分和最低分 / Find the maximum and minimum scores
- 统计不及格人数 / Count the number of failing students

## 说明 / Notes

这个仓库用于分阶段记录我的学习过程和项目积累.  
This repository is used to record my step-by-step learning process and project accumulation.

后续会继续加入更多模块, 包括 Linux, ROS 2, 移动机器人仿真, 路径规划等内容.  
More modules will be added later, including Linux, ROS 2, mobile robot simulation, and path planning.

本仓库中的学习工作在 ChatGPT 5.4 的指导下展开.  
The learning work in this repository is carried out under the guidance of ChatGPT 5.4.