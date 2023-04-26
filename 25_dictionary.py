# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-26 09:42:17 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-26 11:43:23 

# 1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 2 使用字典，字典是一系列键值对，每个键都与一个值相关联，你可使用键来访问相关联的值
# 2-1 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# 2-2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 2-3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# 2-4 修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
# 根据当前速度确定将外星人向右移动多远。
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
# 2-5 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# 2-6 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# 2-7 使用 get() 来访问值，其中第一个参数用于指定键，是必不可少的；第二个参数为指定的
#     键不存在时要返回的值，是可选的
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])      KeyError: 'points'
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 3 遍历字典
# 3-1 遍历所有键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# 3-2 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
# 3-3 按特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# 3-4 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    # 使用集合 set 剔除重复项
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
# 集合 set 的定义：使用一对花括号直接创建集合，并在其中用逗号分隔元素
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
# 集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的
# 很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。

# 4 嵌套
# 4-1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 创建一个用于存储外星人的空列表。
aliens = []
# 创建 30个绿色的外星人。
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 修改前 3个外星人的值 
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前 5个外星人。
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人。
print(f"Total number of aliens: {len(aliens)}")
# 4-2 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述所点的比萨。
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(topping)
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
# 4-3 在字典中存储字典
users = {
    'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton',},
    'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris',},
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")