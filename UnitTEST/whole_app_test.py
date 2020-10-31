import os, sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))
from mainalgo import * 
import unittest
import functions_test 
from random import randint

class algorithm_check(unittest.TestCase):
    def test_funkcji_algorytm(self):
        table = []
        ile_pudelek = randint(2,10)
        table2 = table[:]
        for j in range(ile_pudelek):
            table.append(box3D.random())
        tester = functions_test.algorithm_check()
        stack = boxStack()
        stack2 = boxStack()
        stack.extend(table)
        stack2.extend(table2)
        drzewo = tree()
        self.assertEqual(True, tester.evaluate(stack2, <<<FUNKCJA KLASY BOX3D ZWRACAJĄCA PUDEłKA>>>))




if __name__ == '__main__':
    unittest.main()

