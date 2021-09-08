import portion
import math
from cut_box import *
from boxes3D import *

def mylen(interval):
    '''
    Funkcja licząca długość interwału potrzebna do funkcji is_half_out\n
    :param interval: interwał do zmierzenia długości\n
    :return: długość interwału\n
    :rtype: float
    '''
    if interval == my_closed(math.inf, -math.inf):
        return 0
    else:
        length = interval.upper - interval.lower if interval.lower > 0 else abs(interval.upper + interval.lower)
        return length

class split:
    '''
    Klasa dzieląca pudełka \n
    zawiera ona 20 funkcji, z których każda rozbija pudełka \n
    Uwzględniłem możliwość wystąpienia half-out \n
    :param empty: interwał pusty 
    '''
    empty = my_closed(math.inf, -math.inf)

    def iI_II_iI_II_iI_II(self, box1, box2):
        return [box2]

    def iII_I_iII_I_iII_I(self, box1, box2):
        return [box1]

    def iI_II_iI_II_iII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x, box1.interval_y, my_closed(box1.interval_z.lower, box2.interval_z.lower))
        my_box2 = box3D(box1.interval_x, box1.interval_y, my_closed(box2.inteval_z.upper, box1.interval_z.upper))
        return [box2, my_box1, my_box2]

    def iI_II_iII_I_iII_I(self, box1, box2):
        my_box1 = box3D(my_closed(box2.interval_x.lower, box1.interval_x.lower), box2.interval_y, box2.interval_z)
        my_box2 = box3D(my_closed(box1.interval_x.upper, box2.interval_x.upper), box2.interval_y, box2.interval_z)
        return [box1, my_box1, my_box2]

    def iII_I_oII_I_oII_I(self, box1, box2):
        my_box1 = box3D(box2.interval_x, box2.interval_y & box1.interval_y, box2.interval_z - box1.interval_z)
        my_box2 = box3D(box2.interval_x, box2.interval_y - box1.interval_y, box2.interval_z)
        return [box1, my_box1, my_box2]

    def iI_II_oI_II_oII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x, box1.interval_y - box2.interval_y, box1.interval_z & box2.interval_z)
        my_box2 = box3D(box1.interval_x, box1.interval_y & box2.interval_y, box1.interval_z - box2.interval_z)
        my_box3 = box3D(box1.interval_x, box1.interval_y - box2.interval_y, box1.interval_z - box2.interval_z)
        return [box2, my_box1, my_box2, my_box3]

    def iI_II_oI_II_oI_II(self, box1, box2):
        return self.iII_I_oII_I_oII_I(box2, box1)

    def iI_II_oII_I_oII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x, box1.interval_y & box2.interval_y, box1.interval_z - box2.interval_z)
        my_box2 = box3D(box1.interval_x, box1.interval_y - box2.interval_y, box1.interval_z - box2.interval_z)
        my_box3 = box3D(box1.interval_x, box1.interval_y - box2.interval_y, box1.interval_z & box2.interval_z)
        return [box2, my_box1, my_box2, my_box3]

    def iI_II_iI_II_oII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x, box1.interval_y, box1.interval_z - box2.interval_z)
        return [box2, my_box1]

    def iII_I_iII_I_oI_II(self, box1, box2):
        return self.iI_II_iI_II_oII_I(box2, box1)

    def iII_I_iII_I_oII_I(self, box1, box2):
        my_box1 = box3D(box2.interval_x, box2.interval_y, box2.interval_z - box1.interval_z)
        return [box1, my_box1]

    def iI_II_iI_II_oI_II(self, box1, box2):
        return self.iII_I_iII_I_oII_I(box2, box1)

    def iII_I_oI_II_oI_II(self, box1, box2):
        return self.iI_II_oII_I_oII_I(box2, box1)

    def iII_I_oI_II_oII_I(self, box1, box2):
        my_box1 = box3D(box2.interval_x, box2.interval_y & box1.interval_y, box2.interval_z - box1.interval_z)
        my_box2 = box3D(box2.interval_x, box2.interval_y - box1.interval_y, box2.interval_z - box1.interval_z)
        my_box3 = box3D(box2.interval_x, box2.interval_y - box1.interval_y, box1.interval_z & box2.interval_z)
        return [box1, my_box1, my_box2, my_box3]

    def iI_II_iII_I_oII_I(self, box1, box2):
        interval_split = [i for i in box1.interval_y - box2.interval_y]
        my_box1 = box3D(box1.interval_x, interval_split[0], box1.interval_z)
        my_box2 = box3D(box1.interval_x, interval_split[1], box1.interval_z)
        my_box3 = box3D(box1.interval_x & box2.interval_x, box1.interval_y & box2.interval_y, box1.interval_z -
                        box2.interval_z)
        return [box2, my_box1, my_box2, my_box3]

    def iI_II_iII_I_oI_II(self, box1, box2):
        return self.iI_II_iII_I_oII_I(box1, box2)

    def oI_II_oI_II_oI_II(self, box1, box2):
        my_box1 = box3D(box1.interval_x, box1.interval_y, box1.interval_z - box2.interval_z)
        my_box2 = box3D(box1.interval_x & box2.interval_x, box1.interval_y - box2.interval_y, box1.interval_z &
                        box2.interval_z)
        my_box3 = box3D(box1.interval_x - box2.interval_x, box1.interval_y, box1.interval_z - box2.interval_z)
        return [box2, my_box1, my_box2, my_box3]

    def oII_I_oII_I_oII_I(self, box1, box2):
        return self.oI_II_oI_II_oI_II(box2, box1)

    def oI_II_oI_II_oII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x & box2.interval_x, box2.interval_y - box2.interval_y, box2.interval_z)
        my_box2 = box3D(box2.interval_x - box1.interval_x, box2.interval_y, box2.interval_z)
        my_box3 = box3D(box1.interval_x & box2.interval_x, box2.interval_y & box1.interval_y, box2.interval_z
                        - box1.interval_z)
        return [box1, my_box1, my_box2, my_box3]

    def oI_II_oII_I_oII_I(self, box1, box2):
        my_box1 = box3D(box1.interval_x & box2.interval_x, box2.interval_y & box1.interval_y, box2.interval_z
                        - box1.interval_z)
        my_box2 = box3D(box1.interval_x & box2.interval_x, box2.interval_y - box1.interval_y, box2.interval_z)
        my_box3 = box3D(box2.interval_x - box1.interval_x, box2.interval_y, box2.interval_z)
        return [box1, my_box1, my_box2, my_box3]

    '''
    20 funkcji rozbijających pudełka.
    Na wejściu 2 pudełka, na wyjściu tablica pudełek z po rozbiciu.\n
    '''

    def split(self, idx_sign, tri_sign, tri_sign_i):
        '''
        Funkcja dobierająca właściwą funkcje rozbijającą na bazie trójki interwałów\n
        :param idx_sign: lista sygnatur interwałów\n
        :param tri_sign: lista interwałów pierwszego pudełka\n
        :param tri_sign_i: lista interwałów drugiego pudełka\n
        :return: listę pudełek powstałych w wyniku rozbicia pudełek wejściowych
        '''
        box1 = tri_sign
        box2 = tri_sign_i
        rozbij_dict = {
                       ('ii12', 'ii12', 'ii12'): self.iI_II_iI_II_iI_II,
                       ('ii21', 'ii21', 'ii21'): self.iII_I_iII_I_iII_I,
                       ('ii12', 'ii12', 'ii21'): self.iI_II_iI_II_iII_I,
                       ('ii12', 'ii21', 'ii21'): self.iI_II_iII_I_iII_I,
                       ('ii21', 'io21', 'io21'): self.iII_I_oII_I_oII_I,
                       ('ii12', 'io12', 'io21'): self.iI_II_oI_II_oII_I,
                       ('ii12', 'io12', 'io12'): self.iI_II_oI_II_oI_II,
                       ('ii12', 'ii12', 'io21'): self.iI_II_iI_II_oII_I,
                       ('ii21', 'ii21', 'io12'): self.iII_I_iII_I_oI_II,
                       ('ii21', 'ii21', 'io21'): self.iII_I_iII_I_oII_I,
                       ('ii12', 'ii12', 'io12'): self.iI_II_iI_II_oI_II,
                       ('ii12', 'io21', 'io21'): self.iI_II_oII_I_oII_I,
                       ('ii21', 'io12', 'io12'): self.iII_I_oI_II_oI_II,
                       ('ii21', 'io12', 'io21'): self.iII_I_oI_II_oII_I,
                       ('ii12', 'ii21', 'io21'): self.iI_II_iII_I_oII_I,
                       ('ii12', 'ii21', 'io12'): self.iI_II_iII_I_oI_II,
                       ('io12', 'io12', 'io12'): self.oI_II_oI_II_oI_II,
                       ('io21', 'io21', 'io21'): self.oII_I_oII_I_oII_I,
                       ('io12', 'io12', 'io21'): self.oI_II_oI_II_oII_I,
                       ('io12', 'io21', 'io21'): self.oI_II_oII_I_oII_I
                      }
        verify = []
        split = rozbij_dict[idx_sign](box1, box2)
        for box in split:
            if box.interval_x.empty or box.interval_y.empty or box.interval_z.empty:
                continue
            else:
                verify.append(box)
        return verify
