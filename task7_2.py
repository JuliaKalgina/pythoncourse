import unittest
import random

class NumbersTest(unittest.TestCase):

    def test_even(self):
        gen = [random.random(), random.random(), random.random()]
        print(gen)
        for number in gen:
            with self.subTest(i=number):
                self.assertEqual(number >= 0.5, True)
                print(number)
        print(gen)

test = NumbersTest()
test.test_even()
