# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 11:28
# @Project:  Python
# @FileName: 41_exception.py

# 3 异常

# 3-1 处理 ZeroDivisionError 异常
# print(5/0)      ZeroDivisionError: division by zero

# 3-2 使用try-except 代码块
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 3-3 使用异常避免崩溃
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    # 3-4 else 代码块中存放依赖 try 代码块成功执行的代码
    else:
        print(answer)

# 3-5 处理 FileNotFoundError 异常
filename = 'alice.txt'
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# 3-6 分析文本
title = "Alice in Wonderland"
print(title.split())
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # 计算该文件大致包含多少个单词。
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


# 3-7 使用多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词。"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word = content.split()
        num_word = len(word)
        print(f"The file {filename} has about {num_word} words.")


filename = 'alice.txt'
count_words(filename)
filenames = ['alice.txt', 'siddhartha.txt', 'programming.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# 3-8 静默失败
try:
    print(5 / 0)
except ZeroDivisionError:
    pass

# 3-9 决定报告哪些错误
# 如果用户知道要分析哪些文件，他们可能希望在有文件却没有分析时出现一条消息来告知原因。
