import unittest

def mySort(num):
    if len(num) == 1:
        return num
    if num[0] > num[1]:
        tmp = num[0]
        num[0] = num[1]
        num[1] = tmp
    return num

class test_MySort(unittest.TestCase):
    def test_oneElements1(self):
        self.assertEquals([0],mySort([0]))
    def test_oneElements2(self):
        self.assertEquals([1],mySort([1]))
    def test_twoElements(self):
        self.assertEquals([1,2], mySort([1,2]))
    def test_twoElements2(self):
        self.assertEquals([1,2], mySort([2,1]))












