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
    def factory(x1, x2, y1, y2, z1, z2):
        return box3D(closed(x1, x2), closed(y1, y2), closed(z1, z2))


class boxStack:
    def __init__(self):
        self.stack = []

    def get_stack(self):
        return self.stack

    def set_stack(self, new_stack):
        self.stack = new_stack


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
    def merge(self, int1, box_x, box_y):
        all = [int1.upper, box_x.upper, box_y.upper, int1.lower, box_x.lower, box_y.lower]
        all.sort()
        one, two, thr = closed(all[0], all[1]), closed(all[2], all[3]), closed(all[4], all[5])
        return one, two - one | thr, thr - two
    def is_separate(self, int1, int2):
        return False if any(int1 & int2) else True
    # funkcja rozbij
    def rozbij(self, q, i):

        #jeśli q jest instancją obiektu (pudełkiem kilkuwymiarowym)
        if isinstance(q) and isinstance(i):

        elif not isinstance(q) and not isinstance(i)
        #jeśli q jest interwałem (pudełkiem jednowymiarowym)
            if self.is_in(q, i):
                self.divide_in(q,i)
            elif self.is_out(q, i):
                self.divide_out(q,i)
            elif self.is_equal(q, i):
                self.divide_half_out(q,i)
        else:
        # rozbijanie pudełek

    @staticmethod
    # początek funkcji głównej
    def algorytm(Q, tree):
        iD = 0
        # główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
        while not len(Q.get_stack()) == 0:
            # komenda pop
            q = Q.get_stack().pop()
            print(q, Q)
            # sprawdzanie czy w drzewie pudełko q się przecina
            if any(list(tree.get_tree().intersection(q))):
                # zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                i = list(tree.get_tree().intersection(q))[0]
                # dodanie na koniec zbioru Q "rozbitego" pudełka q
                Q.extend(algorytm.rozbij(q.astype(np.int), i))
            else:
                # w przeciwnym wypadku dodanie do drzewa nowego pudełka
                tree.set_tree(tree.get_tree().insert(iD, list(int(num) for num in self.q)))
                # zwiększenie zmiennej iD
                iD += 1
        # wypisanie drzewa
        print(tree)
        # zwrócenie drzewa
        return tree


# zmienna, która wskazuje ile chcemy pudełek wprowadzić
pudelka = int(input('\nIle pudełek?\n'))
Q = boxStack()
# pętla do wczytywania współrzędnych dla każdego pudełka i
for i in range(pudelka):
    # (int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielonput()), int(input()), int(input()), ine spacją oraz przecinkiem: '))
    Q.set_stack(Q.get_stack().append(box3D.factory(int(input("Podaj po jednej z sześciu współrzędnych pudełka oddzielonych enterem:\n")), \
                           int(input()), int(input()), int(input()), int(input()), int(input()))))
algorytm.algorytm(Q, tree())
