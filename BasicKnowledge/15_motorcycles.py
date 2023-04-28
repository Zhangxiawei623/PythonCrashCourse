# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-24 15:41:34 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-24 16:25:33 

# 创建列表
motorcycles0 = ['honda', 'yamaha', 'suzuki']
print(motorcycles0)

# 修改列表元素
motorcycles0[0] = 'ducati'
print(motorcycles0)

# 在列表末尾添加元素
motorcycles0.append('honda')
print(motorcycles0)
motorcycles1 = []
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)

# 在列表中间插入元素
motorcycles1.insert(0, 'ducati')
print(motorcycles1)

# 删除列表元素并且不再以任何形式使用被删除元素(根据元素所在位置)
del motorcycles0[0]
print(motorcycles0)
del motorcycles1[2]
print(motorcycles1)
# 删除列表元素后还需使用被删除元素(根据元素所在位置)
motorcycles2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles2)
last_owned = motorcycles2.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles2.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
popped_motorcycle = motorcycles0.pop()
print(popped_motorcycle)
# 使用 remove() 方法在列表中删除元素时，一次只能删除第一个匹配的(根据元素值删除)
motorcycles3 = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles3) 
# motorcycles3.remove('ducati') 
print(motorcycles3)
too_expensive = 'ducati'
motorcycles3.remove(too_expensive)
print(motorcycles3)
print(f"\nA {too_expensive.title()} is too expensive for me.")
