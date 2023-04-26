# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-25 16:25:05 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-25 16:40:37 

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3]) 
print(players[1:4]) 
print(players[:4]) 
print(players[2:]) 
print(players[-3:]) 
print("Here are the first three players on my team:") 
for player in players[:3]: 
    print(player.title()) 

# 复制列表需要通过切片操作来完成，friend_foods 是一个新的列表，所以有两个实际列表
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 
my_foods.append('cannoli') 
friend_foods.append('ice cream') 
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# 如果没有使用切片操作，那么只是将 friend_foods 指向了 my_foods 这个列表，实际列表只有一个
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)