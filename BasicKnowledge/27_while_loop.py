# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 10:19
# @Project:  Python
# @FileName: 27_while_loop.py

# 2 while 循环简介
# 2-1 使用 while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 2-2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program1. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
# 2-3 使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program2. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# 2-4 使用break 退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1      # 千万不能遗漏
