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
