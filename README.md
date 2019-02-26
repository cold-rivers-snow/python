这是一个python简单入门教程，参考[菜鸟教程](http://www.runoob.com/python/python-tutorial.html),今后将持续不断的更新python教程。

Python最新源码，二进制文档，新闻资讯等可以在Python的官网查看到：

[Python官网](https://www.python.org/)

你可以在以下链接中下载 Python 的文档，你可以下载 HTML、PDF 和 PostScript 等格式的文档。

[Python文档下载地址](https://www.python.org/doc/)

Unix & Linux 平台安装 Python:

以下为在 Unix & Linux 平台上安装 Python 的简单步骤：

    打开 WEB 浏览器访问https://www.python.org/downloads/source/
    选择适用 于Unix/Linux 的源码压缩包。
    下载及解压压缩包。
    如果你需要自定义一些选项修改Modules/Setup
    执行 ./configure 脚本
    make
    make install

执行以上操作后，Python 会安装在 /usr/local/bin 目录中，Python 库安装在 /usr/local/lib/pythonXX，XX 为你使用的 Python 的版本号。
Window 平台安装 Python:

以下为在 Window 平台上安装 Python 的简单步骤：

    打开 WEB 浏览器访问https://www.python.org/downloads/windows/

    在下载列表中选择Window平台安装包，包格式为：python-XYZ.msi 文件 ， XYZ 为你要安装的版本号。

    要使用安装程序 python-XYZ.msi, Windows 系统必须支持 Microsoft Installer 2.0 搭配使用。只要保存安装文件到本地计算机，然后运行它，看看你的机器支持 MSI。Windows XP 和更高版本已经有 MSI，很多老机器也可以安装 MSI。

    下载后，双击下载包，进入 Python 安装向导，安装非常简单，你只需要使用默认的设置一直点击"下一步"直到安装完成即可。

MAC 平台安装 Python:

MAC 系统一般都自带有 Python2.x版本 的环境，你也可以在链接 https://www.python.org/downloads/mac-osx/ 上下载最新版安装。

 
Ubuntu16.04 python2.7升级python3.5

　　正常情况下，你安装好ubuntu16.04版本之后，系统会自带 python2.7版本，如果需要下载新版本的python3.5，就需要进行更新。下面给出具体教程：
　　1.首先在ubuntu的终端ternimal输入命令：
　　 1 sudo apt-get install python3  （博主选择的是安装python3.5,命令为：sudo apt-get install python3.5）
　　输入你的密码后会下载，刚才下载的Python程序被安装在usr/localb/python3.5 中。
　　2.指定默认打开的是python3.5版本（你新安装的python版本）。
　　安装完成之后，你在终端中输入python，输出的信息里面会提示是2.7版本的，也就是说默认打开的并不是刚才安装好的3.5，所以还需要我们重新修改一下链接。方法如下：
　　第一步：先备份原来的链接（在对系统执行删除之前进行备份是个好的习惯）。在ternimal下输入命令：
　　 1 sudo cp /usr/bin/python /usr/bin/python_bak
　　第二步：删除原来默认指向python2.7版本的链接。在ternimal下输入命令：
　　 1 sudo rm /usr/bin/python
　　第三步：重新指定新的链接给python3.5版本。输入命令：
　　 1 sudo ln -s /usr/bin/python3.5 /usr/bin/python
　　至此，python版本更新已经完成。
　　附上博主成功截图一张：
 　　
 
　　
　　另：python2.7和3.5版本之间随意切换（这里3.5切换回2.7版本）：

1 sudo rm /usr/bin/python
2 sudo ln -s /usr/bin/python2.7 /usr/bin/python

unix/linux设置环境变量

    在 csh shell: 输入

    setenv PATH "$PATH:/usr/local/bin/python"

    , 按下"Enter"。
    在 bash shell (Linux): 输入

    export PATH="$PATH:/usr/local/bin/python" 

    ，按下"Enter"。
    在 sh 或者 ksh shell: 输入

    PATH="$PATH:/usr/local/bin/python" 

     永久有效写在家目录下.bashrc中,
     注意: /usr/local/bin/python 是 Python 的安装目录。

     在 Windows 设置环境变量

在环境变量中添加Python目录：

在命令提示框中(cmd) : 输入

path=%path%;C:\Python 

按下"Enter"。

注意: C:\Python 是Python的安装目录。

也可以通过以下方式设置：

    右键点击"计算机"，然后点击"属性"
    然后点击"高级系统设置"
    选择"系统变量"窗口下面的"Path",双击即可！
    然后在"Path"行，添加python安装路径即可(我的D:\Python32)，所以在后面，添加该路径即可。 ps：记住，路径直接用分号"；"隔开！
    最后设置成功以后，在cmd命令行，输入命令"python"，就可以有相关显示。


Python 环境变量

下面几个重要的环境变量，它应用于Python：
变量名	        描述
PYTHONPATH	    PYTHONPATH是Python搜索路径，默认我们import的模                  块都会从PYTHONPATH里面寻找。
PYTHONSTARTUP 	Python启动后，先寻找PYTHONSTARTUP环境变量，然后                 执行此变量指定的文件中的代码。
PYTHONCASEOK 	加入PYTHONCASEOK的环境变量, 就会使python导入模                  块的时候不区分大小写.
PYTHONHOME 	    另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或                 PYTHONPATH目录中，使得两个模块库更容易切换。
1、交互式解释器：

你可以通过命令行窗口进入python并开在交互式解释器中开始编写Python代码。

你可以在Unix，DOS或任何其他提供了命令行或者shell的系统进行python编码工作。
$ python # Unix/Linux

或者

C:>python # Windows/DOS 
以下为Python命令行参数：
选项	描述
-d	在解析时显示调试信息
-O	生成优化代码 ( .pyo 文件 )
-S	启动时不引入查找Python路径的位置
-V	输出Python版本号
-X	从 1.6版本之后基于内建的异常（仅仅用于字符串）已过时。
-c cmd	执行 Python 脚本，并将运行结果作为 cmd 字符串。
file	在给定的python文件执行python脚本。

2、命令行脚本

在你的应用程序中通过引入解释器可以在命令行中执行Python脚本，如下所示：
$ python script.py # Unix/Linux

或者

C:>python script.py # Windows/DOS

注意：在执行脚本时，请检查脚本是否有可执行权限。

3、集成开发环境（IDE：Integrated Development Environment）: PyCharm

PyCharm 是由 JetBrains 打造的一款 Python IDE，支持 macOS、 Windows、 Linux 系统。

PyCharm 功能 : 调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制……

[PyCharm 下载地址](https://www.jetbrains.com/pycharm/download/)

[PyCharm 安装地址](http://www.runoob.com/w3cnote/pycharm-windows-install.html)

对于 Python 学习的新手来说，安装 Anaconda 包管理软件是一个不错的选择，可以减少很多后续安装 Python 各种包的麻烦。在 Anaconda 自带的 notebook 进行代码的编写要比 IDE 和 Terminal 的体验好得多。

[Anaconda 的下载地址](https://www.anaconda.com/download/)

Windows 如果使用终端进行 Python 编程时，建议对终端进行一定的美化。

[Cmd 美化参考](https://zhuanlan.zhihu.com/p/31904974)

如果需要使用 Pycharm 又恰好是学生的话，可以免费申请享用高大上的Professional版本。

[申请地址](https://www.jetbrains.com/student/)

在填写学校邮箱申请完成后，会收到一封激活邮件。点击链接激活后会收到一封包含下载地址链接的邮件，就可以享用 Jetbrains 的所有专业软件了。

[Python3.6.3中文手册](http://www.runoob.com/manual/pythontutorial3/docs/html/appetite.html)


ipython 是一个 python 的交互式 shell，比默认的 python shell 好用得多，支持变量自动补全，自动缩进，支持 bash shell 命令，内置了许多很有用的功能和函数。

此 ipython 中的 i 代表 “交互(interaction)”。

[官方地址](https://ipython.org/install.html)

安装:

pip install ipython

Linux 环境还可以使用以下命令安装：

# Ubuntu
sudo apt-get install ipython

# Centos
yum  install ipython

使用:

ipython


Python 解释器可不止一种哦，有 CPython、IPython、Jython、PyPy 等。

顾名思义，CPython 就是用 C 语言开发的了，是官方标准实现，拥有良好的生态，所以应用也就最为广泛了。

而 IPython 是在 CPython 的基础之上在交互式方面得到增强的解释器（http://ipython.org/）。

Jython 是专为 Java 平台设计的 Python 解释器（http://www.jython.org/），它把 Python 代码编译成 Java 字节码执行。

PyPy 是 Python 语言（2.7.13和3.5.3）的一种快速、兼容的替代实现（http://pypy.org/），以速度快著称。