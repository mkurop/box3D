import portion

class box3D:
    '''Klasa przechowująca instrukcje dot. pudełek'''

    def __init__(self, interval_x, interval_y, interval_z):
        '''
        :param interval_x: interwał opisujący położenie pudełka na płaszczyźnie x \n
        :param interval_y: interwał opisujący położenie pudełka na płaszczyźnie y \n
        :param interval_z: interwał opisujący położenie pudełka na płaszczyźnie z \n
        Inicjalizacja z interwałami x, y, z
        '''
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.interval_z = interval_z

    def get_interval_x(self):
        '''
        Funkcje get dla jednego z interwałów\n
        :return: interwał pudełka wskazujący położenie na osi x\n
        :rtype: portion.Interval
        '''
        return self.interval_x

    def get_interval_y(self):
        '''
        Funkcje get dla jednego z interwałów\n
        :return: interwał pudełka wskazujący położenie na osi y\n
        :rtype: portion.Interval
        '''
        return self.interval_y

    def get_interval_z(self):
        '''
        Funkcje get dla jednego z interwałów\n
        :return: interwał pudełka wskazujący położenie na osi z\n
        :rtype: portion.Interval
        '''
        return self.interval_z

    def __contains__(self, num):
        '''
        Funkcja sprawdzająca czy punkt jest w pudełku\n
        :param num: tablica zawierająca 3 wartości punktu sprawdzanego - x, y, z\n
        :rtype: bool
        '''
        return True if (num[0] in self.interval_x) & (num[1] in self.interval_y) & (num[2] in self.interval_z) else False

    def __ror__(self, num):
        '''
        Funkcja sprawdzająca czy punkt jest na granicy pudełek\n
        :param num: tablica zawierająca 3 wartości punktu sprawdzanego - x, y, z\n
        :rtype: bool
        '''
        x, y, z = num[0], num[1], num[2]
        is_on_border = x in set([self.interval_x.lower, self.interval_x.upper]) or y in set([self.interval_y.lower, self.interval_y.upper]) or z or set([self.interval_z.lower, self.interval_z.upper])
        is_inside_box = self.__contains__(num)
        return True if is_on_border & is_inside_box else False

    @staticmethod
    def factory(x1, y1, z1, x2, y2, z2):
        '''
        metoda statyczna tworząca pudełko na podstawie interwałów\n
        podanych w kolejności wszystkie lower, potem wszystkie upper\n
        :param x1: wartość lower dla interwału na osi x\n
        :param y1: wartość lower dla interwału na osi y\n
        :param z1: wartość lower dla interwału na osi z\n
        :param x2: wartość upper dla interwału na osi x\n
        :param y2: wartość upper dla interwału na osi y\n
        :param z2: wartość upper dla interwału na osi z\n
        :return: nowy obiekt pudełko\n
        :rtype: box3D
        '''
        return box3D(portion.closed(x1, x2), portion.closed(y1, y2), portion.closed(z1, z2))

def my_closed(lower, upper):
    '''
    Funkcja tworząca interwał zastępująca oryginalny closed\n
    :param lower: wartość lower dla nowo powstającego interwału\n
    :param upper: wartość upper dla nowo powstającego interwału\n
    :return: nowy interwał o dodanych właściwościach\n
    :rtype: myInterval
    '''
    return myInterval.from_atomic(portion.const.Bound.CLOSED, lower, upper, portion.const.Bound.CLOSED)

class myInterval(portion.Interval):
    eps = 1e-7
    '''
    Klasa dziedzicząca z funkcji interwał\n
    :param eps: liczba potrzebna do przycięcia pudełek,
    bez tego są liczone jako przecinające się nawet jak
    tylko nachodzą na siebie granicami
    '''

    @property
    def upper_eps(self):
        '''
        :return: wartość upper interwału + eps(ilon)\n
        :rtype: complex
        '''
        return self.upper + self.eps

    @property
    def upper_meps(self):
        '''
        :return: wartość upper interwału - eps(ilon)\n
        :rtype: complex
        '''
        return self.upper - self.eps

    @property
    def lower_eps(self):
        '''
        :return: wartość lower interwału + eps(ilon)\n
        :rtype: complex
        '''
        return self.lower + self.eps

    @property
    def lower_meps(self):
        '''
        :return: wartość lower interwału - eps(ilon)\n
        :rtype: complex
        '''
        return self.lower - self.eps

    @lower_eps.setter
    def lower_eps(self):
        '''
        Funkcja set dla wartości lower\n
        :return: wartość lower interwału + eps(ilon)\n
        :rtype: complex
        '''
        self.lower_eps = self.lower + self.eps

    @lower_meps.setter
    def lower_meps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower interwału - eps(ilon)\n
        :rtype: complex
        '''
        self.lower_meps = self.lower + self.eps

    @upper_eps.setter
    def upper_eps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper interwału + eps(ilon)\n
        :rtype: complex
        '''
        self.upper_eps = self.upper + self.eps

    @upper_meps.setter
    def upper_meps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper interwału - eps(ilon)\n
        :rtype: complex
        '''
        self.upper_meps = self.upper + self.eps

    @lower_eps.getter
    def get_lower_eps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower_eps(ilon)\n
        :rtype: complex
        '''
        return self.lower_eps

    @lower_meps.getter
    def get_lower_meps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower_meps(ilon)\n
        :rtype: complex
        '''
        return self.lower_meps

    @upper_eps.getter
    def get_upper_eps(self):
        '''
        Funkcja get dla wartości upper\n
        :return: wartość upper_eps(ilon)\n
        :rtype: complex
        '''
        return self.upper_eps

    @upper_meps.getter
    def get_upper_meps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper_meps(ilon)\n
        :rtype: complex
        '''
        return self.upper_meps

    def box_cut_execute(self, interval):
        '''
        Funkcja która przycina 1 interwał\n
        :param interval: interwał do przycięcia\n
        :return: interwał przycięty o epsilon z obu wartości granicznych\n
        :rtype: myInterval
        '''
        myInt = myInterval(interval)
        interval = my_closed(myInt.get_lower_eps, myInt.get_upper_meps)
        return interval

    def box_cut(self, box1):
        '''
        Funkcja przycinająca pudełko\n
        :param box1: pudełko przed przycięciem\n
        :return: pudełko po przycięciu\n
        :rtype: box3D
        '''
        x = self.box_cut_execute(box1.interval_x)
        y = self.box_cut_execute(box1.interval_y)
        z = self.box_cut_execute(box1.interval_z)
        box = box3D(x, y, z)
        return box

    def box_uncut_execute(self, interval):
        '''
        Funkcja która cofa przycięcie 1 interwału\n
        :param interval: interwał przycięty o epsilon, produkt funkcji box_cut_execute\n
        :return: interwał w stanie takim samym jak przed przycięciem\n
        :rtype: myInterval
        '''
        myInt = myInterval(interval)
        interval = my_closed(myInt.get_lower_meps, myInt.get_upper_eps)
        return interval

    def box_uncut(self, box1):
        '''
        Funkcja cofająca przycięcie pudełka\n
        :param box1: pudełko, w którym chcemy cofnąć przycięcie interwałów o epsilon\n
        :return: pudełko z cofniętym przycięciem interwałów\n
        :rtype: box3D
        '''
        x = self.box_uncut_execute(box1.interval_x)
        y = self.box_uncut_execute(box1.interval_y)
        z = self.box_uncut_execute(box1.interval_z)
        box = box3D(x, y, z)
        return box
