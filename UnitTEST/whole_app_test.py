import os, sys

from UnitTEST.functions_test import algorithm_check

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))
from mainalgo import *
import unittest
from functions_test import *
from random import randint
from cut_box import *
import copy

class algorithm_test(unittest.TestCase):
    def copy_box_list(self, list):
        copy_list = []
        for i in list:
            copy_list.append(i)
        return copy_list

    def test_funkcji_algorytm(self):
        table = []
        ile_pudelek = randint(2,10)
        for j in range(ile_pudelek):
            table.append(box3D.random())
        table2 = self.copy_box_list(table)
        stack = boxStack()
        stack2 = boxStack()
        stack.extend(table)
        stack2.extend(table2)
        drzewo = tree()
        stack_temp = []
        algorithm().algorytm(stack, drzewo)
        for i in drzewo.ret_boxes():
            print(i.interval_x, i.interval_y, i.interval_z)
            stack_temp.append(myInterval().box_uncut(i))

        for i in stack_temp:
            print(i.interval_x, i.interval_y, i.interval_z)
        self.assertEqual(True, algorithm_check().evaluate(stack2.get_stack(), stack_temp))




if __name__ == '__main__':
    unittest.main()

