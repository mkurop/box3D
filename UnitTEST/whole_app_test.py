import os, sys
sys.path.insert(0, os.path.abspath('..'))
from mainalgo import * 
import unittest
from random import randint

class algorithm_check(unittest.TestCase):
        
   
    @staticmethod
    def funkcja_uniwersalna(box_list, tree):
        for j in box_list:
            if tree.tree.count((j.interval_x.lower,  j.interval_y.lower, j.interval_z.lower, j.interval_x.upper, j.interval_y.upper,  j.interval_z.upper)) > 0:
                return False
            else:
                continue
        return True


    def test_funkcji_algorytm(self):
        ile_pudelek = randint(2,10)
        drzewo = tree()
        table = []
        stack = boxStack()
        stack2 = boxStack()
        for j in range(ile_pudelek):
            table.append(box3D.random())
        table2 = table[:]
        stack.extend(table)
        stack2.extend(table2)
        drzewo = algorithm.algorytm(stack2, drzewo).tree.tree
        self.assertEqual(True, self.funkcja_uniwersalna(stack.get_stack(), drzewo))




if __name__ == '__main__':
    unittest.main()

