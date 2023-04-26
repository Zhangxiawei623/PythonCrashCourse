# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-25 17:03:21 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-25 17:18:42 

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
    print(dimension)
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 练习 4-13 自助餐
