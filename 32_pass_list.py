# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 14:34
# @Project:  Python
# @FileName: 32_pass_list.py

# 4 传递列表
def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 4-1 在函数中修改列表
def print_models(unprinted_design, completed_model):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_model.append(current_design)


def show_completed_models(completed_model):
    """显示打印好的所有模型。"""
    print("\nThe following models have been printed:")
    for completed_model in completed_model:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
print(unprinted_designs)
print(completed_models)

# 4-2 禁止函数修改列表，使用切片创建列表的副本
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)
