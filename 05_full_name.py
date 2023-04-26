# -*- coding: utf-8 -*- 
# @Author: Zhangxiawei 
# @Date:   2023-04-24 10:20:53 
# @Email:  myzhangxiawei@foxmail.com 
# @Last Modified time: 2023-04-24 10:25:17 

first_name = "ada" 
last_name = "lovelace" 
full_name = f"{first_name} {last_name}" 
print(full_name) 
print(f"Hello, {full_name.title()}!") 

message = f"Hello, {full_name.title()}!" 
print(message) 

# f 字符串在 Python3.6 之前的写法 
full_name = "{} {}".format(first_name, last_name) 
print(full_name.title()) 

print("Python") 
print("\tPython") 
print("Languages:\nPython\nC\nJavaScript") 
print("Languages:\n\tPython\n\tC\n\tJavaScript") 

favorite_language = 'python ' 
print(favorite_language) 
print(favorite_language.rstrip()) 
print(favorite_language) 
favorite_language = favorite_language.rstrip() 
print(favorite_language) 

favorite_language = ' python ' 
print(favorite_language) 
print(favorite_language.rstrip()) 
print(favorite_language.lstrip()) 
print(favorite_language.strip()) 
