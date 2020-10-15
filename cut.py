import portion

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
        return box3D(portion.closed(x1, x2), portion.closed(y1, y2), portion.closed(z1, z2))


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


    @lower_eps.setter
    def lower_eps(self):
        self.lower_eps = self.lower + self.eps

    @lower_meps.setter
    def lower_meps(self):
        self.lower_meps = self.lower + self.eps

    @upper_eps.setter
    def upper_eps(self):
        self.upper_eps = self.upper + self.eps

    @upper_meps.setter
    def upper_meps(self):
        self.upper_meps = self.upper + self.eps


    @lower_eps.getter
    def get_lower_eps(self):
        return self.lower_eps

    @lower_meps.getter
    def get_lower_meps(self):
        return self.lower_meps

    @upper_eps.getter
    def get_upper_eps(self):
        return self.upper_eps

    @upper_meps.getter
    def get_upper_meps(self):
        return self.upper_meps


    def box_cut_execute(self, interval):
        myInt = myInterval(interval)
        interval = my_closed(myInt.get_lower_eps, myInt.get_upper_meps)
        return interval

    def box_cut(self, box1):
        x = self.box_cut_execute(box1.interval_x)
        y = self.box_cut_execute(box1.interval_y)
        z = self.box_cut_execute(box1.interval_z)
        box = box3D(x, y, z)
        return box

    def box_uncut_execute(self, interval):
        myInt = myInterval(interval)
        interval = my_closed(myInt.get_lower_meps, myInt.get_upper_eps)
        return interval

    def box_uncut(self, box1):
        x = self.box_uncut_execute(box1.interval_x)
        y = self.box_uncut_execute(box1.interval_y)
        z = self.box_uncut_execute(box1.interval_z)
        box = box3D(x, y, z)
        return box