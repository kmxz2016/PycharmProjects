# coding=utf-8
import unittest
from my import mySum
from my import mySub

class Test(unittest,TestCase):
    def setUp(self):
        print("开始测试自动调用")

    def tearDown(self):
        print("结束测试自动调用")

    def test_mySum(self):
        self.assertEqual(mySum(1,5),6,"加法有误")
    def test_mySub(self):
        self.assertEqual(mySub(5,2),3,"减法有误")

if __name__ == "__main__":
    unittest.main()