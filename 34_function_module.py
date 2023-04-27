# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 15:03
# @Project:  Python
# @FileName: 34_function_module.py

# 6 将函数存储在模块中
# 6-1 导入整个模块，就可以通过 module_name.function_name() 语句使用任何一个函数
# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 6-2 导入特定的函数，使用这种语法时，调用函数时无须使用句点。
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 6-3 使用 as 给函数指定别名
# from pizza import make_pizza as mp
#
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 6-4 使用 as 给模块指定别名
# import pizza as p
#
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 6-5 导入模块中的所有函数
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 7 函数编写指南

# 7-1 应给函数指定描述性名称，且只在其中使用小写字母和下划线。

# 7-2 每个函数都应包含简要地阐述其功能的注释，应紧跟在函数定义后面，并采用文档字符串格式。

# 7-3 给形参指定默认值时，等号两边不要有空格。
