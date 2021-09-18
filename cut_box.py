import portion
from math import inf
from collections import namedtuple
import random

Atomic = namedtuple('Atomic', ['left', 'lower', 'upper', 'right'])


class box3D:
    '''Klasa przechowująca instrukcje dot. pudełek'''

    def __init__(self, interval_x, interval_y, interval_z, wall=False, edge=False, point=False):
        '''
        :param interval_x: interwał opisujący położenie pudełka na płaszczyźnie x \n
        :param interval_y: interwał opisujący położenie pudełka na płaszczyźnie y \n
        :param interval_z: interwał opisujący położenie pudełka na płaszczyźnie z \n
        Inicjalizacja z interwałami x, y, z
        '''
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.interval_z = interval_z
        self.wall = wall
        self.edge = edge
        self.point = point
        self.box = True if sum([not self.wall, not self.edge, not self.point]) == 3 else False

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
        return True if (num[0] in self.interval_x) & (num[1] in self.interval_y) & (
                num[2] in self.interval_z) else False

    def __ror__(self, num):
        '''
        Funkcja sprawdzająca czy punkt jest na granicy pudełek\n
        :param num: tablica zawierająca 3 wartości punktu sprawdzanego - x, y, z\n
        :rtype: bool
        '''
        x, y, z = num[0], num[1], num[2]
        is_on_border = x in {self.interval_x.lower, self.interval_x.upper} or y in {self.interval_y.lower,
                                                                                    self.interval_y.upper} or z in {
                           self.interval_z.lower, self.interval_z.upper}
        is_inside_box = self.__contains__(num)
        return True if is_on_border & is_inside_box else False

    def __str__(self):
        '''
        Funkcja wypisująca interwały pudełka
        '''
        x = self.get_interval_x()
        y = self.get_interval_y()
        z = self.get_interval_z()
        lista = [x.lower, x.upper, y.lower, y.upper, z.lower, z.upper]
        intervals = '[' + str(lista[0]) + ',' + str(lista[1]) + ']' + ' x ' + '[' + str(lista[2]) + ',' + str(
            lista[3]) + ']' + ' x ' + '[' + str(lista[4]) + ',' + str(lista[5]) + ']' + '\n'
        return intervals

    @staticmethod
    def random(corner_range=100, side_range=20):
        """
        Generuje losowe pudełko, w którym interwały są determinowane przez pseudolosowe liczby całkowite z przedziału podanego przez użytkownika \n
        :param corner_range: dolna granica każdego interwału pudełka jest liczbą pseudolosową z przedziału  [0, corner_range]\n
        :param side_range: górna granica każdego interwału pudełka jest liczbą pseudolosową z przedziału [1 + corner_range, side_range + corner_range]\n
        :return: losowe pudełko\n
        :rtype: box3D
        """
        side_x, side_y, side_z = random.randint(1, side_range), random.randint(1, side_range), random.randint(1,
                                                                                                              side_range)
        corner_x, corner_y, corner_z = random.randint(0, corner_range), random.randint(0, corner_range), random.randint(
            0, corner_range)
        return box3D(my_closed(corner_x, corner_x + side_x), my_closed(corner_y, corner_y + side_y),
                     my_closed(corner_z, corner_z + side_z))

    @staticmethod
    def factory(x1, y1, z1, x2, y2, z2, wall=False, edge=False, point=False):
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
        return box3D(portion.closed(x1, x2), portion.closed(y1, y2), portion.closed(z1, z2), wall=wall, edge=edge,
                     point=point)


def my_closed(lower, upper):
    '''
    Funkcja tworząca interwał zastępująca oryginalny closed\n
    :param lower: wartość lower dla nowo powstającego interwału\n
    :param upper: wartość upper dla nowo powstającego interwału\n
    :return: nowy interwał o dodanych właściwościach\n
    :rtype: myInterval
    '''
    return myInterval.my_from_atomic(portion.const.Bound.CLOSED, lower, upper, portion.const.Bound.CLOSED)


class myInterval(portion.Interval):
    '''
    Klasa dziedzicząca z funkcji interwał\n
    :param eps: liczba potrzebna do przycięcia pudełek, bez tego są liczone jako przecinające się nawet jak tylko nachodzą na siebie granicami\n
    '''

    def __init__(self):
        super().__init__()
        self.eps = 1e-7

    @property
    def upper_eps(self):
        '''
        Atrybut upper_eps\n
        :return: górną  granicę interwału + eps(ilon)\n
        :rtype: float
        '''
        return self.upper + self.eps

    @property
    def upper_meps(self):
        '''
        Atrybut upper_meps\n
        :return: górną  granicę interwału - eps(ilon)\n  
        :rtype: float
        '''
        return self.upper - self.eps

    @property
    def lower_eps(self):
        '''
        Atrybut lower_eps\n
        :return: dolną  granicę interwału + eps(ilon)\n
        :rtype: float        
        '''
        return self.lower + self.eps

    @property
    def lower_meps(self):
        '''
        Atrybut lower_meps\n
        :return: dolną  granicę interwału - eps(ilon)\n
        :rtype: float
        '''
        return self.lower - self.eps

    @lower_eps.setter
    def lower_eps(self):
        '''
        Funkcja set dla wartości lower\n
        :return: wartość lower interwału + eps(ilon)\n
        :rtype: float
        '''
        self.lower_eps = self.lower + self.eps

    @lower_meps.setter
    def lower_meps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower interwału - eps(ilon)\n
        :rtype: float
        '''
        self.lower_meps = self.lower - self.eps

    @upper_eps.setter
    def upper_eps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper interwału + eps(ilon)\n
        :rtype: float
        '''
        self.upper_eps = self.upper + self.eps

    @upper_meps.setter
    def upper_meps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper interwału - eps(ilon)\n
        :rtype: float
        '''
        self.upper_meps = self.upper - self.eps

    @lower_eps.getter
    def get_lower_eps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower_eps(ilon)\n
        :rtype: float
        '''
        return self.lower_eps

    @lower_meps.getter
    def get_lower_meps(self):
        '''
        Funkcja get dla wartości lower\n
        :return: wartość lower_meps(ilon)\n
        :rtype: float
        '''
        return self.lower_meps

    @upper_eps.getter
    def get_upper_eps(self):
        '''
        Funkcja get dla wartości upper\n
        :return: wartość upper_eps(ilon)\n
        :rtype: float
        '''
        return self.upper_eps

    @upper_meps.getter
    def get_upper_meps(self):
        '''
        Funkcja set dla wartości upper\n
        :return: wartość upper_meps(ilon)\n
        :rtype: float
        '''
        return self.upper_meps

    def box_cut_execute(self, myInt):
        '''
        Funkcja która przycina jeden interwał\n
        :param interval: interwał do przycięcia\n
        :return: interwał przycięty o epsilon z obu wartości granicznych\n
        :rtype: myInterval
        '''
        interval = my_closed(myInt.get_lower_eps, myInt.get_upper_meps)
        return interval

    def box_cut(self, box1):
        '''
        Funkcja przycinająca pudełko\n
        :param box1: pudełko przed przycięciem\n
        :return: pudełko po przycięciu\n
        :rtype: box3D
        '''
        x, y, z = box1.interval_x, box1.interval_y, box1.interval_z
        x = my_closed(x.lower, x.upper)
        y = my_closed(y.lower, y.upper)
        z = my_closed(z.lower, z.upper)
        x = self.box_cut_execute(x) if not x.empty else x
        y = self.box_cut_execute(y) if not y.empty else y
        z = self.box_cut_execute(z) if not z.empty else z
        box = box3D(x, y, z)
        return box

    def box_uncut_execute(self, myInt):
        '''
        Funkcja która cofa przycięcie jednego interwału\n
        :param interval: interwał przycięty o epsilon, produkt funkcji box_cut_execute\n
        :return: interwał w stanie takim samym jak przed przycięciem\n
        :rtype: myInterval
        '''
        if myInt == my_closed(inf, -inf):
            interval = myInt
        else:
            interval = my_closed(round(myInt.lower), round(myInt.upper))
        return interval

    def box_uncut(self, box1):
        '''
        Funkcja cofająca przycięcie pudełka\n
        :param box1: pudełko, w którym chcemy cofnąć przycięcie interwałów o epsilon\n
        :return: pudełko z cofniętym przycięciem interwałów\n
        :rtype: box3D
        '''
        x, y, z = box1.interval_x, box1.interval_y, box1.interval_z
        x = my_closed(x.lower, x.upper)
        y = my_closed(y.lower, y.upper)
        z = my_closed(z.lower, z.upper)
        x = self.box_uncut_execute(x)
        y = self.box_uncut_execute(y)
        z = self.box_uncut_execute(z)
        box = box3D(x, y, z)
        return box

    @staticmethod
    def my_from_atomic(left, lower, upper, right):
        '''
    	Funkcja nadpisująca funkcję from_atomic\n
    	:return: interwał na podstawie podanych danych\n
    	:rtype: myInterval
    	'''
        instance = myInterval()
        left = left if lower not in [inf, -inf] else portion.Bound.OPEN
        right = right if upper not in [inf, -inf] else portion.const.Bound.OPEN
        instance._intervals = [Atomic(left, lower, upper, right)]
        if instance.empty:
            return myInterval()
        return instance
