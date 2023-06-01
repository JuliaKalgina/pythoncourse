import os
import unittest
import shutil


def direct(dirt):
    os.makedirs(dirt)
    with open(dirt + r'\texttt.txt', 'w') as f:
        random_speech = 'Sator arepo tenet opera rotas'
        f.write(random_speech)


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        direct(r'C:\Users\User\PycharmProjects\pythoncourse\foldy')
        with open(r'C:\Users\User\PycharmProjects\pythoncourse\foldy\texttt.txt', 'r') as ff:
            tx = ff.read()
            self.assertEqual('Sator arepo tenet opera rotas', tx)
            self.assertTrue(tx)

    def tearDown(self):
        shutil.rmtree(r'C:\Users\User\PycharmProjects\pythoncourse\foldy')

test = TestStringMethods()
test.setUp()
test.tearDown()
