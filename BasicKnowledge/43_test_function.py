# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 15:01
# @Project:  Python
# @FileName: 43_test_function.py

# 1 测试函数
def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

# 1-1 单元测试和测试用例
# 单元测试 用于核实函数的某个方面没有问题。
# 测试用例 是一组单元测试，它们一道核实函数在各种情形下的行为都符合要求。

# 1-2 可通过的测试
import unittest


class NamesTestCase(unittest.TestCase):
    """测试name_function.py。"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

# 1-3 未通过的测试


