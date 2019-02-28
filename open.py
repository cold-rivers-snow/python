#!/usr/bin/python3

'''
Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

open(file, mode='r')
完整的语法格式为：

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener:
mode 参数有：

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（不推荐）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
默认为文本模式，如果要以二进制模式打开，加上 b 。



close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。

当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。

语法
close() 方法语法如下：

fileObject.close();
参数
无

返回值
该方法没有返回值。

flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。

一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。

语法
flush() 方法语法如下：

fileObject.flush();
参数
无

返回值
该方法没有返回值


fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。

语法
fileno() 方法语法如下：

fileObject.fileno(); 
参数
无

返回值
返回文件描述符。

isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。

语法
isatty() 方法语法如下：

fileObject.isatty(); 
参数
无

返回值
如果连接到一个终端设备返回 True，否则返回 False。

Python 3 中的 File 对象不支持 next() 方法。 Python 3 的内置函数 next() 通过迭代器调用 __next__() 方法返回下一项。 在循环中，next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration

语法
next() 方法语法如下：

next(iterator[,default])
参数
无

返回值
返回文件下一行。

read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。

语法
read() 方法语法如下：

fileObject.read(); 
参数
size -- 从文件中读取的字节数。

返回值
返回从字符串中读取的字节。


readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。

语法
readline() 方法语法如下：

fileObject.readline(); 
参数
size -- 从文件中读取的字节数。

返回值
返回从字符串中读取的字节。

readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。 如果碰到结束符 EOF 则返回空字符串。

如果碰到结束符 EOF 则返回空字符串。

语法
readlines() 方法语法如下：

fileObject.readlines( );
参数
无。

返回值
返回列表，包含所有的行。

seek() 方法用于移动文件读取指针到指定位置。

语法
seek() 方法语法如下：

fileObject.seek(offset[, whence])
参数
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。

whence：可选，默认值为 0。给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。

返回值
该函数没有返回值。

tell() 方法返回文件的当前位置，即文件指针当前位置。

语法
tell() 方法语法如下：

fileObject.tell()
参数
无

返回值
返回文件的当前位置

truncate() 方法用于从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。 。

语法
truncate() 方法语法如下：

fileObject.truncate( [ size ])
参数
size -- 可选，如果存在则文件截断为 size 字节。

返回值
该方法没有返回值。

write() 方法用于向文件中写入指定字符串。

在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。

语法
write() 方法语法如下：

fileObject.write( [ str ])
参数
str -- 要写入文件的字符串。

返回值
返回的是写入的字符长度。

writelines() 方法用于向文件中写入一序列的字符串。

这一序列字符串可以是由迭代对象产生的，如一个字符串列表。

换行需要制定换行符 \n。

语法
writelines() 方法语法如下：

fileObject.writelines( [ str ])
参数
str -- 要写入文件的字符串序列。

返回值
该方法没有返回值。


os 模块提供了非常丰富的方法用来处理文件和目录

os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。

语法
access()方法语法格式如下：

os.access(path, mode);
参数
path -- 要用来检测是否有访问权限的路径。

mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。

os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
返回值
如果允许访问返回 True , 否则返回False。

os.chdir() 方法用于改变当前工作目录到指定的路径。

语法
chdir()方法语法格式如下：

os.chdir(path)
参数
path -- 要切换到的新路径。

返回值
如果允许访问返回 True , 否则返回False。


os.chflags() 方法用于设置路径的标记为数字标记。多个标记可以使用 OR 来组合起来。

只支持在 Unix 下使用。

语法
chflags()方法语法格式如下：

os.chflags(path, flags)
参数
path -- 文件名路径或目录路径。

flags -- 可以是以下值：

stat.UF_NODUMP: 非转储文件
stat.UF_IMMUTABLE: 文件是只读的
stat.UF_APPEND: 文件只能追加内容
stat.UF_NOUNLINK: 文件不可删除
stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
stat.SF_ARCHIVED: 可存档文件(超级用户可设)
stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
stat.SF_APPEND: 文件只能追加内容(超级用户可设)
stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
stat.SF_SNAPSHOT: 快照文件(超级用户可设)
返回值
该方法没有返回值。

os.chmod() 方法用于更改文件或目录的权限。

Unix 系统可用。

语法
chmod()方法语法格式如下：

os.chmod(path, mode)
参数
path -- 文件名路径或目录路径。

flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。

stat.S_IXOTH: 其他用户有执行权0o001
stat.S_IWOTH: 其他用户有写权限0o002
stat.S_IROTH: 其他用户有读权限0o004
stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
stat.S_IXGRP: 组用户有执行权限0o010
stat.S_IWGRP: 组用户有写权限0o020
stat.S_IRGRP: 组用户有读权限0o040
stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
stat.S_IXUSR: 拥有者具有执行权限0o100
stat.S_IWUSR: 拥有者具有写权限0o200
stat.S_IRUSR: 拥有者具有读权限0o400
stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
stat.S_IREAD: windows下设为只读
stat.S_IWRITE: windows下取消只读
返回值
该方法没有返回值。


os.chown() 方法用于更改文件所有者，如果不修改可以设置为 -1, 你需要超级用户权限来执行权限修改操作。

只支持在 Unix 下使用。

语法
chown()方法语法格式如下：

os.chown(path, uid, gid);
参数
path -- 设置权限的文件路径

uid -- 所属用户 ID

gid -- 所属用户组 ID

返回值
该方法没有返回值。

os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。

在 unix 中有效。

语法
chroot()方法语法格式如下：

os.chroot(path);
参数
path -- 要设置为根目录的目录。

返回值
该方法没有返回值。


os.close() 方法用于关闭指定的文件描述符 fd。

语法
close()方法语法格式如下：

os.close(fd);
参数
fd -- 文件描述符。

返回值
该方法没有返回值。


os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。

语法
closerange()方法语法格式如下：

os.closerange(fd_low, fd_high);
参数
fd_low -- 最小文件描述符

fd_high -- 最大文件描述符

该方法类似于：

for fd in xrange(fd_low, fd_high):
    try:
        os.close(fd)
    except OSError:
        pass
返回值
该方法没有返回值。


os.dup() 方法用于复制文件描述符 fd。

语法
dup()方法语法格式如下：

os.dup(fd);
参数
fd -- 文件描述符

返回值
返回复制的文件描述符。


os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。

Unix, Windows 上可用。

语法
dup2()方法语法格式如下：

os.dup2(fd, fd2);
参数
fd -- 要被复制的文件描述符

fd2 -- 复制的文件描述符

返回值
没有返回值。


os.fchdir() 方法通过文件描述符改变当前工作目录。

Unix, Windows 上可用。

语法
fchdir()方法语法格式如下：

os.fchdir(fd);
参数
fd -- 文件描述符

返回值
该方法没有返回值。


os.fchmod() 方法用于改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。

Unix上可用。

语法
fchmod()方法语法格式如下：

os.fchmod(fd, mode);
参数
fd -- 文件描述符

mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：

stat.S_ISUID:设置 UID 位

stat.S_ISGID: 设置组 ID 位

stat.S_ENFMT: 系统文件锁定的执法行动

stat.S_ISVTX: 在执行之后保存文字和图片

stat.S_IREAD: 对于拥有者读的权限，Unix V7 版本中 stat.S_IRUSR 的代名词

stat.S_IWRITE: 对于拥有者写的权限，Unix V7 版本中 stat.S_IWUSR 的代名词

stat.S_IEXEC: 对于拥有者执行的权限，Unix V7 版本中 stat.S_IXUSR 的代名词

stat.S_IRWXU:对于拥有者读、写、执行的权限

stat.S_IRUSR: 对于拥有者读的权限

stat.S_IWUSR: 对于拥有者写的权限

stat.S_IXUSR: 对于拥有者执行的权限

stat.S_IRWXG: 对于同组的人读写执行的权限

stat.S_IRGRP: 对于同组读的权限

stat.S_IWGRP:对于同组写的权限

stat.S_IXGRP: 对于同组执行的权限

stat.S_IRWXO: 对于其他组读写执行的权限

stat.S_IROTH: 对于其他组读的权限

stat.S_IWOTH: 对于其他组写的权限

stat.S_IXOTH:对于其他组执行的权限

返回值
该方法没有返回值。


os.fchown() 方法用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

Unix上可用。

语法
fchown()方法语法格式如下：

os.fchown(fd, uid, gid)
参数
fd -- 文件描述符

uid -- 文件所有者的用户id

gid -- 文件所有者的用户组id

返回值
该方法没有返回值。

os.fdatasync() 方法用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。

Unix上可用。

语法
fdatasync()方法语法格式如下：

os.fdatasync(fd);
参数
fd -- 文件描述符

返回值
该方法没有返回值。


os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。

该方法是内置函数 open() 的别名，可以接收一样的参数，唯一的区别是 fdopen() 的第一个参数必须是整型。

语法
fdopen()方法语法格式如下：

os.fdopen(fd, [, mode[, bufsize]]);
参数
fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。

mode -- 可选，和 Python 内建的 open 函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。

bufsize -- 可选，指定返回的文件对象是否带缓冲：bufsize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。

返回值
通过文件描述符返回的文件对象


os.fpathconf() 方法用于返回一个打开的文件的系统配置信息。

Unix上可用。

语法
fpathconf()方法语法格式如下：

os.fpathconf(fd, name)
参数
fd -- 打开的文件的描述符。

name -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。

返回值
返回一个打开的文件的系统配置信息。


os.fstat() 方法用于返回文件描述符fd的状态，类似 stat()。

Unix，Windows上可用。

fstat 方法返回的结构:

st_dev: 设备信息

st_ino: 文件的i-node值

st_mode: 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)

st_nlink: 硬连接数

st_uid: 用户ID

st_gid: 用户组 ID

st_rdev: 设备 ID (如果指定文件)

st_size: 文件大小，以byte为单位

st_blksize: 系统 I/O 块大小

st_blocks: 文件的是由多少个 512 byte 的块构成的

st_atime: 文件最近的访问时间

st_mtime: 文件最近的修改时间

st_ctime: 文件状态信息的修改时间（不是文件内容的修改时间）

语法
fstat()方法语法格式如下：

os.fstat(fd)
参数
fd -- 文件的描述符。

返回值
返回文件描述符fd的状态。



os.fstatvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息，类似 statvfs()。

Unix上可用。

fstatvfs 方法返回的结构:

f_bsize: 文件系统块大小

f_frsize: 分栈大小

f_blocks: 文件系统数据块总数

f_bfree: 可用块数

f_bavail:非超级用户可获取的块数

f_files: 文件结点总数

f_ffree: 可用文件结点数

f_favail: 非超级用户的可用文件结点数

f_fsid: 文件系统标识 ID

f_flag: 挂载标记

f_namemax: 最大文件长度

语法
fstatvfs()方法语法格式如下：

os.fstatvfs(fd)
参数
fd -- 文件的描述符。

返回值
返回包含文件描述符fd的文件的文件系统的信息。


os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。

如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。

Unix、Windows上可用。

语法
fsync()方法语法格式如下：

os.fsync(fd)
参数
fd -- 文件的描述符。

返回值
该方法没有返回值。


os.ftruncate() 裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。

Unix上可用。

语法
ftruncate()方法语法格式如下：

os.ftruncate(fd, length)¶
参数
fd -- 文件的描述符。

length -- 要裁剪文件大小。

返回值
该方法没有返回值。


os.getcwd() 方法用于返回当前工作目录。

语法
getcwd()方法语法格式如下：

os.getcwd()
参数
无
返回值
返回当前进程的工作目录。


os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象。

Unix, Windows 系统下可用。

语法
getcwdu()方法语法格式如下：

os.getcwdu()
参数
无
返回值
返回一个当前工作目录的Unicode对象。

os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

语法
isatty()方法语法格式如下：

os.isatty()
参数
无
返回值
如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。


os.lchflags() 方法用于设置路径的标记为数字标记，类似 chflags()，但是没有软链接。

只支持在 Unix 下使用。

语法
lchflags()方法语法格式如下：

os.lchflags(path, flags)
参数
path -- 设置标记的文件路径

flags -- 可以由一个或多个标记组合，多个使用"|"隔开：

UF_NODUMP: 非转储文件

UF_IMMUTABLE: 文件是只读的

UF_APPEND: 文件只能追加内容

UF_NOUNLINK: 文件不可删除

UF_OPAQUE: 目录不透明，需要通过联合堆栈查看

SF_ARCHIVED: 可存档文件(超级用户可设)

SF_IMMUTABLE: 文件是只读的(超级用户可设)

SF_APPEND: 文件只能追加内容(超级用户可设)

SF_NOUNLINK: 文件不可删除(超级用户可设)

SF_SNAPSHOT: 快照文件(超级用户可设)

返回值
该方法没有返回值。


os.lchmod() 方法用于修改连接文件权限。

只支持在 Unix 下使用。

语法
lchmod()方法语法格式如下：

os.lchmod(path, mode)
参数
path -- 设置标记的文件路径

mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：

stat.S_ISUID:设置 UID 位

stat.S_ISGID: 设置组 ID 位

stat.S_ENFMT: 系统文件锁定的执法行动

stat.S_ISVTX: 在执行之后保存文字和图片

stat.S_IREAD: 对于拥有者读的权限

stat.S_IWRITE: 对于拥有者写的权限

stat.S_IEXEC: 对于拥有者执行的权限

stat.S_IRWXU:对于拥有者读、写、执行的权限

stat.S_IRUSR: 对于拥有者读的权限

stat.S_IWUSR: 对于拥有者写的权限

stat.S_IXUSR: 对于拥有者执行的权限

stat.S_IRWXG: 对于同组的人读写执行的权限

stat.S_IRGRP: 对于同组读的权限

stat.S_IWGRP:对于同组写的权限

stat.S_IXGRP: 对于同组执行的权限

stat.S_IRWXO: 对于其他组读写执行的权限

stat.S_IROTH: 对于其他组读的权限

stat.S_IWOTH: 对于其他组写的权限

stat.S_IXOTH:对于其他组执行的权限

返回值
该方法没有返回值。


os.lchown() 方法用于更改文件所有者，类似 chown，但是不追踪链接。

只支持在 Unix 下使用。

语法
lchown()方法语法格式如下：

os.lchown(path, uid, gid)
参数
path -- 设置权限的文件路径

uid -- 所属用户 ID

gid -- 所属用户组 ID

返回值
该方法没有返回值。


os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。

该方法对于创建一个已存在文件的拷贝是非常有用的。

只支持在 Unix, Windows 下使用。

语法
link()方法语法格式如下：

os.link(src, dst)
参数
src -- 用于创建硬连接的源地址

dst -- 用于创建硬连接的目标地址

返回值
该方法没有返回值。

os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。

只支持在 Unix, Windows 下使用。

语法
listdir()方法语法格式如下：

os.listdir(path)
参数
path -- 需要列出的目录路径

返回值
返回指定路径下的文件和文件夹列表。


os.lseek() 方法用于设置文件描述符 fd 当前位置为 pos, how 方式修改。

在Unix，Windows中有效。

语法
lseek()方法语法格式如下：

os.lseek(fd, pos, how)
参数
fd -- 文件描述符。

pos -- 这是相对于给定的参数 how 在文件中的位置。。

how -- 文件内参考位置。SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。

返回值
该方法没有返回值。


os.lstat() 方法用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。

语法
lstat()方法语法格式如下：

os.lstat(path)
参数
path -- 要返回信息的文件。

返回值
返回文件信息。


os.major() 方法用于从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

语法
major()方法语法格式如下：

os.major(device)
参数
device -- 原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

返回值
返回设备major号码。


os.makedev() 方法用于以major和minor设备号组成一个原始设备号。

语法
makedev()方法语法格式如下：

os.makedev(major, minor)
参数
major -- Major 设备号。

minor -- inor 设备号。

返回值
返回设备号。


os.makedirs() 方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。

语法
makedirs()方法语法格式如下：

os.makedirs(path, mode=0o777)
参数
path -- 需要递归创建的目录。

mode -- 权限模式。

返回值
该方法没有返回值。


os.minor() 方法用于从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。

语法
minor()方法语法格式如下：

os.minor(device)
参数
device -- 原始的设备(使用stat中的st_dev或者st_rdev field )

返回值
返回设备 minor 号。


os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。

语法
mkdir()方法语法格式如下：

os.mkdir(path[, mode])
参数
path -- 要创建的目录

mode -- 要为目录设置的权限数字模式

返回值
该方法没有返回值。


os.mkfifo() 方法用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。

语法
mkfifo()方法语法格式如下：

os.mkfifo(path[, mode])
参数
path -- 要创建的目录

mode -- 要为目录设置的权限数字模式

返回值
该方法没有返回值。

os.mknod() 方法用于创建一个指定文件名的文件系统节点（文件，设备特别文件或者命名pipe）。

语法
mknod()方法语法格式如下：

os.mknod(filename[, mode=0600[, device=0]])
参数
filename -- 创建的文件系统节点

mode -- mode指定创建或使用节点的权限, 组合 (或者bitwise) stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, 和stat.S_IFIFO (这些常数在stat模块). 对于 stat.S_IFCHR和stat.S_IFBLK, 设备定义了 最新创建的设备特殊文件 (可能使用 os.makedev()),其它都将忽略。

device -- 可选，指定创建文件的设备

返回值
该方法没有返回值。


os.open() 方法用于打开一个文件，并且设置需要的打开选项，模式参数mode参数是可选的，默认为 0777。

语法
open()方法语法格式如下：

os.open(file, flags[, mode]);
参数
file -- 要打开的文件

flags -- 该参数可以是以下选项，多个使用 "|" 隔开：

os.O_RDONLY: 以只读的方式打开
os.O_WRONLY: 以只写的方式打开
os.O_RDWR : 以读写的方式打开
os.O_NONBLOCK: 打开时不阻塞
os.O_APPEND: 以追加的方式打开
os.O_CREAT: 创建并打开一个新文件
os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
os.O_EXCL: 如果指定的文件存在，返回错误
os.O_SHLOCK: 自动获取共享锁
os.O_EXLOCK: 自动获取独立锁
os.O_DIRECT: 消除或减少缓存效果
os.O_FSYNC : 同步写入
os.O_NOFOLLOW: 不追踪软链接
mode -- 类似 chmod()。

返回值
返回新打开文件的描述符。


os.openpty() 方法用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

语法
openpty()方法语法格式如下：

os.openpty()
参数
无
返回值
返回文件描述符对，主从。


os.pathconf() 方法用于返回一个打开的文件的系统配置信息。

Unix 平台下可用。

语法
fpathconf()方法语法格式如下：

os.fpathconf(fd, name)
参数
fd -- 文件描述符

name -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。

返回值
返回文件的系统信息。


os.pipe() 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写。

语法
pipe()方法语法格式如下：

os.pipe()
参数
无

返回值
返回文件描述符对。


os.popen() 方法用于从一个命令打开一个管道。

在Unix，Windows中有效

语法
popen()方法语法格式如下：

os.popen(command[, mode[, bufsize]])
参数
command -- 使用的命令。

mode -- 模式权限可以是 'r'(默认) 或 'w'。

bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。

返回值
返回一个文件描述符号为fd的打开的文件对象

os.read() 方法用于从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。

在Unix，Windows中有效

语法
read()方法语法格式如下：

os.read(fd,n)
参数
fd -- 文件描述符。

n -- 读取的字节。

返回值
返回包含读取字节的字符串


os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。

在Unix, Windows中有效

语法
remove()方法语法格式如下：

os.remove(path)
参数
path -- 要移除的文件路径

返回值
该方法没有返回值

os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。

语法
removedirs()方法语法格式如下：

os.removedirs(path)
参数
path -- 要移除的目录路径

返回值
该方法没有返回值


os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

语法
rename()方法语法格式如下：

os.rename(src, dst)
参数
src -- 要修改的目录名

dst -- 修改后的目录名

返回值
该方法没有返回值

os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。

语法
rmdir()方法语法格式如下：

os.rmdir(path)
参数
path -- 要删除的目录路径

返回值
该方法没有返回值


os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。

语法
stat()方法语法格式如下：

os.stat(path)
参数
path -- 指定路径

返回值
stat 结构:

st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。


os.stat_float_times() 方法用于决定stat_result是否以float对象显示时间戳。

语法
stat_float_times()方法语法格式如下：

os.stat_float_times([newvalue])
参数
newvalue -- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。

返回值
返回 True 或 False。


os.statvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息。

语法
statvfs()方法语法格式如下：

os.statvfs([path])
参数
path -- 文件路径。

返回值
返回的结构:

f_bsize: 文件系统块大小

f_frsize: 分栈大小

f_blocks: 文件系统数据块总数

f_bfree: 可用块数

f_bavail:非超级用户可获取的块数

f_files: 文件结点总数

f_ffree: 可用文件结点数

f_favail: 非超级用户的可用文件结点数

f_fsid: 文件系统标识 ID

f_flag: 挂载标记

f_namemax: 最大文件长度


os.symlink() 方法用于创建一个软链接。

语法
symlink()方法语法格式如下：

os.symlink(src, dst)
参数
src -- 源地址。

dst -- 目标地址。

返回值
该方法没有返回值。


os.tcgetpgrp() 方法用于回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组。

语法
tcgetpgrp()方法语法格式如下：

os.tcgetpgrp(fd)
参数
fd -- 文件描述符。

返回值
该方法返回进程组。


os.tcsetpgrp() 方法用于设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

可用系统: Unix。
语法
tcsetpgrp()方法语法格式如下：

os.tcsetpgrp(fd, pg)
参数
fd -- 文件描述符。

pg -- 关联的进程组。

返回值
该方法没有返回值。


os.ttyname() 方法用于返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

语法
ttyname()方法语法格式如下：

os.ttyname(fd)
参数
fd -- 文件描述符

返回值
返回一个字符串，它表示与文件描述符fd 关联的终端设备。


os.unlink() 方法用于删除文件,如果文件是一个目录则返回一个错误。

语法
unlink()方法语法格式如下：

os.unlink(path)
参数
path -- 删除的文件路径

返回值
该方法没有返回值。



os.utime() 方法用于设置指定路径文件最后的修改和访问时间。

在Unix，Windows中有效。

语法
utime()方法语法格式如下：

os.utime(path, times)
参数
path -- 文件路径

times -- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。

返回值
该方法没有返回值。

os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下。

在Unix，Windows中有效。

语法
walk()方法语法格式如下：

os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
参数
top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。

topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。

onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。

followlinks -- 设置为 true，则通过软链接访问目录。

返回值
该方法没有返回值。


os.write() 方法用于写入字符串到文件描述符 fd 中. 返回实际写入的字符串长度。

在Unix中有效。

语法
write()方法语法格式如下：

os.write(fd, str)
参数
fd -- 文件描述符。

str -- 写入的字符串。

返回值
该方法返回写入的实际位数。


os.path 模块主要用于获取文件的属性。

以下是 os.path 模块的几种常用方法：

方法	说明
os.path.abspath(path)	返回绝对路径
os.path.basename(path)	返回文件名
os.path.commonprefix(list)	返回list(多个路径)中，所有path共有的最长的路径
os.path.dirname(path)	返回文件路径
os.path.exists(path)	路径存在则返回True,路径损坏返回False
os.path.lexists	路径存在则返回True,路径损坏也返回True
os.path.expanduser(path)	把path中包含的"~"和"~user"转换成用户目录
os.path.expandvars(path)	根据环境变量的值替换path中包含的"$name"和"${name}"
os.path.getatime(path)	返回最近访问时间（浮点型秒数）
os.path.getmtime(path)	返回最近文件修改时间
os.path.getctime(path)	返回文件 path 创建时间
os.path.getsize(path)	返回文件大小，如果文件不存在就返回错误
os.path.isabs(path)	判断是否为绝对路径
os.path.isfile(path)	判断路径是否为文件
os.path.isdir(path)	判断路径是否为目录
os.path.islink(path)	判断路径是否为链接
os.path.ismount(path)	判断路径是否为挂载点
os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
os.path.normcase(path)	转换path的大小写和斜杠
os.path.normpath(path)	规范path字符串形式
os.path.realpath(path)	返回path的真实路径
os.path.relpath(path[, start])	从start开始计算相对路径
os.path.samefile(path1, path2)	判断目录或文件是否相同
os.path.sameopenfile(fp1, fp2)	判断fp1和fp2是否指向同一文件
os.path.samestat(stat1, stat2)	判断stat tuple stat1和stat2是否指向同一个文件
os.path.split(path)	把路径分割成 dirname 和 basename，返回一个元组
os.path.splitdrive(path)	一般用在 windows 下，返回驱动器名和路径组成的元组
os.path.splitext(path)	分割路径，返回路径名和文件扩展名的元组
os.path.splitunc(path)	把路径分割为加载点与文件
os.path.walk(path, visit, arg)	遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
os.path.supports_unicode_filenames	设置是否支持unicode路径名


Python有两种错误很容易辨认：语法错误和异常。

>>>while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")
try语句按照如下方式工作；

首先，执行try子句（在关键字try和关键字except之间的语句）
如果没有异常发生，忽略except子句，try子句执行后结束。
如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。

处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

except (RuntimeError, TypeError, NameError):
        pass
最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

Python 使用 raise 语句抛出一个指定的异常。例如:

>>>raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出


'''


import sys
 
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

'''
try:
    raise NameError("HiThere")
except NameError:
    print('An exception flew by !')
    raise


你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承


try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为


'''



class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred,value:',e.value)

'''
try:
    raise KeyboardInterrupt
    
finally:
    print('goodbye,world!')

'''