#!/usr/bin/env python3
import os
import rtree
import math
from portion import closed, closedopen, openclosed
# Notatka, bo nie przyjmuje nie zmienionego kodu
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

    def extend(self, added):
        self.stack.extend(added)

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
    def permute(self, sortin, permutation):
        assert len(sortin) == len(permutation)
        return [sortin[i] for i in permutation]

    def my_sort(self, inputlist):
        inputlist = zip(inputlist, range(len(inputlist)))
        aux = sorted(inputlist, key = lambda x:x[0])
        sorted2in = [aux[i][1] for i in range(len(aux))]
        list2 = zip(sorted2in, range(len(sorted2in)))
        aux1 = sorted(list2, key = lambda x:x[0])
        in2sorted = [aux1[i][1] for i in range(len(aux1))]
        sort = [aux[i][0] for i in range(len(aux))]
        return sort, in2sorted, sorted2in

    def divide_in(self, int1, int2):
        return [int1 | int2]

    def divide_half_out(self, int1, int2):
        up, low = (int1.upper, int2.upper), (int1.lower, int2.lower)
        if int2.lower == int1.lower:
            return [closed(min(low), min(up)), openclosed(min(up), max(up))]
        else:
            return [closed(min(low), max(low)), openclosed(max(low), max(up))]

    def divide_out(self, int1, int2):
        inter = int1 & int2
        return [int1 - inter, inter, int2 - inter]

    def divide_equal(self, int1, int2):
        return [closedopen(int1.lower, math.floor(int1.upper/2)), openclosed(math.floor(int2.upper/2), int2.upper)]

    def is_in(self, interval1, interval2):
        union = interval1 & interval2
        return True if ((union == interval1) ^ (union == interval2)) and (interval2.lower != interval1.lower and interval1.upper != interval2.upper)  else False

    def is_equal(self, interval1, interval2):
        return True if interval1 == interval2 else False

    def is_out(self, interval1, interval2):
        return True if (interval1.lower != interval2.lower) and (interval2.upper != interval1.upper) and (interval1 & interval2) else False

    def is_separate(self, int1, int2):
        return False if int1 & int2 else True

    def is_half_out(self, int1, int2):
        return True if ((int1.lower == int2.lower) ^ (int2.upper == int1.upper)) and ((int2 == int2 & int1) ^ (int1 == int1 & int2)) else False

    def rozbijanie(self, q, i):
        if self.is_in(q, i):
            return self.divide_in(q, i)
        elif self.is_out(q, i):
            return self.divide_out(q, i)
        elif self.is_half_out(q, i):
            return self.divide_half_out(q, i)
        elif self.is_equal(q, i):
            return self.divide_equal(q, i)
        elif self.is_separate(q, i):
            return q

    def rozbij(self, q, i):
        return self.canonical(q.interval_x, q.interval_y, q.interval_z, i.interval_x, i.interval_y, i.interval_z)

    def canonical_execute(self, inter_q, inter_i):
        if self.is_in(inter_q, inter_i):
            return 0
        elif self.is_half_out(inter_q, inter_i):
            return 1
        elif self.is_equal(inter_q, inter_i):
            return 2
        elif self.is_out(inter_q, inter_i):
            return 3
        elif self.is_separate(inter_q, inter_i):
            return 4
            #1  2  3  3  5  7
            #2  3  2  4  7  7

    def canonical_int(self, interval, interval_i):
        results = []
        if self.is_in(interval, interval_i):
            results.extend(self.divide_in(interval, interval_i))
        elif self.is_equal(interval, interval_i):
            results.extend(self.divide_equal(interval, interval_i))
        elif self.is_half_out(interval, interval_i):
            results.extend(self.divide_half_out(interval, interval_i))
            results[1] = closed(results[1].lower + 1, results[1].upper)
        elif self.is_out(interval, interval_i):
            results.extend(self.divide_out(interval, interval_i)) if interval.lower < interval_i.lower else results.extend(self.divide_out(interval_i, interval))
            results[0] = closed(results[0].lower, results[0].upper - 1)
            results[2] = closed(results[2].lower + 1, results[2].upper)
        else:
            results.extend(interval)
        return results


        '''
        if out:
            return [self.divide_out(swap_small, swap_big)]
        elif half_out:
            return [self.divide_half_out(swap_small, swap_big)]
        elif equal:
            return [self.divide_equal(swap_small, swap_big)]
        else:
            return [self.divide_in(swap_big, swap_small)]
        '''
        '''
        if self.is_out(interval_small, interval_big):
            if interval_small.upper > interval_big.upper:
                interval_small = closed(interval_big.upper + 1, interval_small.upper) if (abs(interval_small.upper - interval_big.upper) > 0) or (abs(interval_small.upper + interval_big.upper) < 0) else closed(interval_big.upper, interval_small.upper)
            else:
                interval_small = closed(interval_small.lower, interval_big.lower - 1) if (abs(interval_big.lower - interval_small.lower) > 0) or (abs(interval_big.lower + interval_small.lower) < 0) else closed(interval_small.lower, interval_big.lower)
        else:
            if interval_big.lower > interval_small.lower:
                interval_small = closed(interval_small.lower, interval_big.lower - 1) if (abs(interval_big.lower - interval_small.lower) > 0) or (abs(interval_big.lower + interval_small.lower) < 0) else closed(interval_small.lower, interval_big.lower)
            elif interval_big.lower < interval_small.lower and interval_big.upper < interval_small.upper :
                interval_small = closed(interval_small.upper + 1, interval_big.upper) if (abs(interval_big.upper - interval_small.upper) > 0) or (abs(interval_big.upper + interval_small.upper) < 0) else closed(interval_small.upper, interval_big.upper)

            elif interval_big.upper > interval_small.upper:
                interval_small = closed(interval_big.upper + 1, interval_small.upper) if (abs(interval_small.upper - interval_big.upper) > 0) or (abs(interval_small.upper + interval_big.upper) < 0) else closed(interval_big.upper, interval_small.upper)
            else:
                interval_small = closed(interval_big.lower, interval_small.lower - 1) if (abs(interval_small.lower - interval_big.lower) > 0) or (abs(interval_small.lower + interval_big.lower) < 0) else closed(interval_big.lower, interval_small.lower)
        '''
        '''
        max_t = False
        swap_temp_s, swap_temp_b = swap_small.copy(), swap_big.copy()
        if (interval_small.lower < interval_big.lower) and (interval_small.upper > interval_big.upper):
            max_t = True
            interval_backup_s = interval_small
            interval_backup_b = interval_big
            interval_small, interval_big = interval_backup_b, interval_small
            interval_big = closed(interval_big.lower, interval_small.lower)
        elif (interval_small.lower > interval_big.lower) and (interval_small.upper < interval_big.upper):
            interval_big = closed(interval_small.lower, interval_big.upper)
        interval_small = interval_big - interval_small
        if swap_small[j] == swap_big[j]:
            swap_small[j], swap_small[j + 1] = interval_small.lower - 1, interval_small.upper
        elif swap_small[j + 1] == swap_big[j + 1]:
            swap_small[j], swap_small[j + 1] = interval_small.lower, interval_small.upper + 1
        
        if self.is_half_out(interval_small, interval_big):
            if swap_small[j + 1] < swap_big[j] and swap_small[j] < swap_big[j]:
                swap_small[j + 1] = swap_big[j] - 1
            elif swap_small[j + 1] > swap_big[j + 1] and swap_small [j] >= swap_big[j + 1]:
                swap_small[j] = swap_big[j + 1] + 1
        elif self.is_out(interval_small, interval_big):
            if swap_small[j + 1] < swap_big[j]:
                swap_small[j + 1] = swap_big[j] - 1
            else:
                swap_small[j] = swap_big[j + 1] + 1

        if interval_small != interval_big:
            interval_small = interval_small - interval_big

        if max_t:
            temp1, temp2 = swap_small.copy()[j], swap_small.copy()[j + 1]
            swap_small, swap_big = temp2, temp1
            #            swap_small[j], swap_small[j + 1] = temp1, temp2
        '''

    def canonical_box(self, table):
        for i in range(3):
            if i == len(table):
                table.append(table[- 1])
            elif i == len(table) + 1:
                table.append(table[i - 2])
            elif not table[i]:
                table.append(table[i - 1]) if i > 0 else table.append(table[i + 1]) if table[i + 1] else table.append(table[i + 2])
        return table

    def equal_boxes(self, table1, table2):
        return True if table1[0] == table2[0] and table1[1] == table2[1] and table1[2] == table2[2] else False

    def canonical(self, inter_x, inter_y, inter_z, inter_x_i, inter_y_i, inter_z_i):
        results1, results2, results3, boxes = [], [], [], []
        results1.extend(self.canonical_int(inter_x, inter_x_i))
        results2.extend(self.canonical_int(inter_y, inter_y_i))
        results3.extend(self.canonical_int(inter_z, inter_z_i))
        results1 = self.canonical_box(results1)
        results2 = self.canonical_box(results2)
        results3 = self.canonical_box(results3)
        boxes.append(box3D(results1[0], results2[0], results3[0]))
        if not self.equal_boxes(results1, results2):
            boxes.append(box3D(results1[1], results2[1], results3[1]))
        if not (self.equal_boxes(results1, results3) and self.equal_boxes(results2, results3)):
            boxes.append(box3D(results1[2], results2[2], results3[2]))
        print(results1, '\n', results2, '\n', results3, '\n')
        return boxes

        '''
        x, y, z, x_o, y_o, z_o, x_e, y_e, z_e = False, False, False, False, False, False, False, False, False
        list_q = [inter_x, inter_y, inter_z]
        list_i = [inter_x_i, inter_y_i, inter_z_i]
        list_q_new = []
        swap_small, swap_big = list_q.copy(), list_i.copy()
        if any([self.is_out(inter_x, inter_x_i), self.is_out(inter_y, inter_y_i), self.is_out(inter_z, inter_z_i)]):
            if self.is_out(inter_x, inter_x_i):
                x = True
            if self.is_half_out(inter_x, inter_x_i):
                x_o = True
            if self.is_out(inter_y, inter_y_i):
                y = True
            if self.is_half_out(inter_y, inter_y_i):
                y_o = True
            if self.is_out(inter_z, inter_z_i):
                z = True
            if self.is_half_out(inter_z, inter_z_i):
                z_o = True
            if self.is_equal(inter_x, inter_x_i):
                x_e = True
            if self.is_equal(inter_y, inter_y_i):
                y_e = True
            if self.is_equal(inter_z, inter_z_i):
                z_e = True
            if True in [x, y, z] or True in [x_o, y_o, z_o] or True in [x_e, y_e, z_e]:
                sorted_vars, from_before, from_after = self.my_sort([x, y, z])
                sorted_o, from_before_o, from_after_o = self.my_sort([x_o, y_o, z_o])
                sorted_e, from_before_e, from_after_e = self.my_sort([x_e, y_e, z_e])
                results1, results2, results3 = [], [], []
                vars = [x, y, z]
                if sorted_vars[0]:
                    results1.extend(i for i in self.canonical_box(swap_small[from_before[0]], swap_big[from_before[0]], True, False, False)[0])
                elif sorted_o[0]:
                    results1.extend(i for i in self.canonical_box(swap_small[from_before[0]], swap_big[from_before[0]], False, True, False)[0])
                elif sorted_e[0]:
                    results1.extend(i for i in self.canonical_box(swap_small[from_before[0]], swap_big[from_before[0]], False, False, True)[0])
                else:
                    results1.extend(i for i in self.canonical_box(swap_small[from_before[0]], swap_big[from_before[0]], False, False, False,)[0])
                if sorted_vars[1]:
                    results2.extend(i for i in self.canonical_box(swap_small[from_before[1]], swap_big[from_before[1]], True, False, False)[0])
                elif sorted_o[1]:
                    results2.extend(i for i in self.canonical_box(swap_small[from_before[1]], swap_big[from_before[1]], False, True, False)[0])
                elif sorted_e[1]:
                    results2.extend(i for i in self.canonical_box(swap_small[from_before[1]], swap_big[from_before[1]], False, False, True)[0])
                else:
                    results2.extend(i for i in self.canonical_box(swap_small[from_before[1]], swap_big[from_before[1]], False, False, False)[0])
                if sorted_vars[2]:
                    results3.extend(i for i in self.canonical_box(swap_small[from_before[2]], swap_big[from_before[2]], True, False, False)[0])
                elif sorted_o[2]:
                    results3.extend(i for i in self.canonical_box(swap_small[from_before[2]], swap_big[from_before[2]], False, True, False)[0])
                elif sorted_e[2]:
                    results2.extend(i for i in self.canonical_box(swap_small[from_before[1]], swap_big[from_before[1]], False, False, True)[0])
                else:
                    results3.extend(i for i in self.canonical_box(swap_small[from_before[2]], swap_big[from_before[2]], False, False, False)[0])
            else:
                return []
            for i in range(max((len(results3)), len(results2), len(results1))):
                if results1[i] == closed(math.inf, -math.inf) and i < len(results1) - 1:
                    x = results1[i + 1] if results1[i + 1] != closed(math.inf, -math.inf) else results1[i + 2]
                elif results1[-1] == closed(math.inf, -math.inf) and i > len(results1) - 1:
                    x = results1[-3] if results1[-2] == closed(math.inf, -math.inf) else results1[-2]
                else:
                    x = results1[i] if len(results1) - 1 >= i else results1[-1]
                if results2[i] == closed(math.inf, -math.inf) and i < len(results2) - 1:
                    y = results2[i + 1] if results2[i + 1] != closed(math.inf, -math.inf) else results2[i + 2]
                elif results2[-1] == closed(math.inf, -math.inf) and i > len(results2) - 1:
                    y = results2[-3] if results2[-2] == closed(math.inf, -math.inf) else results2[-2]
                else:
                    y = results2[i] if len(results2) - 1 >= i else results2[-1]
                if results3[i] == closed(math.inf, -math.inf) and i < len(results3) - 1:
                    z = results3[i + 1] if results3[i + 1] != closed(math.inf, -math.inf) else results3[i + 2]
                elif results3[-1] == closed(math.inf, -math.inf) and i > len(results1) - 1:
                    z = results3[-3] if results3[-2] == closed(math.inf, -math.inf) else results3[-2]
                else:
                    z = results1[i] if len(results1) - 1 >= i else results1[-1]
                for j in range(max((len(results3)), len(results2), len(results1))):
                    if j < len(x) and x[j + 1] != closed(max.inf, -math.inf) and x[j] != closed(max.inf, -math.inf) and x[j] & x[j + 1]:
                        x[j] -= x[j + 1] & x[j]
                        x[j].closed(int(x[j].lower), x[j].upper - 1)
                    if j < len(y) and y[j + 1] != closed(max.inf, -math.inf) and y[j] != closed(max.inf, -math.inf) and y[j] & y[j]:
                        y[j] -= y[j + 1] & y[j]
                        y[j].closed(int(y[j].lower), y[j].upper - 1)

                    if j < len(z) and z[j + 1] != closed(max.inf, -math.inf) and z[j] != closed(max.inf, -math.inf) and z[j] & z[j]:
                        z[j] -= z[j + 1] & z[j]
                        z[j].closed(int(z[j].lower), z[j].upper - 1)
                x[j].closed(x[j].lower, x[j].upper)
                y[j].closed(y[j].lower, y[j].upper)
                z[j].closed(z[j].lower, z[j].upper)
                print(x, y, z)
                boxes.append(box3D(x[j], y[j], z[j]))
            '''


    @staticmethod
    # początek funkcji głównej
    def algorytm(Q, tree):
        iD = 0
        alg = algorytm()
        # główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
        while not len(Q.get_stack()) == 0:
            # komenda pop
            q = Q.pop()
            # sprawdzanie czy w drzewie pudełko q się przecina
            if list(tree.tree.intersection(([q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper]), True)):
                # zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                i = list(tree.tree.intersection((q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper), True))[0]
                inter = [item for item in i.bbox]
                i = box3D.factory(inter[0], inter[1], inter[2], inter[3], inter[4], inter[5])
                #print(q.interval_x, q.interval_y, q.interval_z)
                divided = alg.rozbij(q, i)
                Q.extend(divided)
            else:
                #print(q.interval_x, q.interval_y, q.interval_z)
                # w przeciwnym wypadku dodanie do drzewa nowego pudełka
                tree.tree.insert(iD, [q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper, q.interval_z.upper])
                # zwiększenie zmiennej iD
                iD += 1
        # wypisanie drzewa
        lista = tree.tree.intersection(tree.tree.get_bounds(), True)
        lista = [(item.bbox)for item in lista]
        print('\n')
        for i in lista:
            print([i[0], i[3]], end = '') if i[0] != i[3] else print([i[0]], end = '')
            print(' x ', end = '')
            print([i[1], i[4]], end = '') if i[1] != i[4] else print([i[1]], end = '')
            print(' x ', end = '')
            print([i[2], i[5]], end = '\n') if i[2] != i[5] else print([i[2]], end = '\n')
        #zwrócenie drzewa
        return tree.tree


Q = boxStack()


pudelka = int(input('Ile pudełek?: '))
for i in range(pudelka):
    # (int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielonput()), int(input()), int(input()), ine spacją oraz przecinkiem: '))
    Q.append(box3D.factory(int(input("Podaj po jednej z sześciu współrzędnych pudełka oddzielonych enterem: \n")), int(input()), int(input()), int(input()), int(input()), int(input())))
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
