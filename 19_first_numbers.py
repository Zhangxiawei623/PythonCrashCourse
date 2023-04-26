# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-25 15:25:36 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-25 16:24:28 

for value in range(6): 
    print(value) 

numbers = list(range(1, 6)) 
print(numbers) 

even_numbers = list(range(2, 11, 2)) 
print(even_numbers) 

squares = [] 
for value in range(1, 11): 
    square = value ** 2 
    squares.append(square) 

print(squares) 

print(min(squares)) 
print(max(squares)) 
print(sum(squares)) 

# 列表解析
squares1 = [value**2 for value in range(1, 13)] 
print(squares1) 

