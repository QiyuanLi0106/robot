# numpy_vector_analyzer / numpy 向量分析工具

这是一个使用 Python 和 numpy 编写的简单向量统计工具.  
This is a simple vector analysis tool written with Python and numpy.

## 功能 / Functions

- 从 `.txt` 文件读取数字向量  
  Read a numeric vector from a `.txt` file
- 计算向量长度, 平均值, 标准差, 最小值, 最大值和总和  
  Calculate count, mean, standard deviation, minimum, maximum, and sum
- 将分析结果输出到终端  
  Print the analysis result to the terminal
- 将分析结果保存到 `result.txt`  
  Save the analysis result to `result.txt`

## 项目结构 / Project Structure

```text
numpy_vector_analyzer/
├── vector_analyzer.py
├── vector.txt
├── result.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## 运行方式 / How to Run

先安装依赖:  
Install dependencies first:

```bash
pip install -r requirements.txt
```

运行程序:  
Run the program:

```bash
python vector_analyzer.py vector.txt
```

查看帮助信息:  
Show help information:

```bash
python vector_analyzer.py -h
```

指定输出文件:  
Specify the output file:

```bash
python vector_analyzer.py vector.txt --output my_result.txt
```

## 示例输入 / Example Input

```text
1 2 3 4 5 6 7 8 9 10
```

## 示例输出 / Example Output

```text
Count: 10
Mean: 5.50
Std: 2.87
Min: 1.00
Max: 10.00
Sum: 55.00
```

## 说明 / Notes

本项目是 Python 工程基础阶段的 numpy 练习项目.  
This project is a numpy practice project in the Python engineering fundamentals stage.
