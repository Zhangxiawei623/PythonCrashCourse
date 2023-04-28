# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 10:02
# @Project:  Python
# @FileName: 38_standard_library.py

# 5 Python 标准库
from random import randint, choice

print(randint(1, 6))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)
