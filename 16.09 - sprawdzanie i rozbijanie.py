"""
najpierw trzeba stworzyć 20 funkcji rozbijających kanoniczne trójki sygnatur
lista kanoniczny trójek sygnatur jest następująca:

[(''), (''), (''),
(''), (''), ('')',
(''), (''), (''),
(''), (''), (''),
(''), (''), (''),
(''), (''), (''),
(''), ('')]

"""
import math

class TEST:


    def oI_II_oI_II_oI_II(box1, box2):
        return

    def oI_II_oI_II_oII_I(box1, box2):
        return

    def oI_II_oII_I_oII_I(box1, box2):
        return

    def oII_I_oII_I_oII_I(box1, box2):
        return

    def iI_II_i_I_II_iI_II(box1, box2):
        return

    def iI_II_i_I_II_iII_I(box1, box2):
        return

    def iI_II_i_II_I_iII_I(box1, box2):
        return

    def iII_I_i_II_I_iII_I(box1, box2):
        return

    def oII_I_iI_II_iI_II(box1, box2):
        return

    def oI_II_oI_II_iII_I(box1, box2):
        return

    def oI_II_oI_II_iI_II(box1, box2):
        return

    def oI_II_oII_I_iI_II(box1, box2):
        return

    def oI_II_oII_I_iII_I(box1, box2):
        return

    def oII_I_oII_I_iII_I(box1, box2):
        return

    def oII_I_oII_I_iI_II(box1, box2):
        return

    def oII_I_iI_II_i_II_I(box1, box2):
        return

    def oI_II_iI_II_iI_II(box1, box2):
        return

    def oI_II_iI_II_iII_I(box1, box2):
        return

    def oI_II_iII_I_iII_I(box1, box2):
        return

    def oII_I_iII_I_iII_I(box1, box2):
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
            if self.divide_out[1] == (math.inf, -math.inf):
                return self.idx_sig['oI_II'] if interval2.upper > interval1.upper else self.idx_sig['oII_I']
            else:
                return self.idx_sig['iI_II'] if interval2.upper > interval1.upper else self.idx_sig['iII_I']
        else:
            self.idx_sig['sep']



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

    rozbij_dict = {([0, 0, 0]): oI_II_oI_II_oI_II,
                   ([0, 0, 1]): oI_II_oI_II_oII_I,
                   ([0, 1, 1]): oI_II_oII_I_oII_I,
                   ([1, 1, 1]): oII_I_oII_I_oII_I,

                   ([2, 2, 2]): iI_II_i_I_II_iI_II,
                   ([2, 2, 3]): iI_II_i_I_II_iII_I,
                   ([2, 3, 3]): iI_II_i_II_I_iII_I,
                   ([3, 3, 3]): iII_I_i_II_I_iII_I,

                   ([0, 0, 2]): oI_II_oI_II_iI_II,
                   ([0, 1, 2]): oI_II_oII_I_iI_II,
                   ([1, 1, 2]): oII_I_oII_I_iI_II,
                   ([1, 2, 2]): oII_I_iI_II_iI_II,

                   ([0, 0, 3]): oI_II_oI_II_iII_I,
                   ([0, 1, 3]): oI_II_oII_I_iII_I,
                   ([1, 1, 3]): oII_I_oII_I_iII_I,
                   ([1, 3, 3]): oII_I_iII_I_iII_I,

                   ([1, 2, 3]): oII_I_iI_II_i_II_I,
                   ([0, 2, 2]): oI_II_iI_II_iI_II,
                   ([0, 2, 3]): oI_II_iI_II_iII_I,
                   ([0, 3, 3]): oI_II_iII_I_iII_I,
                   }
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
        split = self.rozbij_dict[ts](box1, box2)
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
from portion import closed
tst = TEST()
int1 = tst.rozbij(box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())), box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())))

for i in range(len(int1)):
    print(int1[i].interval_x, int1[i].interval_y, int1[i].interval_z)
