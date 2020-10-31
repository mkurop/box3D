import math
import os, sys
sys.path.insert(0, os.path.abspath('..'))
from mainalgo import * 
from portion import closed
import unittest
from random import randint
import functions_test as ft

class tree_test(tree):
    def __init__(self):
        '''Tworzenie drzewa'''
        self.properties = rtree.index.Property()
        self.properties.dimension = 3
        self.tree = rtree.index.Index('3d_index_test', properties=self.properties)    

class testing(unittest.TestCase):
    algo_test = algorithm()
    def setUp(self):
        self.stack = boxStack()
        self.stack_2 = boxStack()
        self.tree1 = tree()
        self.tree2 = tree_test()
    def ready_vars(self):
        table = []
        ile_pudelek = randint(1, 6)
        for i in range(ile_pudelek):
            x_l = randint(1, 1000)
            y_l = randint(1, 1000)
            z_l = randint(1, 1000)
            x_h = randint(1 + x_l, 1000 + x_l)
            y_h = randint(1 + x_l, 1000 + x_l)
            z_h = randint(1 + x_l, 1000 + x_l)
            x, y, z = closed(x_l, x_h), closed(y_l, y_h), closed(z_l, z_h)
            table.append(box3D(x, y, z))
        self.stack_2.set_stack(table.copy)
        self.stack.set_stack(table.copy)
        return ile_pudelek  
		
    def rotate_and_execute(self, box1, box2):
        sign = signatures()
        spl = ft.split()
        idx_sign = sign.get_signatures_triple(box1, box2)
        sort, in2sorted, sorted2in = sign.my_sort(idx_sign)
        tri_sign, tri_sign_i = sign.sort_signatures(box1, box2, in2sorted)
        split_sign = spl.split(tuple(sort), tri_sign, tri_sign_i)
        table = sign.ret_original_order(split_sign, sorted2in)
        return table
    
    
    @staticmethod
    def funkcja_uniwersalna(Q, tree):
        #obiekt klasy myInterval
        my_int = myInterval()
        #zmienna potrzebna do wprowadzania pudełka w unikalne miejsce do drzewa
        iD = 0
        #pętla działa dopóki stos nie zostanie pusty
        while not len(Q.get_stack()) == 0:
            #zdjęcie ostatniego pudełka ze stosu i przycięcie go
            q = Q.pop()
            q = my_int.box_cut(q)
            if tree.tree.count((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper)) > 0:
                i = list(tree.tree.intersection((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper), objects=True))[0]
                inter = [i.object.interval_x, i.object.interval_y, i.object.interval_z]
                j = box3D(inter[0], inter[1], inter[2])
                q = my_int.box_uncut(q)
                j = my_int.box_uncut(j)
                #cofnięcie przycięcia dla pudełek które mają być rozbite
                Q.extend(algorithm().rotate_and_execute(q, j))
                #wprowadzenie wyniku rozbicia na stos
                tree.tree.delete(i.id, (i.bbox[0], i.bbox[1], i.bbox[2], i.bbox[3], i.bbox[4], i.bbox[5]))
                #usunięcie starego pudełka z drzewa
            else:
                tree.tree.add(iD, (q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper), q)
                #dodanie nowego pudełka do drzewa i zwiększenie zmiennej iD o 1
                iD += 1

    def test_funkcji_algorytm(self):
        ile_pudelek = self.ready_vars()
        self.assertEqual(testing.funkcja_uniwersalna(self.stack_2, self.tree2),algorithm.algorytm(self.stack, self.tree1))




if __name__ == '__main__':
    unittest.main()

