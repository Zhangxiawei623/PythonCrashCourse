# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-24 10:20:53 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-24 10:27:51 

# 整数 
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

print(2 + 3 * 4)
print((2 + 3) * 4)

# 浮点数 
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

# 将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除 
print(4 / 2)
# 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数 
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

# Python3.6 及以上版本支持在数字中加入下划线以方便阅读，下划线的位置可以任意 
universe_age = 14_000_000_000
print(universe_age)
# 可以同时给多个变量赋值，只要变量和值的个数相同，Python就能正确地将它们关联起来 
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# 常量，在 Python 中一般使用全大写来标识常量，常量在程序中实际是可以改变的，但是我们不应该去改变它 
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
MAX_CONNECTIONS = 4000
print(MAX_CONNECTIONS)

# 练习 2-8 
print(5 + 3)
print(15 - 7)
print(2 * 4)
print(32 / 4)
# 练习 2-9 
favorite_number = 36
message = f"Hello, my favorite number is {favorite_number}!"
print(message)
