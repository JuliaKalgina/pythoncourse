import unittest


def dividers(a):
    dr = []
    for i in range(a):
        if a % (i + 1) == 0:
            dr.append(i + 1)
    return dr


def check_if_same(a, b):
    if type(a) == type(b):
        return True
    else:
        return False


def degree(a, b):
    return a ** b


def sq_degree(a):
    sqs = []
    i = 1
    while i ** 2 <= a:
        sqs.append(i ** 2)
        i += 1
    return sqs


class TestTest(unittest.TestCase):

    def test_check_if_same_true(self):
        self.assertTrue(check_if_same(-45692.76, 25j))

    def test_check_if_same_false(self):
        self.assertFalse(check_if_same(81e2, 3.0))

    def test_dividers_in(self):
        self.assertIn(9300, dividers(98765))

    def test_dividers_notin(self):
        self.assertNotIn(7101, dividers(34598))

    def test_exp_greater(self):
        self.assertGreater(degree(5, 4), degree(4, 5))

    def test_exp_less(self):
        self.assertLess(degree(4, 5), degree(5, 4))

    def test_squares(self):
        self.assertCountEqual(sq_degree(123), sq_degree(125))


if __name__ == '__main__':
    unittest.main()
