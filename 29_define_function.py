# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 11:10
# @Project:  Python
# @FileName: 29_define_function.py

# 1 定义函数
def greet_user():
    # 显示简单的问候语。
    print("Hello!")


greet_user()


# 1-1 向函数传递信息
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")


greet_user('jesse')

