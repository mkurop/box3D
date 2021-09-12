import os, sys
from collections import defaultdict

sys.path.insert(0, os.path.abspath('.'))
from signatures_setup import *
from split_intervals import *
from cut_box import *
from preparing_boxes import Slice

try:
    os.remove('3d_index.idx')
    os.remove('3d_index.dat')
except:
    pass
'''
Usuwanie poprzednich plików drzewa,
inaczej błąd kompilacji, bo python
próbuje zapisać coś co już jest
'''

#główna klasa całego programu
class algorithm:
    '''
    Główna klasa programu.
    '''
    def rotate_and_execute(self, box1, box2):
        '''
        Funkcja obraca pudełka zmieniając kolejność interwałów \n
        :param box1: pudełko ze stosu \n
        :param box2: pudełko z drzewa \n
        :return: lista table, która zawiera pudełka po rozbiciach \n
        :rtype: list
        '''
        sign = signatures()
        spl = split()
        idx_sign = sign.get_signatures_triple(box1, box2)
        sort, in2sorted, sorted2in = sign.my_sort(idx_sign)
        tri_sign = sign.permute([box1.interval_x, box1.interval_y, box1.interval_z], in2sorted)
        tri_sign_i = sign.permute([box2.interval_x, box2.interval_y, box2.interval_z], in2sorted)
        tri_sign, tri_sign_i = box3D(tri_sign[0], tri_sign[1], tri_sign[2]), box3D(tri_sign_i[0], tri_sign_i[1],
                                                                                   tri_sign_i[2])

        split_sign = spl.split(tuple(sort), tri_sign, tri_sign_i)
        table = sign.ret_original_order(split_sign, sorted2in)
        return table

    @staticmethod
    def append_wall_to_tree(iD, wall_list, tree):
        wall = wall_list.pop()
        tree.tree.add(iD, (wall.interval_x.lower, wall.interval_y.lower, wall.interval_z.lower,
                           wall.interval_x.upper, wall.interval_y.upper, wall.interval_z.upper), wall)
        return tree, wall_list, iD

    @staticmethod
    def execute(box_list):
        '''
        Funkcja statyczna, która przyjmuje listę pudełek i zwraca listę rozbitych pudełek\n
        :param box_list: lista pudełek do rozbicia\n
        :return: lista pudełek po rozbiciu\n
        :rtype: list
        '''
        Q, drzewo = boxStack(), tree()
        Q.extend(box_list)
        algorithm().algorytm(Q, drzewo)
        return drzewo.ret_boxes()


    @staticmethod
    def algorytm(Q, tree):
        '''
        Funkcja statyczna, w wyniku której wszystkie przecinające się pudełka ze stosu zostają rozbite i wstawione do drzewa\n

        :param Q: stos pudełek\n
        :param tree: puste drzewo z indeksowaniem w trzech wymiarach\n
        :return: drzewo rtree zawierające pudełka\n
        :rtype: tree.tree
        '''
        #obiekt klasy myInterval
        my_int, my_slice = myInterval(), Slice()
        #zmienna potrzebna do wprowadzania pudełka w unikalne miejsce do drzewa
        iD = 0
        #pętla działa dopóki stos nie zostanie pusty
        while not Q.empty():
            #zdjęcie ostatniego pudełka ze stosu i przycięcie go
            q = Q.pop()
            while q.interval_x == my_closed(inf, -inf) or q.interval_y == my_closed(inf, -inf) or q.interval_z == my_closed(inf, -inf):
                q = Q.pop()
            if tree.tree.count((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper)) > 0:
                '''
                Sprawdzenie czy pudełko q przecina się z którymkolwiek elementem z drzewa.
                Jeśli tak, pudełko przecinające się zostaje pobrane z drzewa i usunięte,
                zaś wynik rozbicia zostaje wstawiony ponownie na stos pudełek
                '''
                i = list(tree.tree.intersection((q.interval_x.lower,  q.interval_y.lower, q.interval_z.lower, q.interval_x.upper, q.interval_y.upper,  q.interval_z.upper), objects=True))[0]
                inter = [i.object.interval_x, i.object.interval_y, i.object.interval_z]
                j = box3D(inter[0], inter[1], inter[2])
                q = my_int.box_uncut(q)
                j = my_int.box_uncut(j)
                #cofnięcie przycięcia dla pudełek które mają być rozbite
                q = [my_int.box_cut(i) for i in algorithm().rotate_and_execute(q, j)]
                Q.extend(q)
                #wprowadzenie wyniku rozbicia na stos
                tree.tree.delete(i.id, (i.bbox[0], i.bbox[1], i.bbox[2], i.bbox[3], i.bbox[4], i.bbox[5]))
                #usunięcie starego pudełka z drzewa
            else:
                tree.tree.add(iD, (q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper,
                                   q.interval_y.upper, q.interval_z.upper), q)
                #dodanie nowego pudełka do drzewa i zwiększenie zmiennej iD o 1
                iD += 1

        wall_stack = []
        wall_stack.extend([box.object for box in tree.tree.intersection((tree.tree.bounds[0], tree.tree.bounds[1],
                                                            tree.tree.bounds[2], tree.tree.bounds[3],
                                                            tree.tree.bounds[4], tree.tree.bounds[5]),
                                                             objects=True)])

        wall_yz_dict, wall_xz_dict, wall_xy_dict = defaultdict(list), defaultdict(list), defaultdict(list)
        for box in wall_stack:
            while not any([my_slice.x_sliceable(box), my_slice.y_sliceable(box), my_slice.z_sliceable(box)]):
                # TUTAJ BłĄD - ZłE ROZBIJANIE ŚCIANEK
                wall_yz, wall_xz, wall_xy, wall_stack = my_slice.slice_boxes(wall_stack)
                wall_yz_dict, wall_xz_dict, wall_xy_dict = my_slice.sort_sliced_walls(wall_yz, wall_yz_dict), \
                                                           my_slice.sort_sliced_walls(wall_xz, wall_xz_dict), \
                                                           my_slice.sort_sliced_walls(wall_xy, wall_xy_dict)
        print(wall_yz_dict)
        print(wall_xz_dict)
        print(wall_xy_dict)
        wall_yz_prepared = my_slice.prepare_walls_for_tree(wall_yz_dict)
        wall_xz_prepared = my_slice.prepare_walls_for_tree(wall_xz_dict)
        wall_xy_prepared = my_slice.prepare_walls_for_tree(wall_xy_dict)

        while any([len(wall_xy_prepared) != 0, len(wall_xz_prepared) != 0, len(wall_yz_prepared) != 0]):
            if len(wall_xy_prepared) != 0:
                tree, wall_xy_prepared, iD = algorithm.append_wall_to_tree(iD, wall_xy_prepared, tree)
                iD += 1
            if len(wall_xz_prepared) != 0:
                tree, wall_xz_prepared, iD = algorithm.append_wall_to_tree(iD, wall_xz_prepared, tree)
                iD += 1
            if len(wall_yz_prepared) != 0:
                tree, wall_yz_prepared, iD = algorithm.append_wall_to_tree(iD, wall_yz_prepared, tree)
                iD += 1



