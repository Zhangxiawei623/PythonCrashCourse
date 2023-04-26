# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-24 16:42:17 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-24 17:16:03 

cars = ['bmw', 'audi', 'toyota', 'subaru'] 
# 方法 sort() 永久性地修改列表元素的排列顺序 
cars.sort() 
print(cars) 
# 当参数 reverse=True 时，将按与字母顺序相反的顺序排列列表元素 
cars.sort(reverse=True) 
print(cars) 

# 使用函数 sorted() 对列表临时排序 
cars1 = ['bmw', 'audi', 'toyota', 'subaru'] 
print("Here is the original list:") 
print(cars1) 
print("\nHere is the sorted list:") 
print(sorted(cars1)) 
print("\nHere is the original list again:") 
print(cars1) 

# 使用方法 reverse() 反转列表元素的排列顺序，再次调用可以还原元素的排列顺序
cars2 = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars2) 
cars2.reverse() 
print(cars2) 

# 使用函数 len() 可快速获悉列表的长度 
print(len(cars)) 

motorcycles = ['honda', 'yamaha', 'suzuki'] 
# print(motorcycles[3])  	IndexError: list index out of range
print(motorcycles[-1]) 
motorcycles = [] 
# print(motorcycles[-1]) 	IndexError: list index out of range
