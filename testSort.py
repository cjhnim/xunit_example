import unittest

def mySort(numbers):
    if len(numbers) == 1:
        return numbers
    if len(numbers) >= 2 and numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
    if len(numbers) >= 3 and numbers[1] > numbers[2]:
        numbers[1], numbers[2] = numbers[2], numbers[1]
    return numbers

class test_MySort(unittest.TestCase):
    def test_oneElementsZero(self):
        self.assertEquals([0],mySort([0]))
    def test_oneElementsOne(self):
        self.assertEquals([1],mySort([1]))
    def test_twoElements(self):
        self.assertEquals([1,2], mySort([1,2]))
    def test_twoElementsSwap(self):
        self.assertEquals([1,2], mySort([2,1]))
    def test_threeElements1(self):
        self.assertEquals([1,2,3], mySort([1,2,3]))
    def test_threeElements2(self):
        self.assertEquals([1,2,3], mySort([2,1,3]))
    def test_threeElements_swap(self):
        self.assertEquals([1,2,3], mySort([3,2,1]))










