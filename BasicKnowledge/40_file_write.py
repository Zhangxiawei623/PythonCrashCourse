# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 11:19
# @Project:  Python
# @FileName: 40_file_write.py

# 2 写入文件

# 2-1 写入空文件 (写入模式：‘w’,读取模式：‘r’,附加模式：‘a’,读写模式：’r+‘)
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# 2-2 写入多行  (注意：Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 str() 将其转换为字符串格式。)
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 2-3 附加到文件
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")