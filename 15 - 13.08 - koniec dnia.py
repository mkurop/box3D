# import bibliotek
import numpy as np
import os
import rtree
from portion import closed
from math import ceil, floor
import itertools
# usuwanie plików z poprzedniego działania programu
try:
    os.remove('3d_index.idx')
    os.remove('3d_index.dat')
except:
    pass
class box3D:  # klasa pudełka 3-wymiarowego
    def __init__(self, interval_x, interval_y, interval_z):
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.interval_z = interval_z
    def get_interval_x(self):
        return self.interval_x
    def get_interval_y(self):
        return self.interval_y
    def get_interval_z(self):
        return self.interval_z

    @staticmethod
    def factory(x1, y1, z1, x2, y2, z2):
        return box3D(closed(x1, x2), closed(y1, y2), closed(z1, z2))
class boxStack:
    def __init__(self):
        self.stack = []
    def get_stack(self):
        return self.stack

    def set_stack(self, new_stack):
        self.stack = new_stack
    def append(self, added):
        self.stack.append(added)
    def pop(self):
        return self.stack.pop()

class tree:
    def __init__(self):
        # tworzenie drzewa
        self.properties = rtree.index.Property()
        # ustawienia drzewa
        self.properties.dimension = 3
        self.tree = rtree.index.Index('3d_index', properties=self.properties)
    def get_tree(self):
        return self.tree
    def set_tree(self, new_tree):
        self.tree = new_tree

class algorytm:
    def __init__(self, Q, tree):
        self.Q = Q
        self.tree = tree
        self.q = []
    def divide_in(self, int1, int2):
        return int1 | int2
    def divide_half_out(self, int1, int2):
        up, low = (int1.upper, int2.upper), (int1.lower, int2.lower)
        if int2.lower==int1.lower:
            return closed(min(low), min(up)), closed(min(up), max(up))
        else:
            return closed(min(low), max(low)), closed(max(low), max(up))
    def divide_out(self, int1, int2):
        inter = int1 & int2
        return int1 - (inter), inter ,int2 - (inter)
    def is_in(self, interval1, interval2):
        return True if interval1 & interval2 == min(interval2, interval1) else False
    def is_equal(self, interval1, interval2):
        return True if interval1==interval2 else False
    def is_out(self, interval1, interval2):
        return True if (interval1 & interval2)!=(interval1|interval2) and any(interval1&interval2)  else False
    '''
    def merge(self, int1, box_x, box_y):
        all = [int1.upper, box_x.upper, box_y.upper, int1.lower, box_x.lower, box_y.lower]
        all.sort()
        one, two, thr = closed(all[0], all[1]), closed(all[2], all[3]), closed(all[4], all[5])
        return one, two - one | thr, thr - two
    '''
    def is_separate(self, int1, int2):
        return False if any(int1 & int2) else True
    def rozbijanie(self, q, i):
        if self.is_in(q, i):
            return self.divide_in(q,i)
        elif self.is_out(q, i):
            return self.divide_out(q,i)
        elif self.is_equal(q, i):
            return self.divide_half_out(q,i)
        elif self.is_separate(q, i):
            return q
    def rozbij(self, q, i):
        return self.rozbijanie(q.interval_x, i.interval_x), self.rozbijanie(q.interval_y, i.interval_y), self.rozbijanie(q.interval_z, i.interval_z)
    @staticmethod
    # początek funkcji głównej
    def algorytm(Q, tree):
        iD = 0
        # główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
        while not len(Q.get_stack()) == 0:
            # komenda pop
            q = Q.pop()
            print(q, Q)
            # sprawdzanie czy w drzewie pudełko q się przecina
            if any(tree.tree.intersection((q.interval_x.lower,q.interval_y.lower,q.interval_z.lower, q.interval_x.upper,q.interval_y.upper,q.interval_z.upper))):
                # zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                i = list(tree.tree.intersection((q.interval_x.lower, q.interval_x.upper,q.interval_y.lower, q.interval_y.upper, q.interval_z.lower, q.interval_z.upper), objects=True))[0]
                # dodanie na koniec zbioru Q "rozbitego" pudełka q
                Q.append(algorytm.rozbij(q, i))
            else:
                # w przeciwnym wypadku dodanie do drzewa nowego pudełka
                tree.tree.insert(iD, [q.interval_x.lower, q.interval_y.lower,q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper])
                # zwiększenie zmiennej iD
                iD += 1
        # wypisanie drzewa
        print(tree.tree.get_bounds())
        # zwrócenie drzewa
        return tree.get_tree()# zmienna, która wskazuje ile chcemy pudełek wprowadzić
###pudelka = int(input('\nIle pudełek?\n'))
Q = boxStack()
# pętla do wczytywania współrzędnych dla każdego pudełka i
'''
for i in range(pudelka):
    # (int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielonput()), int(input()), int(input()), ine spacją oraz przecinkiem: '))
    Q.append(box3D.factory(int(input("Podaj po jednej z sześciu współrzędnych pudełka oddzielonych enterem:\n")), \
                           int(input()), int(input()), int(input()), int(input()), int(input())))
algorytm.algorytm(Q, tree())
'''

'''TEST FUNKCJI'''
####Dokończyć
import unittest
class testing(unittest.TestCase):
    def setUp(self):
        self.we1 = [0, 1, 2, 5, 6, 7]
        self.we2 = [10, 20, 30, 44, 22, 31]
        self.we3 = [-2, 10, 3, 11, 13, 5]
        self.q = algorytm().box3D.factory(self.we1[0], self.we1[1],self.we1[2],self.we1[3],self.we1[4],self.we1[5])
        self.i = list(tree().tree.intersection((self.we1[0], self.we1[1],self.we1[2],self.we1[3],self.we1[4],self.we1[5]), objects=True))
        self.tree = tree()
    def test_funkcji_algorytm(self):
        self.assertTrue(algorytm().algorytm(tree().tree.insert(algorytm().box3D.factory(self.we2[0], self.we2[1],self.we2[2],self.we2[3],self.we2[4],self.we2[5])), self.tree) == tree().tree.insert(algorytm().box3D.factory(self.we2[0], self.we2[1],self.we2[2],self.we2[3],self.we2[4],self.we2[5])))
        self.assertTrue(algorytm().algorytm(self.q, self.tree) == tree().tree.insert(self.q))
    def test_funkcji_rozbij(self):
        self.assertTrue(algorytm().rozbij(self.q, self.i))
    def test_funkcji_rozbijanie(self):
        self.assertEqual(algorytm().rozbijanie(closed(self.we3[1], self.we3[4]),closed(self.we2[1], self.we2[4])), ([10, 12], [13,20], [20,22]))



if __name__ == '__main__':
    unittest.main()

