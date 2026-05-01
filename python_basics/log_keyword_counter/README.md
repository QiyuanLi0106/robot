# log_keyword_counter / 日志关键词统计工具

这是一个用于统计日志文件中指定关键词出现次数的简单 Python 工具.  
This is a simple Python tool for counting occurrences of a specified keyword in a log file.

## 功能 / Functions

- 读取 `.log` 日志文件 / Read a `.log` file
- 从命令行接收关键词 / Receive the keyword from command-line arguments
- 统计关键词在日志文件中的出现次数 / Count occurrences of the keyword in the log file
- 在终端中输出统计结果 / Print the counting result in the terminal

## 运行方式 / How to Run

```bash
python log_keyword_counter.py sample.log ERROR
```

## 示例输入 / Example Input

文件: `sample.log`  
File: `sample.log`

```text
[INFO] Robot started successfully
[WARNING] Battery level is low
[INFO] Navigation module initialized
[ERROR] Failed to connect to sensor
[INFO] Retrying sensor connection
[ERROR] Sensor connection failed again
```

## 示例输出 / Example Output

```text
Keyword: ERROR
Count: 2
```