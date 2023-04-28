# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-27 11:28
# @Project:  Python
# @FileName: 30_pass_parameters.py

# 2 传递实参

# 2-1 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')

# 2-2 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# 2-3 默认值
def describe_pet1(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet1(pet_name='willie')
describe_pet1('willie')

# 2-4 等效的函数调用
# 一条名为Willie的小狗。
describe_pet1('willie')
describe_pet1(pet_name='willie')
# 一只名为Harry的仓鼠。
describe_pet1('harry', 'hamster')
describe_pet1(pet_name='harry', animal_type='hamster')
describe_pet1(animal_type='hamster', pet_name='harry')

# 2-5 避免实参错误
# describe_pet()    TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
