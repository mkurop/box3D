import os, sys
from functions_test import algorithm_check

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
        print("Ile pudełek?")
        ile_pudelek = int(input())
        for j in range(ile_pudelek):
            print("Podaj współrzędne pudełka ", j +1, " kolejność x lower, x upper, y lower, y upper, z lower, z upper, "
                                                      "po każdej współrzędnej wciśnij enter")
            print("Przykład 2 enter 4 enter 5 enter 10 enter 3 enter 12 enter to pudełko o współrzędnych x=(2,4) "
                  "y=(5,10) z=(3,12)")
            x1, x2, y1, y2, z1, z2 = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
            table.append(box3D.factory(x1, y1, z1, x2, y2, z2))
        table_copy = self.copy_box_list(table)
        stack = boxStack()
        stack.extend(table)
        drzewo = tree()
        algorithm().algorytm(stack, drzewo)
        self.assertEqual(True, algorithm_check().evaluate(table_copy, drzewo.ret_boxes(), 10000))


if __name__ == '__main__':
    unittest.main()

