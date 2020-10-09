#!/usr/bin/env python3
import os
import rtree
import math
from portion import *
import portion
import portion.const
# Notatka, bo nie przyjmuje nie zmienionego kodu
# usuwanie plików z poprzedniego działania programu
try:
    os.remove('3d_index.idx')
    os.remove('3d_index.dat')
except:
    pass


class box3D:

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

    def __contains__(self, num):
        return True if (num[0] in self.interval_x) & (num[1] in self.interval_y) & (num[2] in self.interval_z) else False

    def __ror__(self, num):
        x, y, z = num[0], num[1], num[2]
        is_on_border = x in set([self.interval_x.lower, self.interval_x.upper]) or y in set([self.interval_y.lower, self.interval_y.upper]) or z or set([self.interval_z.lower, self.interval_z.upper])
        is_inside_box = self.__contains__(num)
        return True if is_on_border & is_inside_box else False

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

    def extend(self, added):
        self.stack.extend(added)

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

def my_closed(lower, upper):
    return myInterval.from_atomic(portion.const.Bound.CLOSED, lower, upper, portion.const.Bound.CLOSED)

class myInterval(portion.Interval):
    eps = 1e-7

    @property
    def upper_eps(self):
        return self.upper + self.eps

    @property
    def upper_meps(self):
        return self.upper - self.eps

    @property
    def lower_eps(self):
        return self.lower + self.eps

    @property
    def lower_meps(self):
        return self.lower - self.eps

    @upper_eps.setter
    def upper_eps(self, value):
        self.upper_eps = value + self.eps

    @lower_meps.setter
    def lower_meps(self, value):
        self.lower_meps = value - self.eps

    @upper_eps.setter
    def upper_eps(self, value):
        self.upper_eps = value + self.eps

    @upper_meps.setter
    def upper_meps(self, value):
        self.upper_meps = value - self.eps

    @upper_eps.getter
    def upper_eps(self):
        return self.upper_eps

    @lower_meps.getter
    def lower_meps(self):
        return self.lower_meps

    @upper_eps.getter
    def upper_eps(self):
        return self.upper_eps

    @upper_meps.getter
    def upper_meps(self):
        return self.upper_meps

    def box_cut_execute(self, interval, i, int):
        if (i > 0) & (i + 1 < len(interval)):
            interval[i].int.replace(upper=interval[i].upper_meps)
            interval[i + 1].int.replace(lower=interval[i].lower_eps)
        elif i == 0:
            interval[i].int.replace(lower=interval[i].lower_eps)
        elif i + 1 == len(interval):
            interval[i].int.replace(upper=interval[i].upper_meps)

    def box_cut(self, boxes):
        new_boxes = []
        for i in range(len(boxes)):
            if i < len(boxes) & boxes[i].interval_x.upper == boxes[i + 1].lower:
                self.box_cut_execute(boxes, i, boxes[i].interval_x)
                pass
            elif i > 0 & boxes[i].interval_x.lower == boxes[i - 1]:
                self.box_cut_execute(boxes, i, boxes[i].interval_x)
                pass
            if i < len(boxes) & boxes[i].interval_y.upper == boxes[i + 1].lower:
                self.box_cut_execute(boxes, i, boxes[i].interval_y)
                pass
            elif i > 0 & boxes[i].interval_y.lower == boxes[i - 1]:
                self.box_cut_execute(boxes, i, boxes[i].interval_y)
                pass
            if i < len(boxes) & boxes[i].interval_z.upper == boxes[i + 1].lower:
                self.box_cut_execute(boxes, i, boxes[i].interval_z)
                pass
            elif i > 0 & boxes[i].interval_z.lower == boxes[i - 1]:
                self.box_cut_execute(boxes, i, boxes[i].interval_z)
                pass

            box = box3D(closed(boxes[i].interval_x, boxes[i].interval_y, boxes[i].interval_z))
            new_boxes.append(box)
        return new_boxes

class algorytm:
    my_int = myInterval()
    def oI_II_oI_II_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(float(box1.interval_x.lower), float(box1.interval_x.upper)), \
                     my_closed(float(box1.interval_y.lower), float(box1.interval_y.upper)), \
                     my_closed(float(box1.interval_z.lower), float(box1.interval_z.upper))
        x2, y2, z2 = my_closed(float(box2.interval_x.lower), float(box2.interval_x.upper)), \
                     my_closed(float(box2.interval_y.lower), float(box2.interval_y.upper)), \
                     my_closed(float(box2.interval_z.lower), float(box2.interval_z.upper))
        z2_cut, x1_cut, y2_cut = my_closed(float(z1.upper), float(z2.upper)), my_closed(float(x1.upper), float(x2.upper)), my_closed(float(y1.upper), float(y2.upper))
        table = myInterval().box_cut([(x1, y1, z1), (x1 & x2, y1 & y2, z2_cut), (x1_cut, y2 & y1, z2), (x2, y2_cut, z2)])
        table = myInterval.box_cut(table)
        return table

    def oI_II_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x2, y2 - y1, z2), box3D(x2 - x1, y2, z2)]
        return table

    def oI_II_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, closed(z2.lower, z1.lower)), box3D(x2, closed(y2.lower, y1.lower - self.eps), z2), box3D(closed(x1.upper + self.eps, x2.upper), closed(y1.lower, y2.upper), z2)]
        return table

    def oII_I_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x2, y2 - y1, z2), box3D(x2 - x1, y2, z2)]
        return table

    def iI_II_iI_II_iI_II(self, box1, box2):
        x, y, z = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x, y, z)]
        return table

    def iI_II_iI_II_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2, closed(y2.lower, y1.lower), z2), box3D(x2, closed(y1.upper, y2.upper), z2)]
        return table

    def iI_II_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 - x2, y2, z2), box3D(x2 - x1, y2, z2)]
        return table

    def iII_I_iII_I_iII_I(self, box1, box2):
        x, y, z = box1.interval_x, box1.interval_y, box1.interval_z
        table = [box3D(x, y, z)]
        return table

    def oII_I_iI_II_iI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1, z1)]
        return table

    def oI_II_oI_II_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2, y2 - y1, z2), box3D(x2 - x1, y2 & y1, z2)]
        return table

    def oI_II_oI_II_iI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1 & y2, z1), box3D(x1, y1 - y2, z1)]
        return table

    def iI_II_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1 & y2, z1), box3D(x1, y1 - y2, z1)]
        return table

    def oI_II_oII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1 & y2, z1), box3D(x1, y1 - y2, z1)]
        return table

    def oII_I_oII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2 - x1, y1 & y2, z2), box3D(x2, y2 - y1, z2)]
        return table

    def oII_I_oII_I_iI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1 & y2, z1), box3D(x1, y1 - y2, z1)]
        return table

    def oII_I_iI_II_i_II_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2 - x1, y2, z2), box3D(x1 & x2, closed(y2.lower, y1.lower), z2), box3D(x1 & x2, closed(y1.upper, y2.upper), z2)]
        return table

    def oI_II_iI_II_iI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x2, y2, z2), box3D(x1 - x2, y1, z1)]
        return table

    def oI_II_iI_II_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2 - x1, y2, z2), box3D(x1 & x2, closed(y2.lower, y1.lower), z2), box3D(x1 & x2, closed(y1.upper, y2.upper), z2)]
        return table

    def oI_II_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2 - x1, y2, z2)]
        return table

    def oII_I_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x2 - x1, y2, z2)]
        return table

    def mylen(self, interval):
        if interval == closed(math.inf, -math.inf):
            return 0
        else:
            length = interval.upper - interval.lower if interval.lower > 0 else interval.upper + interval.lower
            return length

    def divide_in(self, int1, int2):
        return [int1 | int2]

    def divide_out(self, int1, int2):
        inter = int1 & int2
        return [int1 - inter, inter, int2 - inter]

    def is_in(self, interval1, interval2):
        union = interval1 & interval2
        return True if ((union.lower == interval1.lower and union.upper == interval1.upper) ^ (union.lower == interval2.lower and union.upper == interval2.upper)) else False

    def is_equal(self, interval1, interval2):
        return True if interval1 == interval2 else False

    def is_out(self, interval1, interval2):
        return True if (interval1.lower != interval2.lower) and (interval2.upper != interval1.upper) and (interval1 & interval2) else False

    def is_separate(self, int1, int2):
        intersect = int1 & int2
        return True if self.mylen(intersect) == 0 else False

    def is_half_out(self, int1, int2):
        len1, len2 = (self.mylen(int1), self.mylen(int2))
        difference2 = len2 - len1 if len1 > 0 else len1 + len2
        difference1 = len1 - len2 if len2 > 0 else len1 + len2
        return True if ((int1.lower == int2.lower) ^ (int2.upper == int1.upper)) and ((difference1 > 0) | (difference2 > 0)) else False

    def get_signature(self, interval1, interval2):
        if self.ii12(interval1, interval2):
            return 'ii12'
        if self.ii21(interval1, interval2):
            return 'ii21'
        if self.io12(interval1, interval2):
            return 'io12'
        if self.io21(interval1, interval2):
            return 'io21'
        if self.ie(interval1, interval2):
            return 'ii12'

    def ie(self, interval1, interval2):
        return True if self.is_equal(interval1, interval2) else False

    def io12(self, interval1, interval2):
        if ((interval1.upper < interval2.upper) & (self.is_out(interval1, interval2))) | (self.is_half_out(interval1, interval2) & ((interval1.lower < interval2.lower) ^ (interval1.upper < interval2.upper))):
            return True
        else:
            return False

    def ii12(self, interval1, interval2):
        union = interval1 & interval2
        return True if (union.lower == interval1.lower) and (union.upper == interval1.upper) and (interval1.lower < interval2.lower) and (interval1.upper < interval2.upper) else False

    def io21(self, interval1, interval2):
        if ((interval2.upper < interval1.upper) & (self.is_out(interval1, interval2))) | (self.is_half_out(interval1, interval2) & ((interval2.lower < interval1.lower) ^ (interval2.upper < interval1.upper))):
            return True
        else:
            return False

    def ii21(self, interval1, interval2):
        union = interval1 & interval2
        return True if ((union.lower == interval2.lower) and (union.upper == interval2.upper) and (interval1.lower > interval2.lower) and (interval1.upper > interval2.upper)) else False

    def get_signatures_triple(self, box1, box2):
        x1, y1, z1, x2, y2, z2 = box1.interval_x, box1.interval_y, box1.interval_z, box2.interval_x, box2.interval_y, box2.interval_z
        signatures = [self.get_signature(x1, x2), self.get_signature(y1, y2), self.get_signature(z1, z2)]
        return signatures

    def main_signatures(self, box1, box2):
        idx_sign = self.get_signatures_triple(box1, box2)
        sort, in2sorted, sorted2in = self.my_sort(idx_sign)
        tri_sign, tri_sign_i = self.sort_signatures(box1, box2, in2sorted)

        split = self.split(tuple(sort), tri_sign, tri_sign_i)

        table = self.ret_original_order(split, sorted2in)

        for k in range(len(split)):
            print('table = ', [table[k].interval_x, table[k].interval_y, table[k].interval_z])

        return table

    def split(self, idx_sign, tri_sign, tri_sign_i):
        box1 = box3D(tri_sign[0], tri_sign[1], tri_sign[2])
        box2 = box3D(tri_sign_i[0], tri_sign_i[1], tri_sign_i[2])
        rozbij_dict = {('io12', 'io12', 'io12'): self.oI_II_oI_II_oI_II,
                       ('io12', 'io21', 'io21'): self.oI_II_oII_I_oII_I,



                       ('ii12', 'io12', 'io21'): self.iI_II_oI_II_oII_I,
                       ('io12', 'io12', 'io21'): self.oI_II_oI_II_oII_I,
                       ('io21', 'io21', 'io21'): self.oII_I_oII_I_oII_I,

                       ('ii12', 'ii12', 'ii12'): self.iI_II_iI_II_iI_II,
                       ('ii12', 'ii12', 'ii21'): self.iI_II_iI_II_iII_I,
                       ('ii12', 'ii21', 'ii21'): self.iI_II_iII_I_iII_I,
                       ('ii21', 'ii21', 'ii21'): self.iII_I_iII_I_iII_I,

                       ('ii12', 'io12', 'io12'): self.oI_II_oI_II_iI_II,
                       ('ii12', 'io21', 'io21'): self.oII_I_oII_I_iI_II,
                       ('ii12', 'ii12', 'io21'): self.oII_I_iI_II_iI_II,

                       ('ii21', 'io12', 'io12'): self.oI_II_oI_II_iII_I,
                       ('ii21', 'io12', 'io21'): self.oI_II_oII_I_iII_I,
                       ('ii21', 'io21', 'io21'): self.oII_I_oII_I_iII_I,
                       ('ii21', 'ii21', 'io21'): self.oII_I_iII_I_iII_I,

                       ('ii12', 'ii21', 'io21'): self.oII_I_iI_II_i_II_I,
                       ('ii12', 'ii12', 'io12'): self.oI_II_iI_II_iI_II,
                       ('ii12', 'ii21', 'io12'): self.oI_II_iI_II_iII_I,
                       ('ii21', 'ii21', 'io12'): self.oI_II_iII_I_iII_I}
        print(idx_sign)
        split = rozbij_dict[idx_sign](box1, box2)
        return split

    def sort_signatures(self, box1, box2, in2sorted):
        box_tab1 = [box1.interval_x, box1.interval_y, box1.interval_z]
        box_tab2 = [box2.interval_x, box2.interval_y, box2.interval_z]
        tri_sign, tri_sign_i = self.permute_signatures(box_tab1, box_tab2, in2sorted)
        return tri_sign, tri_sign_i

    def ret_original_order(self, split, sorted2in):
        table = []
        for i in split:
            j = [i.interval_x, i.interval_y, i.interval_z]
            perm = self.permute(j, sorted2in)
            table.append(box3D(perm[0], perm[1], perm[2]))
        return table

    def permute_signatures(self, box_tab1, box_tab2, sorted2in):
        box_tab1, box_tab2 = self.permute(box_tab1, sorted2in), self.permute(box_tab2, sorted2in)
        return box_tab1, box_tab2

    def permute(self, sortin, permutation):
        assert len(sortin) == len(permutation)
        return [sortin[i] for i in permutation]

    def my_sort(self, inputlist):
        inputlist = zip(inputlist, range(len(inputlist)))
        aux = sorted(inputlist, key = lambda x : x[0])
        sorted2in = [aux[i][1] for i in range(len(aux))]
        list2 = zip(sorted2in, range(len(sorted2in)))
        aux1 = sorted(list2, key = lambda x : x[0])
        in2sorted = [aux1[i][1] for i in range(len(aux1))]
        sort = [aux[i][0] for i in range(len(aux))]
        return sort, in2sorted, sorted2in

    @staticmethod
    def algorytm(Q, tree):
        iD = 0
        while not len(Q.get_stack()) == 0:
            q = Q.pop()
            if tree.tree.count((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper)) > 0:
                i = list(tree.tree.intersection((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper), objects=True))[0]
                inter = [i.object.interval_x, i.object.interval_y, i.object.interval_z]
                print(inter)
                j = box3D(inter[0], inter[1], inter[2])
                Q.extend(algorytm().main_signatures(q, j))
                tree.tree.delete(i.id, (i.bbox[0], i.bbox[1], i.bbox[2], i.bbox[3], i.bbox[4], i.bbox[5]))
            else:
                tree.tree.add(iD, (q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper), q)
                iD += 1
        # wypisanie drzewa
        lista = tree.tree.intersection(tree.tree.get_bounds(), True)
        lista = [item.bbox for item in lista]
        print('\n')
        for i in lista:
            print([i[0], i[3]], end = '') if i[0] != i[3] else print([i[0]], end = '')
            print(' x ', end = '')
            print([i[1], i[4]], end = '') if i[1] != i[4] else print([i[1]], end = '')
            print(' x ', end = '')
            print([i[2], i[5]], end = '\n') if i[2] != i[5] else print([i[2]], end = '\n')
        return tree.tree


Q = boxStack()


pudelka = int(input('Ile pudełek?: '))
for i in range(pudelka):
    Q.append(box3D.factory(int(input("Podaj po jednej z sześciu współrzędnych pudełka oddzielonych enterem: \n")), int(input()), int(input()), int(input()), int(input()), int(input())))
algorytm().algorytm(Q, tree())


'''TEST FUNKCJI'''
'''
import unittest
class testing(unittest.TestCase):
    def setUp(self):
        self.we1 = [0, 1, 2, 5, 6, 7]
        self.we2 = [10, 20, 30, 44, 22, 31]
        self.we3 = [-2, 10, 3, 11, 13, 5]
        self.q = boxStack()
        self.q.append(box3D.factory(self.we1[0], self.we1[1],self.we1[2],self.we1[3],self.we1[4],self.we1[5]))
        self.i = list(tree().tree.intersection((self.we1[0], self.we1[1],self.we1[2],self.we1[3],self.we1[4],self.we1[5]), objects=True))
        self.tree = tree()
        self.tree.tree.insert(0, self.we1)
    def test_funkcji_algorytm(self):
        self.assertTrue(algorytm().algorytm(self.q,self.tree).get_bounds() == self.tree.tree.get_bounds())
    def test_funkcji_rozbij(self):
        self.q = box3D.factory(self.we1[0], self.we1[1],self.we1[2],self.we1[3],self.we1[4],self.we1[5])
        self.i = box3D(closed(self.we1[0],self.we1[3]), closed(self.we1[1],self.we1[4]), closed(self.we1[2],self.we1[5]))
        self.assertEqual(algorytm().rozbij(self.q, self.i) , (algorytm().rozbijanie(closed(self.we1[0], self.we1[3]), closed(self.we1[0], self.we1[3])),algorytm().rozbijanie(closed(self.we1[1], self.we1[4]), closed(self.we1[1], self.we1[4])),algorytm().rozbijanie(closed(self.we1[2], self.we1[5]), closed(self.we1[2], self.we1[5]))))
    def test_funkcji_rozbijanie(self):
        self.assertEqual(algorytm().rozbijanie(closed(self.we3[1], self.we3[4]),closed(self.we2[0], self.we2[3])), (empty(), closed(10,13), openclosed(13, 44)))
if __name__ == '__main__':
    unittest.main()
'''
