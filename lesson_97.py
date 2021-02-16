# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
"""
# with open() 这种防止忘记关闭文件
with open('files/file_01.txt', 'w', encoding='utf-8') as f:   # 编码格式utf-8,不然写入中文打开会乱码,w写入文件会覆盖原有文件内容,a在末尾追加文件;不存在会新建文件
    s = input('输入字符:')
    while s != '#':
        f.write(s+'\n')
        s = input('输入字符:')
