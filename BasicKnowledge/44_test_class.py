# -*- coding: utf-8 -*-
# @Author:   Zhangxiawei
# @Date:     2023-04-28 15:16
# @Project:  Python
# @FileName: 44_test_class.py
import unittest


# 2 测试类

# 2-1 各种断言方法
# assertEqual(a, b)         核实 a == b
# assertNotEqual(a, b)      核实 a != b
# assertTrue(x)             核实 x == True
# assertFalse(x)            核实 x == False
# assertIn(item, list)      核实 item 在 list 中
# assertNotIn(item, list)   核实 item 不在 list 中

# 2-2 一个要测试的类
class AnonymousSurvey:
    """收集匿名调查问卷的答案。"""

    def __init__(self, question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷。"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷。"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷。"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


# 定义一个问题，并创建一个调查。
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# 显示问题并存储答案。
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# 显示调查结果。
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


# 2-3 测试 AnonymousSurvey 类
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试。"""

# 2-4 方法setUp()，方法setUp() 让我们只需创建这些对象一次，就能在每个测试方法中使用。
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用。
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储。"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储。"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

