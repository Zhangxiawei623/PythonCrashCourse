# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-26 11:46:01 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-27 09:59:52 

# 1 函数 input() 的工作原理
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# 1-1 编写清晰的程序
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
# 1-2 使用 int() 来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
# 1-3 求模运算符
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
