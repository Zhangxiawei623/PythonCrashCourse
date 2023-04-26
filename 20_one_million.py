# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-25 15:52:39 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-25 16:21:07 

# 练习 4-3 数到20
for value in range(1, 21) :
    print(value, end = " ") 
print(" (打印数字 1~20)") 

# 练习 4-4 一百万
# for value in range(1, 1_000_001) : 
#     if value % 25 == 0 : 
#         print(value) 
#     else : 
#         print(value, end=' ') 

# 练习 4-5 一百万求和
# numbers = list(range(1, 1_000_001)) 
# print(max(numbers)) 
# print(min(numbers)) 
# print(sum(numbers)) 

# 练习 4-6 奇数
for value in range(1, 20, 2) : 
    print(value, end=' ') 
print(" (1~20 的奇数)") 

# 练习 4-7 3的倍数
for value in range(3, 31, 3) : 
    print(value, end=' ') 
print(" (3~30 能被3整除的数)") 

# 练习 4-8 立方
numbers = [] 
for value in range(1, 11) : 
    numbers.append(value**3) 
print(numbers) 
for number in numbers :
    print(number, end=' ') 
print(" (1~10 的立方)")

# 练习 4-9 立方解析
numbers1 = [value**3 for value in range(1, 11)] 
print("立方解析结果:",numbers1)  