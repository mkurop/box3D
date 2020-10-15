from portion import *
from split import *
from cut import *
import math


def mylen(interval):
    if interval == closed(math.inf, -math.inf):
        return 0
    else:
        length = interval.upper - interval.lower if interval.lower > 0 else abs(interval.upper + interval.lower)
        return length


class divide:
    def split(self, idx_sign, tri_sign, tri_sign_i):
        box1 = box3D(tri_sign[0], tri_sign[1], tri_sign[2])
        box2 = box3D(tri_sign_i[0], tri_sign_i[1], tri_sign_i[2])
        rozbij_dict = {
                       ('ii21', 'io21', 'io21'): self.iII_I_oII_I_oII_I,
                       ('ii12', 'io12', 'io21'): self.iI_II_oI_II_oII_I,
                       ('ii12', 'ii12', 'ii21'): self.iI_II_iI_II_iII_I,
                       ('ii12', 'ii21', 'ii21'): self.iI_II_iII_I_iII_I,
                       ('ii12', 'io12', 'io12'): self.iI_II_oI_II_oI_II,
                       ('ii12', 'io21', 'io21'): self.iI_II_oII_I_oII_I,
                       ('ii12', 'ii12', 'io21'): self.iI_II_iI_II_oII_I,
                       ('ii21', 'io12', 'io12'): self.iII_I_oI_II_oI_II,
                       ('ii21', 'io12', 'io21'): self.iII_I_oI_II_oII_I,
                       ('ii21', 'ii21', 'io21'): self.iII_I_iII_I_oII_I,
                       ('ii12', 'ii21', 'io21'): self.iI_II_i_II_I_oII_I,
                       ('ii12', 'ii12', 'io12'): self.iI_II_iI_II_oI_II,
                       ('ii21', 'ii21', 'io12'): self.iII_I_iII_I_oI_II,
                       ('ii12', 'ii21', 'io12'): self.iI_II_iII_I_oI_II,
                       ('io12', 'io12', 'io12'): self.oI_II_oI_II_oI_II,
                       ('io12', 'io12', 'io21'): self.oI_II_oI_II_oII_I,
                       ('io12', 'io21', 'io21'): self.oI_II_oII_I_oII_I,
                       ('io21', 'io21', 'io21'): self.oII_I_oII_I_oII_I,
                       ('ii12', 'ii12', 'ii12'): self.iI_II_iI_II_iI_II,
                       ('ii21', 'ii21', 'ii21'): self.iII_I_iII_I_iII_I}

        split = rozbij_dict[idx_sign](box1, box2)
        return split

    def ret_original_order(self, split, sorted2in):
        table = []
        for i in split:
            j = [i.interval_x, i.interval_y, i.interval_z]
            perm = self.permute_signatures(j, sorted2in)
            table.append(box3D(perm[0], perm[1], perm[2]))
        return table