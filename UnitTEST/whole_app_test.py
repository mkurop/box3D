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
        table_copy = self.copy_box_list(table)
        stack = boxStack()
        stack2 = boxStack()
        stack.extend(table)
        stack2.extend(table_copy)
        drzewo = tree()
        table_out = []
        algorithm().algorytm(stack, drzewo)
        for i in drzewo.ret_boxes():
            print(i.interval_x, i.interval_y, i.interval_z)
            x1, x2 = int(round(i.interval_x.lower)), int(round(i.interval_x.upper))
            y1, y2 = int(round(i.interval_y.lower)), int(round(i.interval_y.upper))
            z1, z2 = int(round(i.interval_z.lower)), int(round(i.interval_z.upper))
            table_out.append(box3D(closed(x1, x2), closed(y1, y2), closed(z1, z2)))

        for i in table_out:
            print(i.interval_x, i.interval_y, i.interval_z)
        self.assertEqual(True, algorithm_check().evaluate(stack2.get_stack(), table_out, 10000))




if __name__ == '__main__':
    unittest.main()

