# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 10:10
# @Project:  Python
# @FileName: 39_file_reader.py

# 1 从文件中读取数据

# 1-1 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# print(contents)
print(contents.rstrip())

# 1-2 文件路径
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# 1-3 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 1-4 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print(lines)

# 1-5 使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
