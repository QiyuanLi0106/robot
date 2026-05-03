# basic_commands / Linux 基础命令

这个文件记录 Linux 入门阶段最常用的基础命令.  
This file records the most commonly used basic commands in the Linux introduction stage.

## 路径与目录 / Path and Directory

### `pwd`

显示当前所在路径.  
Print the current working directory.

```bash
pwd
```

### `cd`

切换目录.  
Change the current directory.

```bash
cd ~
cd /mnt/d/code/robot
```

### `ls`

查看当前目录下的文件和文件夹.  
List files and directories in the current folder.

```bash
ls
```

### `mkdir`

创建新文件夹.  
Create a new directory.

```bash
mkdir linux_notes
```

## 文件操作 / File Operations

### `touch`

创建空文件.  
Create an empty file.

```bash
touch notes.txt
```

### `cat`

查看文件内容.  
Display file content.

```bash
cat notes.txt
```

### `echo`

向终端输出文本, 也可以配合 `>` 写入文件.  
Print text to the terminal, or write text into a file with `>`.

```bash
echo "Linux practice started"
echo "Linux practice started" > notes.txt
```

### `nano`

在终端中编辑文本文件.  
Edit text files in the terminal.

```bash
nano README.md
```

## WSL 路径 / WSL Path

Windows 中的 D 盘在 WSL 中对应:  
The D drive in Windows corresponds to this path in WSL:

```bash
/mnt/d
```

例如, Windows 路径:  
For example, the Windows path:

```text
D:\code\robot
```

在 WSL 中对应:  
Corresponds to this path in WSL:

```bash
/mnt/d/code/robot
```

## 文件和目录操作强化 / File and Directory Operations

### `cp`

复制文件或目录.  
Copy files or directories.

```bash
cp log1.txt log1_backup.txt
```

### `mv`

移动或重命名文件.  
Move or rename files.

```bash
mv log3.txt navigation.log
```

### `rm`

删除文件.  
Remove files.

```bash
rm log1_backup.txt
```

注意: `rm` 删除的文件不会进入 Windows 回收站.  
Note: Files removed by `rm` do not go to the Windows recycle bin.

### `grep`

在文件中搜索指定关键词.  
Search for a specified keyword in files.

```bash
grep error *.log
grep error *.txt
```

### `wc`

统计文件的行数, 单词数和字节数.  
Count lines, words, and bytes in files.

```bash
wc log1.txt
wc *.log
```

### `head`

查看文件开头的内容.  
Show the beginning of a file.

```bash
head -n 2 multi_line.txt
```

### `tail`

查看文件末尾的内容.  
Show the end of a file.

```bash
tail -n 2 multi_line.txt
```

### `find`

按条件查找文件.  
Find files by conditions.

```bash
find . -name "*.log"
find . -name "*.txt"
```

### Output Redirection

`>` 表示覆盖写入文件.  
`>` writes to a file by overwriting existing content.

`>>` 表示追加写入文件.  
`>>` appends content to a file.

```bash
echo "line 1" > multi_line.txt
echo "line 2" >> multi_line.txt
```