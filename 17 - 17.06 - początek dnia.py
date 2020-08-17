import os
import rtree
import itertools as it
from portion import closed, closedopen, openclosed, open, empty
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

class algorytm:
    def divide_in(self, int1, int2):
        return int1 | int2
    def divide_half_out(self, int1, int2):
        up, low = (int1.upper, int2.upper), (int1.lower, int2.lower)
        if int2.lower==int1.lower:
            return closed(min(low), min(up)), openclosed(min(up), max(up))
        else:
            return closed(min(low), max(low)), openclosed(max(low)+1, max(up))
    def divide_out(self, int1, int2):
        inter = int1 & int2
        return int1 - (inter), inter ,int2 - (inter)
    def is_in(self, interval1, interval2):
        return True if interval1 & interval2 == min(interval2, interval1) else False
    def is_equal(self, interval1, interval2):
        return True if interval1==interval2 else False
    def is_out(self, interval1, interval2):
        return True if (interval1 & interval2)!=(interval1|interval2) and any(interval1&interval2)  else False
    def is_separate(self, int1, int2):
        return False if any(int1 & int2) else True
    def rozbijanie(self, q, i):
        if self.is_in(q, i):
            return self.divide_in(q,i)
        elif self.is_out(q, i):
            return self.divide_out(q,i)
        elif self.is_equal(q, i):
            return self.divide_half_out(q,i)
        elif self.is_separate(q, i):
            return q
    def rozbij(self, q, i):
        x, y, z = self.rozbijanie(q.interval_x, i.interval_x), self.rozbijanie(q.interval_y, i.interval_y), self.rozbijanie(q.interval_z, i.interval_z)
        print(list(it.combinations_with_replacement([x,y,z],3)))

    @staticmethod
    # początek funkcji głównej
    def algorytm(Q, tree):
        iD = 0
        # główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
        while not len(Q.get_stack()) == 0:
            # komenda pop
            q = Q.pop()
            # sprawdzanie czy w drzewie pudełko q się przecina
            if list(tree.tree.intersection([q.interval_x.lower,q.interval_y.lower,q.interval_z.lower, q.interval_x.upper,q.interval_y.upper,q.interval_z.upper])):
                # zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                i = list(tree.tree.intersection((q.interval_x.lower, q.interval_y.lower,q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper), True))
                inter = [item for item in i[0].bounds]
                i = box3D.factory(inter[0],inter[1],inter[2],inter[3],inter[4],inter[5])
                # dodanie na koniec zbioru Q "rozbitego" pudełka q
                divided = [i for i in algorytm().rozbij(q, i)]
                print(divided)
                Q.append(box3D(divided))
            else:
                #print(q.interval_x, q.interval_y, q.interval_z)
                # w przeciwnym wypadku dodanie do drzewa nowego pudełka
                tree.tree.insert(iD, [q.interval_x.lower, q.interval_y.lower,q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper])
                # zwiększenie zmiennej iD
                iD += 1
        # wypisanie drzewa
        lista = list(tree.tree.intersection(tree.tree.get_bounds(),True))
        lista = [(item.bbox)for item in lista]
        for i in lista:
            print([i[0],i[3]],'x', [i[1], i[4]],'x',[i[2],i[5]],'\n')
        # zwrócenie drzewa
        return tree.tree

###pudelka = int(input('\nIle pudełek?\n'))
Q = boxStack()
# pętla do wczytywania współrzędnych dla każdego pudełka i
pudelka = int(input('Ile pudełek?: '))
for i in range(pudelka):
    # (int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielonput()), int(input()), int(input()), ine spacją oraz przecinkiem: '))
    Q.append(box3D.factory(int(input("Podaj po jednej z sześciu współrzędnych pudełka oddzielonych enterem:\n")), \
                           int(input()), int(input()), int(input()), int(input()), int(input())))
algorytm.algorytm(Q, tree())


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
