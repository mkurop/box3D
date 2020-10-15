import portion
from divide import *
from cut import *

def my_closed(lower, upper):
    return myInterval.from_atomic(portion.const.Bound.CLOSED, lower, upper, portion.const.Bound.CLOSED)

class algorytm:
    def oI_II_oI_II_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x2 - x1, y2 & y1, z2), box3D(x2, y2 - y1, z2)]
        return table

    def oI_II_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x2 - x1, y2, z2), box3D(x2 & x1, y2 - y1, z2)]
        return table

    def oI_II_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x1 & x2, y1 & y2, closed(z2.lower, z1.lower)), box3D(x2, closed(y2.lower, y1.lower), z2), box3D(closed(x1.upper, x2.upper), closed(y1.lower, y2.upper), z2)]
        return table

    def oII_I_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x2, y2 - y1, z2), box3D(x2 - x1, y2 & y1, z2), box3D(x1 & x2, y1 & y2, z2 - z1)]
        return table

    def iI_II_iI_II_iI_II(self, box1, box2):
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2)]
        return table

    def iI_II_iI_II_iII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2)]
        z = [i for i in z1 - z2]
        if len(z) == 2:
            if z[0] != closed(math.inf, -math.inf) and z[1] != closed(math.inf, -math.inf):
                table.append(box3D(x1, y1, z[0]))
                table.append(box3D(x1, y1, z[1]))
        if len(z) != 2 or (closed(math.inf, -math.inf) in z):
            if z[0] != closed(math.inf, -math.inf):
                table.append(box3D(x1, y1, z[0]))
            if len(z) == 2:
                if z[1] != closed(math.inf, -math.inf):
                    table.append(x1, y1, z[1])
        return table

    def iI_II_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1)]
        x = [i for i in x2 - x1]
        if x[0] != closed(math.inf, -math.inf):
            table.append(box3D(x[0], y2, z2))
        if len(x) == 2:
            if x[1] != closed(math.inf, -math.inf):
                table.append(box3D(x[1], y2, z2))
        return table

    def iII_I_iII_I_iII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        table = [box3D(x1, y1, z1)]
        return table

    def iI_II_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2), box3D(x1, y1 - y2, z1), box3D(x1, y2 & y1, z1 - z2)]
        return table

    def iI_II_oI_II_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        if mylen(z2) > mylen(z1):
            x = [x for x in x1 - x2]
            table = [box3D(x2, y2, z2), box3D(x1, y1 - y2, z1), box3D(x1 & x2, y1 & y2, z1 - z2), box3D(x[0], y1 & y2, z1), box3D(x[1], y1 & y2, z1)]
        else:
            table = [box3D(x1, y1, z1), box3D(x2, y2 - y1, z2), box3D(x2, y1 & y2, z2 - z1)]
        return table

    def iI_II_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2), box3D(x1, y1 & y2, z1 - z2), box3D(x1, y1 - y2, z1)]
        return table

    def iI_II_iI_II_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2), box3D(x1, y1, z1 - z2)]
        return table

    def iII_I_oI_II_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x2, y2 & y1, z2 - z1), box3D(x2, y2 - y1, z2)]
        return table

    def iII_I_oII_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        if mylen(z2) > mylen(z1):
            x = [x for x in x2 - x1]
            table = [box3D(x1, y1, z1), box3D(x2, y2 - y1, z2), box3D(x1 & x2, y1 & y2, z2 - z1), box3D(x[0], y1 & y2, z2), box3D(x[1], y1 & y2, z2)]

        else:
            table = [box3D(x2, y2, z2), box3D(x1, y1 - y2, z1), box3D(x1, y1 & y2, z1 - z2)]
        return table

    def iII_I_oI_II_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x2, y2 & y1, z2 - z1), box3D(x2, y2 - y1, z2)]
        return table

    def iII_I_iII_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x2, y2, z2 - z1)]
        return table

    def iI_II_i_II_I_oII_I(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        x = [i for i in x2 - x1]
        table = [box3D(x1, y1, z1), box3D(x2 & x1, y2 & y1, z2 - z1)]
        if not (closed(math.inf, -math.inf) in x) and (len(x) == 2):
            table.append(box3D(x[0], y2, z2))
            table.append(box3D(x[1], y2, z2))
        else:
            table.append(box3D(x2 - x1, y2, z2))
        return table

    def iI_II_iI_II_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x2, y2, z2), box3D(x1, y1, z1 - z2)]
        return table

    def iII_I_iII_I_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        table = [box3D(x1, y1, z1), box3D(x2, y2, z2 - z1)]
        return table

    def iI_II_iII_I_oI_II(self, box1, box2):
        x1, y1, z1 = my_closed(box1.interval_x.lower, box1.interval_x.upper), \
                     my_closed(box1.interval_y.lower, box1.interval_y.upper), \
                     my_closed(box1.interval_z.lower, box1.interval_z.upper)
        x2, y2, z2 = my_closed(box2.interval_x.lower, box2.interval_x.upper), \
                     my_closed(box2.interval_y.lower, box2.interval_y.upper), \
                     my_closed(box2.interval_z.lower, box2.interval_z.upper)
        x = [x for x in x2 - x1]
        table = [box3D(x1, y1, z1), box3D(x2 & x1, y2 & y1, z2 - z1)]
        if not (closed(math.inf, -math.inf) in x) and (len(x) == 2):
            table.append(box3D(x[0], y2, z2))
            table.append(box3D(x[1], y2, z2))
        else:
            table.append(box3D(x2 - x1, y2, z2))
        return table
