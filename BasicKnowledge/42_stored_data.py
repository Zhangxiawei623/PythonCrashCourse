# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 14:41
# @Project:  Python
# @FileName: 42_stored_data.py

# 4 存储数据

# 4-1 使用 json.dump() 和 json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# 4-2 保存和读取用户生成的数据
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")


# 4-3 重构，每个函数都应执行单一而清晰的任务。
def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其姓名。"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
