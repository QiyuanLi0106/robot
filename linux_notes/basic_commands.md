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

符号 `>` 表示覆盖写入文件.  
The symbol `>` writes to a file by overwriting existing content.

符号 `>>` 表示追加写入文件.  
The symbol `>>` appends content to a file.

```bash
echo "line 1" > multi_line.txt
echo "line 2" >> multi_line.txt
```

## 权限与 Shell 脚本 / Permissions and Shell Scripts

### `ls -l`

查看文件和目录的详细信息, 包括权限, 所有者, 大小和修改时间.  
Show detailed information about files and directories, including permissions, owner, size, and modification time.

```bash
ls -l
```

权限示例:  
Permission example:

```text
-rw-r--r--
```

其中 `r` 表示可读, `w` 表示可写, `x` 表示可执行.  
Here, `r` means read, `w` means write, and `x` means execute.

### `chmod +x`

给文件添加可执行权限.  
Add executable permission to a file.

```bash
chmod +x hello.sh
```

### `bash script.sh`

使用 bash 执行脚本文件.  
Run a script file with bash.

```bash
bash hello.sh
```

这种方式不要求脚本本身具有可执行权限.  
This method does not require the script itself to have executable permission.

### `./script.sh`

直接执行当前目录下的脚本文件.  
Execute a script file in the current directory directly.

```bash
./hello.sh
```

这种方式要求脚本文件具有可执行权限.  
This method requires the script file to have executable permission.

### Shebang

Shell 脚本第一行通常写成:  
The first line of a shell script is usually written as:

```bash
#!/bin/bash
```

它表示这个脚本使用 bash 解释器执行.  
It means the script should be executed with the bash interpreter.

### Pipe

管道 `|` 会把左边命令的输出传给右边命令继续处理.  
The pipe `|` passes the output of the left command to the right command for further processing.

```bash
ls | wc -l
```

这个命令表示先列出当前目录内容, 再统计输出行数.  
This command lists the current directory contents first, then counts the number of output lines.

### Shell Script with Arguments

Shell 脚本可以接收命令行参数.  
Shell scripts can accept command-line arguments.

常用参数变量:  
Common parameter variables:

- `$1` 表示第一个参数 / `$1` represents the first argument  
- `$2` 表示第二个参数 / `$2` represents the second argument  
- `$#` 表示参数个数 / `$#` represents the number of arguments  

示例:  
Example:

```bash
#!/bin/bash

if [ $# != 1 ]
then
    echo "Usage: ./greet.sh <name>"
else
    echo "Hello, $1"
fi
```

运行方式:  
How to run:

```bash
./greet.sh qiyuan
```

输出:  
Output:

```text
Hello, qiyuan
```

如果参数错误:  
If arguments are incorrect:

```bash
./greet.sh
```

输出:  
Output:

```text
Usage: ./greet.sh <name>
```

## 环境变量与 source / Environment Variables and source

### Environment Variable

环境变量是当前终端或系统中保存的一些配置信息.  
Environment variables are configuration values stored in the current terminal or system.

常见环境变量:  
Common environment variables:

- `$HOME`: 当前用户家目录 / Current user's home directory
- `$USER`: 当前用户名 / Current username
- `$PATH`: 系统查找可执行命令的路径列表 / Search paths for executable commands

```bash
echo $HOME
echo $USER
echo $PATH
```

### `export`

设置环境变量.  
Set an environment variable.

```bash
export ROBOT_NAME=mobile_robot_01
```

临时修改 PATH:  
Temporarily modify PATH:

```bash
export PATH=$PATH:$(pwd)
```

这表示在原来的 PATH 后面追加当前目录.  
This appends the current directory to the original PATH.

### `source`

在当前 shell 中执行脚本, 常用于加载环境配置.  
Run a script in the current shell, commonly used to load environment configuration.

```bash
source setup_env.sh
```

### `bash script.sh` 和 `source script.sh` 的区别 / Difference Between `bash script.sh` and `source script.sh`

`bash script.sh` 会在子 shell 中执行脚本, 脚本结束后变量通常不会保留在当前终端.  
`bash script.sh` runs the script in a subshell, so variables usually do not remain in the current terminal after the script ends.

`source script.sh` 会在当前 shell 中执行脚本, 脚本设置的环境变量会保留在当前终端.  
`source script.sh` runs the script in the current shell, so environment variables set by the script remain in the current terminal.

### `env | grep`

查看并筛选环境变量.  
Show and filter environment variables.

```bash
env | grep ROBOT
```

### Why ROS 2 Uses `source`

ROS 2 经常使用 `source install/setup.bash`, 目的是把 ROS 2 工作空间的环境变量加载到当前终端.  
ROS 2 often uses `source install/setup.bash` to load workspace environment variables into the current terminal.

## `.bashrc`, alias, and Automatic Environment Loading

### `.bashrc`

`.bashrc` 是 bash 启动交互式终端时会读取的配置文件.  
`.bashrc` is a configuration file read by bash when starting an interactive terminal.

```bash
nano ~/.bashrc
```

修改 `.bashrc` 前建议先备份.  
It is recommended to back up `.bashrc` before modifying it.

```bash
cp ~/.bashrc ~/.bashrc_backup
```

### `alias`

`alias` 可以给长命令设置短名字.  
`alias` can define a short name for a long command.

```bash
alias robot_status='~/bashrc_practice/robot_status.sh'
```

之后可以直接运行:  
Then it can be run directly:

```bash
robot_status
```

### `source ~/.bashrc`

修改 `.bashrc` 后, 使用 `source ~/.bashrc` 让配置在当前终端立即生效.  
After modifying `.bashrc`, use `source ~/.bashrc` to make the configuration take effect in the current terminal.

```bash
source ~/.bashrc
```

### Why ROS 2 Uses `.bashrc`

ROS 2 经常需要加载环境配置, 例如:  
ROS 2 often needs to load environment configuration, for example:

```bash
source /opt/ros/jazzy/setup.bash
```

如果把这条命令写进 `.bashrc`, 每次打开 bash 终端时就会自动加载 ROS 2 环境.  
If this command is written into `.bashrc`, the ROS 2 environment will be loaded automatically whenever a bash terminal starts.

## apt 包管理与命令查询 / apt Package Management and Command Lookup

### `sudo apt update`

更新本地软件包索引.  
Update the local package index.

```bash
sudo apt update
```

### `apt search`

搜索软件包.  
Search for packages.

```bash
apt search tree
```

### `apt show`

查看软件包详细信息.  
Show detailed information about a package.

```bash
apt show tree
```

### `sudo apt install`

安装软件包.  
Install a package.

```bash
sudo apt install tree
```

### `sudo apt remove`

卸载软件包.  
Remove a package.

```bash
sudo apt remove tree
```

### `which`

查看命令实际对应的可执行文件路径.  
Show the executable path used by a command.

```bash
which python3
which tree
```

### `whereis`

查找命令相关的二进制文件, 源码和帮助文档位置.  
Find binary, source, and manual locations for a command.

```bash
whereis python3
whereis tree
```

### `dpkg -l`

查看系统中已安装的软件包.  
List installed packages on the system.

```bash
dpkg -l | grep tree
```

### `tree`

以树状结构显示目录.  
Display directories in a tree-like format.

```bash
tree -L 2
```

其中 `-L 2` 表示只显示 2 层目录.  
Here, `-L 2` means displaying only two directory levels.

## Python 虚拟环境 / Python Virtual Environment

### `python3 -m venv`

创建 Python 虚拟环境.  
Create a Python virtual environment.

```bash
python3 -m venv .venv
```

其中 `.venv` 是虚拟环境目录名.  
Here, `.venv` is the virtual environment directory name.

### `source .venv/bin/activate`

激活虚拟环境.  
Activate the virtual environment.

```bash
source .venv/bin/activate
```

激活后, 当前终端会使用虚拟环境中的 Python 和 pip.  
After activation, the current terminal uses Python and pip from the virtual environment.

### `which python` and `which pip`

查看当前使用的 Python 和 pip 路径.  
Check the paths of the currently used Python and pip.

```bash
which python
which pip
```

### `pip install`

安装 Python 包.  
Install a Python package.

```bash
pip install numpy
```

### `pip list`

查看当前环境中已安装的 Python 包.  
List installed Python packages in the current environment.

```bash
pip list
```

### `pip freeze`

导出当前环境中的包和版本.  
Export packages and versions in the current environment.

```bash
pip freeze > requirements.txt
```

### `requirements.txt`

`requirements.txt` 用于记录项目依赖.  
`requirements.txt` is used to record project dependencies.

别人可以使用下面的命令复现环境:  
Others can reproduce the environment with:

```bash
pip install -r requirements.txt
```

### `deactivate`

退出当前虚拟环境.  
Exit the current virtual environment.

```bash
deactivate
```
