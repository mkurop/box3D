import math

class TEST:
###PROBLEMY: 1 - funkcje są w zlej kolejności interwałów względem mysort (in12 powinno być np jako pierwsze a jest po o21)
###2 - funkcja rozbija na przecinające sie pudełka
    def oI_II_oI_II_oI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(closed(x2.lower, x1.upper), closed(y2.lower, y1.upper ), closed(z1.upper + 1, z2.upper)), box3D(closed(x1.upper + 1, x2.upper), closed(y2.lower, y1.upper), z2), box3D(x2, closed(y1.upper + 1, y2.upper), z2)]
        return table

    def oI_II_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, closed(z2.lower, z1.lower)), box3D(x2, closed(y2.lower, y1.lower - 1), z2), box3D(closed(x1.upper + 1, x2.upper), closed(y1.lower, y2.upper), z2)]
        return table


####
    def oI_II_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x2, y2 - y1, z2), box3D(x2 - x1, y2, z2)]
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

    def oI_II_oII_I_iI_II(self, box1, box2):
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
        if interval.empty():
            return 0
        else:
            length = interval.upper - interval.lower
            return length

    def get_signature(self, interval1, interval2):
        if self.ii12(interval1, interval2):
            return 'ii12'
        elif self.ii21(interval1, interval2):
            return 'ii21'
        elif self.io12(interval1, interval2):
            return 'io12'
        elif self.io21(interval1, interval2):
            return 'io21'
        elif self.ie(interval1, interval2):
            return 'ii12'


    def ie(self, interval1, interval2):
        return True if self.is_equal(interval1, interval2) else False

    def io12(self, interval1, interval2):
        if (interval1.upper < interval2.upper) & (self.is_out(interval1, interval2)) | (self.is_half_out(interval1, interval2) & ((interval1.lower < interval2.lower) | (interval1.upper < interval2.upper))):
            return True
        else:
            return False

    def ii12(self, interval1, interval2):
        return True if self.is_in(interval1, interval2) & interval1.upper < interval2.upper else False

    def io21(self, interval1, interval2):
        if (interval2.upper < interval1.upper) & (self.is_out(interval1, interval2)) | (self.is_half_out(interval1, interval2) & ((interval2.lower < interval1.lower) | (interval2.upper < interval1.upper))):
            return True
        else:
            return False

    def ii21(self, interval1, interval2):
        return True if self.is_in(interval1, interval2) & interval2.upper < interval1.upper else False

    def get_signatures_triple(self, box1, box2):
        x1, y1, z1, x2, y2, z2 = box1.interval_x, box1.interval_y, box1.interval_z, box2.interval_x, box2.interval_y, box2.interval_z
        return self.get_signature(x1, x2), self.get_signature(y1, y2), self.get_signature(z1, z2)

    rozbij_dict = {('io12', 'io12', 'io12'): oI_II_oI_II_oI_II,
                   ('io12', 'io21', 'io21'): oI_II_oII_I_oII_I,
                    #dotąd zrobione


                   ('io12', 'io12', 'io21'): oI_II_oI_II_oII_I,
                   ('io21', 'io21', 'io21'): oII_I_oII_I_oII_I,

                   ('ii12', 'ii12', 'ii12'): iI_II_iI_II_iI_II,
                   ('ii12', 'ii12', 'ii21'): iI_II_iI_II_iII_I,
                   ('ii12', 'ii21', 'ii21'): iI_II_iII_I_iII_I,
                   ('ii21', 'ii21', 'ii21'): iII_I_iII_I_iII_I,

                   ('io12', 'io12', 'ii12'): oI_II_oI_II_iI_II,
                   ('io12', 'io21', 'ii12'): oI_II_oII_I_iI_II,
                   ('io21', 'io21', 'ii12'): oII_I_oII_I_iI_II,
                   ('io21', 'ii12', 'ii12'): oII_I_iI_II_iI_II,

                   ('io12', 'io12', 'ii21'): oI_II_oI_II_iII_I,
                   ('io12', 'io21', 'ii21'): oI_II_oII_I_iII_I,
                   ('io21', 'io21', 'ii21'): oII_I_oII_I_iII_I,
                   ('io21', 'ii21', 'ii21'): oII_I_iII_I_iII_I,

                   ('io21', 'ii12', 'ii21'): oII_I_iI_II_i_II_I,
                   ('io12', 'ii12', 'ii12'): oI_II_iI_II_iI_II,
                   ('io12', 'ii12', 'ii21'): oI_II_iI_II_iII_I,
                   ('io12', 'ii21', 'ii21'): oI_II_iII_I_iII_I}

    def main_signatures(self, box1, box2):
        idx_sign = self.get_signatures_triple(box1, box2)
        sort, in2sorted, sorted2in = self.my_sort(idx_sign)
        tri_sign, tri_sign_i = self.sort_signatures(box1, box2, in2sorted)
        split = self.split(idx_sign, tri_sign, tri_sign_i)
        table = [self.ret_original_order(split, sorted2in)]
        return table

    def split(self, idx_sign, tri_sign, tri_sign_i):
        box1, box2 = box3D(tri_sign[0], tri_sign[1], tri_sign[2]), box3D(tri_sign_i[0], tri_sign_i[1], tri_sign_i[2])
        split = self.rozbij_dict[idx_sign](box1, box2)
        return split

    def sort_signatures(self, box1, box2, in2sorted):
        box_tab1, box_tab2 = [box1.interval_x, box1.interval_y, box1.interval_z], [box2.interval_x, box2.interval_y, box2.interval_z]
        tri_sign = self.permute([[box_tab1[0]], [box_tab1[1]], [box_tab1[2]]], in2sorted)
        tri_sign_i = self.permute([[box_tab2[0]], [box_tab2[1]], [box_tab2[2]]], in2sorted)
        return tri_sign, tri_sign_i

    def ret_original_order(self, tri_sign, tri_sign_i, sorted2in):
        tri_sign = self.permute(tri_sign, sorted2in)
        tri_sign_i = self.permute(tri_sign_i, sorted2in)
        return tri_sign, tri_sign_i

    def permute_signatures(self, box1, box2, sorted2in):
        box1, box2 = self.permute(box1, sorted2in), self.permute(box2, sorted2in)
        return box1, box2

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

    def is_in(self, interval1, interval2):
        union = interval1 & interval2
        return True if ((union == interval1) ^ (union == interval2)) and (interval2.lower != interval1.lower and interval1.upper != interval2.upper) else False

    def is_out(self, interval1, interval2):
        return True if (interval1.lower != interval2.lower) and (interval2.upper != interval1.upper) and (interval1 & interval2) else False

    def is_equal(self, interval1, interval2):
        return True if interval1 == interval2 else False

    def is_half_out(self, int1, int2):
        len1, len2 = (self.mylen(int1), self.mylen(int2))
        difference2 = len2 - len1 if len1 > 0 else len1 + len2
        difference1 = len1 - len2 if len2 > 0 else len1 + len2
        return True if ((int1.lower == int2.lower) ^ (int2.upper == int1.upper)) and ((difference1 > 0) | (difference2 > 0)) else False

    def divide_out(self, int1, int2):
        inter = int1 & int2
        return [int1 - inter, inter, int2 - inter]

    def is_separate(self, int1, int2):
        intersect = int1 & int2
        return True if self.mylen(intersect) == 0 else False

    def divide_in(self, int1, int2):
        return [int1 | int2]

class box3D:
    def __init__(self, interval_x, interval_y, interval_z):
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.interval_z = interval_z

    def __contains__(self, num):
        return True if (num[0] in self.interval_x) & (num[1] in self.interval_y) & (num[2] in self.interval_z) else False

    def __ror__(self, num):
        x, y, z = num[0], num[1], num[2]
        is_on_border = x in set([self.interval_x.lower, self.interval_x.upper]) or y in set([self.interval_y.lower, self.interval_y.upper]) or z in set([self.interval_z.lower, self.interval_z.upper])
        is_inside_box = self.__contains__(num)
        return True if is_on_border & is_inside_box else False

    def get_interval_x(self):
        return self.interval_x

    def get_interval_y(self):
        return self.interval_y

    def get_interval_z(self):
        return self.interval_z

    @staticmethod
    def factory(x1, y1, z1, x2, y2, z2):
        return box3D(closed(x1, x2), closed(y1, y2), closed(z1, z2))

from portion import closed, closedopen, openclosed

'''
tst = TEST()
int1 = tst.rozbij(box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())), box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())))

for i in range(len(int1)):
    print(int1[i].interval_x, int1[i].interval_y, int1[i].interval_z)
'''

#unit testy
import random as rnd
class algorithm_check():

    def random_point_from_a_box(self, box):
        num_x = rnd.randint(box.interval_x.lower, box.interval_x.upper)
        num_y = rnd.randint(box.interval_y.lower, box.interval_y.upper)
        num_z = rnd.randint(box.interval_z.lower, box.interval_z.upper)
        return [num_x, num_y, num_z]

    def loop_test(self, boxes_in, boxes_out):
        b = rnd.choice(boxes_in)
        x = self.random_point_from_a_box(b)
        num_in = sum([b.__contains__(x) for b in boxes_out])
        num_boundary = sum([b.__ror__(x) for b in boxes_out])
        if (num_in == 1) or ((num_in == num_boundary) and (num_in != 0)):
            return True
        else:
            return False

    def evaluate(self, boxes_in, boxes_out, checks_num = 1000):
        for i in range(checks_num):
            if fct_chk.loop_test(boxes_in, boxes_out):
                continue
            else:
                return False
        return True

fct_chk = algorithm_check()
out_interval_bigger = closed(3, 6)
interval_smaller = closed(2, 5)
in_interval_bigger = closed(1, 6)
tst = TEST()

box0 = box3D(interval_smaller, interval_smaller, interval_smaller)
box1 = box3D(out_interval_bigger, out_interval_bigger, out_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oI_II_oI_II(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, out_interval_bigger)
box1 = box3D(out_interval_bigger, out_interval_bigger, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oI_II_oII_I(box0, box1)))
box0 = box3D(interval_smaller, out_interval_bigger, out_interval_bigger)
box1 = box3D(out_interval_bigger, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oII_I_oII_I(box0, box1)))
box0 = box3D(out_interval_bigger, out_interval_bigger, out_interval_bigger)
box1 = box3D(interval_smaller, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oII_I_oII_I_oII_I(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, interval_smaller)
box1 = box3D(in_interval_bigger, in_interval_bigger, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.iI_II_iI_II_iI_II(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, in_interval_bigger)
box1 = box3D(in_interval_bigger, in_interval_bigger, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.iI_II_iI_II_iII_I(box0, box1)))
box0 = box3D(interval_smaller, in_interval_bigger, in_interval_bigger)
box1 = box3D(in_interval_bigger, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.iI_II_iII_I_iII_I(box0, box1)))
box0 = box3D(in_interval_bigger, in_interval_bigger, in_interval_bigger)
box1 = box3D(interval_smaller, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.iII_I_iII_I_iII_I(box0, box1)))
box0 = box3D(out_interval_bigger, interval_smaller, interval_smaller)
box1 = box3D(interval_smaller, in_interval_bigger, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oII_I_iI_II_iI_II(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, in_interval_bigger)
box1 = box3D(out_interval_bigger, out_interval_bigger, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oI_II_iII_I(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, interval_smaller)
box1 = box3D(out_interval_bigger, out_interval_bigger, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oI_II_iI_II(box0, box1)))
box0 = box3D(interval_smaller, out_interval_bigger, interval_smaller)
box1 = box3D(out_interval_bigger, interval_smaller, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oII_I_iI_II(box0, box1)))
box0 = box3D(interval_smaller, out_interval_bigger, interval_smaller)
box1 = box3D(out_interval_bigger, interval_smaller, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oI_II_oII_I_iII_I(box0, box1)))
box0 = box3D(out_interval_bigger, out_interval_bigger, in_interval_bigger)
box1 = box3D(interval_smaller, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oII_I_oII_I_iII_I(box0, box1)))
box0 = box3D(out_interval_bigger, out_interval_bigger, interval_smaller)
box1 = box3D(interval_smaller, interval_smaller, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oII_I_oII_I_iI_II(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, in_interval_bigger)
box1 = box3D(out_interval_bigger, in_interval_bigger, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oII_I_iI_II_i_II_I(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, interval_smaller)
box1 = box3D(out_interval_bigger, in_interval_bigger, in_interval_bigger)
print(fct_chk.evaluate([box0, box1], tst.oI_II_iI_II_iI_II(box0, box1)))
box0 = box3D(interval_smaller, interval_smaller, in_interval_bigger)
box1 = box3D(out_interval_bigger, in_interval_bigger, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oI_II_iI_II_iII_I(box0, box1)))
box0 = box3D(interval_smaller, in_interval_bigger, in_interval_bigger)
box1 = box3D(out_interval_bigger, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oI_II_iII_I_iII_I(box0, box1)))
box0 = box3D(out_interval_bigger, in_interval_bigger, in_interval_bigger)
box1 = box3D(interval_smaller, interval_smaller, interval_smaller)
print(fct_chk.evaluate([box0, box1], tst.oII_I_iII_I_iII_I(box0, box1)))
'''
import unittest
class testing(unittest.TestCase):
    def setUp(self):
        self.out_interval_bigger = closed(3, 6)
        self.interval_smaller = closed(2, 5)
        self.in_interval_bigger = closed(1, 6)
        self.tst = TEST()

    def test_funkcji_iI_II_iI_II_iI_II(self):
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.in_interval_bigger)
        self.assertEqual(self.tst.iI_II_iI_II_iI_II(box0, box1),
                         [[self.in_interval_bigger], [self.in_interval_bigger], [self.in_interval_bigger]])

    def test_funkcji_iII_I_iII_I_iII_I(self):
        box0 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.in_interval_bigger)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        self.assertEqual(self.tst.iII_I_iII_I_iII_I(box0, box1),
                         [[self.in_interval_bigger], [self.in_interval_bigger], [self.in_interval_bigger]])

    def test_funkcji_iI_II_iI_II_iII_I(self):
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.in_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.interval_smaller)
        z_cut = self.tst.divide_out(box0.interval_z, box1.interval_z)
        self.assertEqual(self.tst.iI_II_iI_II_iII_I(box0, box1),
                         [[self.interval_smaller, self.interval_smaller, self.in_interval_bigger],
                          [self.in_interval_bigger, self.in_interval_bigger, z_cut[0]],
                          [self.in_interval_bigger, self.in_interval_bigger, z_cut[2]]])

    def test_funkcji_iI_II_iII_I_iII_I(self):
        box0 = box3D(self.interval_smaller, self.in_interval_bigger, self.in_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.interval_smaller, self.interval_smaller)
        x_cut = self.tst.divide_out(self.interval_smaller, self.in_interval_bigger)
        self.assertEqual(self.tst.iI_II_iII_I_iII_I(box0, box1),
                         [[self.interval_smaller, self.in_interval_bigger, self.in_interval_bigger],
                          [x_cut[0], self.interval_smaller, self.interval_smaller],
                          [x_cut[2], self.interval_smaller, self.interval_smaller]])

    def test_funkcji_oI_II_iI_II_iI_II(self):
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.out_interval_bigger, self.in_interval_bigger, self.in_interval_bigger)
        x1, y1, z1 = box0.interval_x, box0.interval_y, box0.interval_z
        x2, y2, z2 = box1.interval_x, box1.interval_y, box1.interval_z
        self.assertEqual(self.tst.oI_II_iI_II_iI_II(box0, box1), [[x2, y2, z2], [x1, y1, z1 - z2]])

if __name__ == '__main__':
    unittest.main()
'''
