# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 09:41
# @Project:  Python
# @FileName: 37_my_car.py

# 4 导入类

# 4-1 导入单个类
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 4-2 在一个模块中存储多个类
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_mileage()

# 4-3 从一个模块中导入多个类
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# 4-4 导入整个模块
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# 4-5 导入模块中的所有类 (不推荐)
# from module_name import *

# 4-5 在一个模块中导入另一个模块
