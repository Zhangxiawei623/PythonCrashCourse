# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 16:06
# @Project:  Python
# @FileName: pizza.py

def make_pizza(size, *toppings):
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")