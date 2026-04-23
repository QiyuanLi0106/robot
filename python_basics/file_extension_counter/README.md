# file_extension_counter / 文件扩展名统计工具

这是一个用于统计指定文件夹中文件扩展名数量的简单 Python 工具.  
This is a simple Python tool for counting file extensions in a specified folder.

## 功能 / Functions

- 统计指定文件夹中不同文件扩展名的数量  
  Count the number of different file extensions in a specified folder
- 只统计当前目录下的文件，不递归子文件夹  
  Count only files in the current folder without scanning subfolders recursively
- 在终端中输出统计结果  
  Print the counting results in the terminal

## 运行方式 / How to Run

```bash
python file_extension_counter.py sample_files
```

## 示例输入 / Example Input

目录：`sample_files/`  
Folder: `sample_files/`

```text
a.py
b.py
notes.txt
data.txt
readme.md
```

## 示例输出 / Example Output

```text
.md: 1
.py: 2
.txt: 2
```