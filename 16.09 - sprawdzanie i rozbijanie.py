"""
najpierw trzeba stworzyć 20 funkcji rozbijających kanoniczne trójki sygnatur
lista kanoniczny trójek sygnatur jest następująca:
"""
import math

class TEST:

    def oI_II_oI_II_oI_II(self, box1, box2):
        table = [[]]
        return table

    def oI_II_oI_II_oII_I(self, box1, box2):

        table = [[]]
        return table

    def oI_II_oII_I_oII_I(self, box1, box2):
        table = []
        return table

    def oII_I_oII_I_oII_I(self, box1, box2):
        table = []
        return table

    def iI_II_iI_II_iI_II(self, box1, box2):
        x, y, z = box2.interval_x, box2.interval_y, box2.interval_z
        table = [[x], [y], [z]]
        return table

    def iI_II_iI_II_iII_I(self, box1, box2):
        x1, x2, y1, y2 = box1.interval_x, box2.interval_x, box1.interval_y, box2.interval_y
        z_cut = self.divide_out(box1.interval_z, box2.interval_z)
        table = [[x1, y1, box1.interval_z], [x2, y2, z_cut[0]], [x2, y2, z_cut[2]]]
        return table

    def iI_II_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        x_cut = self.divide_out(x1, x2)
        table = [[x1, y1, z1], [x_cut[0], y2, z2], [x_cut[2], y2, z2]]
        return table

    def iII_I_iII_I_iII_I(self, box1, box2):
        x, y, z = box1.interval_x, box1.interval_y, box1.interval_z
        table = [[x], [y], [z]]
        return table

    def oII_I_iI_II_iI_II(self, box1, box2):
        return

    def oI_II_oI_II_iII_I(self, box1, box2):
        return

    def oI_II_oI_II_iI_II(self, box1, box2):
        return

    def oI_II_oII_I_iI_II(self, box1, box2):
        return

    def oI_II_oII_I_iII_I(self, box1, box2):
        return

    def oII_I_oII_I_iII_I(self, box1, box2):
        return

    def oII_I_oII_I_iI_II(self, box1, box2):
        return

    def oII_I_iI_II_i_II_I(self, box1, box2):
        return

    def oI_II_iI_II_iI_II(self, box1, box2):
        x1, y1, z1 = box1.interval_x, box1.interval_y, box1.interval_z
        x2, y2, z2 = box2.interval_x, box2.interval_y, box2.interval_z
        table = [[x2, y2, z2], [x1, y1, z1 - z2]]
        return table

    def oI_II_iI_II_iII_I(self, box1, box2):
        return

    def oI_II_iII_I_iII_I(self, box1, box2):
        return

    def oII_I_iII_I_iII_I(self, box1, box2):
        return

    """
    ...
    i tak dalej
    """

    """
    potrzebny jest słownik który przyporządkowuje indeksy do słownika sygnatur
    """

    idx_sig = {'oI_II': 0, 'oII_I': 1, 'iI_II': 2, 'iII_I': 3, 'sep': 4}

    """
    potrzebna jest funkcja która zwraca sygnaturę dla pary interwałów wejściowych
    sygnatury są ze zbioru oI_II,oII_I, iI_II, iII_I
    """
    def get_signature(self, interval1, interval2):
        if self.is_out(interval1, interval2):
            return self.idx_sig['oI_II'] if interval2.upper > interval1.upper else self.idx_sig['oII_I']
        elif self.is_in(interval1, interval2):
            return self.idx_sig['iI_II'] if interval2.lower < interval1.lower else self.idx_sig['iII_I']
        elif self.is_equal(interval1, interval2):
            return self.idx_sig['iI_II']
        elif self.is_half_out(interval1, interval2):
            if self.divide_out[1] == (0, 0):
                return self.idx_sig['oI_II'] if interval2.upper > interval1.upper else self.idx_sig['oII_I']
            else:
                return self.idx_sig['iI_II'] if interval2.upper > interval1.upper else self.idx_sig['iII_I']
        else:
            return self.idx_sig['sep']



    """
    funkcja która dla pary pudełek zwraca trójkę sygnatur (możliwe że niekanoniczną)
    """

    def get_signatures_triple(self, box1, box2):
        x1, y1, z1, x2, y2, z2 = box1.interval_x, box1.interval_y, box1.interval_z, box2.interval_x, box2.interval_y, box2.interval_z
        return self.get_signature(x1, x2), self.get_signature(y1, y2), self.get_signature(z1, z2)

    """
    Powiedzmy że powyższa funkcja zwraca trójkę sygnatur ts
    """
#    idx_sig = {'oI_II': 0, 'oII_I': 1, 'iI_II': 2, 'iII_I': 3, 'sep': 4}

    rozbij_dict = {tuple([0, 0, 0]): oI_II_oI_II_oI_II,
                   tuple([0, 0, 1]): oI_II_oI_II_oII_I,
                   tuple([0, 1, 1]): oI_II_oII_I_oII_I,
                   tuple([1, 1, 1]): oII_I_oII_I_oII_I,

                   tuple([2, 2, 2]): iI_II_iI_II_iI_II,
                   tuple([2, 2, 3]): iI_II_iI_II_iII_I,
                   tuple([2, 3, 3]): iI_II_iII_I_iII_I,
                   tuple([3, 3, 3]): iII_I_iII_I_iII_I,

                   tuple([0, 0, 2]): oI_II_oI_II_iI_II,
                   tuple([0, 1, 2]): oI_II_oII_I_iI_II,
                   tuple([1, 1, 2]): oII_I_oII_I_iI_II,
                   tuple([1, 2, 2]): oII_I_iI_II_iI_II,

                   tuple([0, 0, 3]): oI_II_oI_II_iII_I,
                   tuple([0, 1, 3]): oI_II_oII_I_iII_I,
                   tuple([1, 1, 3]): oII_I_oII_I_iII_I,
                   tuple([1, 3, 3]): oII_I_iII_I_iII_I,

                   tuple([1, 2, 3]): oII_I_iI_II_i_II_I,
                   tuple([0, 2, 2]): oI_II_iI_II_iI_II,
                   tuple([0, 2, 3]): oI_II_iI_II_iII_I,
                   tuple([0, 3, 3]): oI_II_iII_I_iII_I}
    """
    Tworzymy liste indeksów dla sygnatur z ts
    """
    def sort_signatures(self, box1, box2):
        idx_sig = self.get_signatures_triple(box1, box2)
        ts = self.get_signatures_triple(box1, box2)
        tsi = [idx_sig[ts[0]], idx_sig[ts[1]], idx_sig[ts[2]]]
        a, b, c = self.my_sort(tsi)
        ts = self.permute(ts, b)
        box1 = self.permute([box1.interval_x, box1.interval_y, box1.interval_z], b)
        box2 = self.permute([box2.interval_x, box2.interval_y, box2.interval_z], b)
        split, table = [], self.rozbij_dict[ts](box1, box2)
        split.extend(box3D(i[0], i[1], i[2]) for i in table)
        box1, box2 = self.permute(box1, c), self.permute(box2, c)
        return split, box1, box2
    """
    następnie my_sort na tsi
    """


    """
    sprowadzamy ts do postaci kanonicznej przy pomocy permute
    """

    """
    sprowadzamy interwały w box1 i box2 do postaci kanonicznej przy pomocy permute
    """

    """
    tworzymy słownik dla funkcji rozbijających
    
    rozbij_dict = {(kanoniczna trójka sygnatur) : (odpowiadająca jej funkcja rozbijająca)}
    """

    """
    stosujemy odpowiednią funkcję do rozbicia naszych pudełek box1 i box2, z interwałami w kolejności kanonicznej
    funkcję rozbijającą pobieramy ze słownika
    """

    """
    cofamy permutację interwałów w box1 i box2 do pierwotnej kolejności przy pomocy funkcji permute
    """

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
        return True if ((union == interval1) ^ (union == interval2)) and (interval2.lower != interval1.lower and interval1.upper != interval2.upper)  else False

    def is_out(self, interval1, interval2):
        return True if (interval1.lower != interval2.lower) and (interval2.upper != interval1.upper) and (interval1 & interval2) else False

    def is_equal(self, interval1, interval2):
        return True if interval1 == interval2 else False

    def is_half_out(self, int1, int2):
        return True if ((int1.lower == int2.lower) ^ (int2.upper == int1.upper)) and ((int2 == int2 & int1) ^ (int1 == int1 & int2)) else False

    def divide_out(self, int1, int2):
        inter = int1 & int2
        return [int1 - inter, inter, int2 - inter]

    def divide_in(self, int1, int2):
        return [int1 | int2]

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
class function_check():
    def test_funkcji_uniwersalny(self, box0, box1, split):
        wrong_x = wrong_y = wrong_z = 0
        x1, y1, z1 = box0.interval_x, box0.interval_y, box0.interval_z
        x2, y2, z2 = box1.interval_x, box1.interval_y, box1.interval_z
        for i in range(1000):
            x_rand = rnd.randint(min(x1.lower, x2.lower), max(x1.upper, x2.upper))
            y_rand = rnd.randint(min(y1.lower, y2.lower), max(y1.upper, y2.upper))
            z_rand = rnd.randint(min(z1.lower, z2.lower), max(z1.upper, z2.upper))
            for j in range(len(split[0][0])):
                if not (x_rand in split[0][0][j]):
                    wrong_x += 1
                else:
                    print('Num: ', x_rand, 'Pod:', i, ': pass!')
                if not (y_rand in split[1][0][j]):
                    wrong_y += 1
                else:
                    print('Num: ', y_rand, 'Pod:', i, ': pass!')
                if not (z_rand in split[2][0][j]):
                    wrong_z += 1
                else:
                    print('Num: ', z_rand, 'Pod:', i, ': pass!')
            if wrong_x == 3:
                exit(('ERROR X, Liczba:', x_rand, ' Iteracja', i + 1))
                break
            elif wrong_y == 3:
                exit(('ERROR Y, Liczba:', y_rand, ' Iteracja', i + 1))
                break
            elif wrong_z == 3:
                exit(('ERROR Z, Liczba:', z_rand, ' Iteracja', i + 1))
            else:
                pass
        print('SUKCES po 1000 prób!')

fct_chk = function_check()
out_interval_bigger = closed(3, 6)
interval_smaller = closed(2, 5)
in_interval_bigger = closed(1, 6)
box0 = box3D(interval_smaller, interval_smaller, interval_smaller)
box1 = box3D(in_interval_bigger, in_interval_bigger, in_interval_bigger)
tst = TEST()
fct_chk.test_funkcji_uniwersalny(box0, box1, tst.iI_II_iI_II_iI_II(box0, box1))
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
