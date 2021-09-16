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


# główna klasa całego programu
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
        # obiekt klasy myInterval
        my_int, my_slice = myInterval(), Slice()
        # zmienna potrzebna do wprowadzania pudełka w unikalne miejsce do drzewa
        iD = 0
        # pętla działa dopóki stos nie zostanie pusty
        while not Q.empty():
            # zdjęcie ostatniego pudełka ze stosu i przycięcie go
            q = Q.pop()
            while (q.interval_x == my_closed(inf, -inf) or q.interval_y == my_closed(inf,
                                                                                    -inf) or q.interval_z == my_closed(
                inf, -inf)) and len(Q.get_stack()) > 0:
                q = Q.pop()
            if tree.tree.count((q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper,
                                q.interval_y.upper, q.interval_z.upper)) > 0:
                '''
                Sprawdzenie czy pudełko q przecina się z którymkolwiek elementem z drzewa.
                Jeśli tak, pudełko przecinające się zostaje pobrane z drzewa i usunięte,
                zaś wynik rozbicia zostaje wstawiony ponownie na stos pudełek
                '''
                i = list(tree.tree.intersection((q.interval_x.lower, q.interval_y.lower, q.interval_z.lower,
                                                 q.interval_x.upper, q.interval_y.upper, q.interval_z.upper),
                                                objects=True))[0]
                inter = [i.object.interval_x, i.object.interval_y, i.object.interval_z]
                j = box3D(inter[0], inter[1], inter[2])
                q = my_int.box_uncut(q)
                j = my_int.box_uncut(j)
                # cofnięcie przycięcia dla pudełek które mają być rozbite
                q = [my_int.box_cut(i) for i in algorithm().rotate_and_execute(q, j)]
                Q.extend(q)
                # wprowadzenie wyniku rozbicia na stos
                tree.tree.delete(i.id, (i.bbox[0], i.bbox[1], i.bbox[2], i.bbox[3], i.bbox[4], i.bbox[5]))
                # usunięcie starego pudełka z drzewa
            else:
                tree.tree.add(iD, (q.interval_x.lower, q.interval_y.lower, q.interval_z.lower, q.interval_x.upper,
                                   q.interval_y.upper, q.interval_z.upper), q)
                # dodanie nowego pudełka do drzewa i zwiększenie zmiennej iD o 1
                iD += 1

        wall_stack = []
        wall_stack.extend([box.object for box in tree.tree.intersection((tree.tree.bounds[0], tree.tree.bounds[1],
                                                                         tree.tree.bounds[2], tree.tree.bounds[3],
                                                                         tree.tree.bounds[4], tree.tree.bounds[5]),
                                                                        objects=True)])
        box_num = 0
        wall_yz_dict, wall_xz_dict, wall_xy_dict = defaultdict(list), defaultdict(list), defaultdict(list)
        for box in wall_stack:
            box = my_int.box_uncut(box)
            while mylen(box.interval_x) >= 1 or mylen(box.interval_y) >= 1 or mylen(box.interval_z) >= 1:
                wall_yz, wall_xz, wall_xy, box = my_slice.slice_boxes([box])
                wall_yz_dict, wall_xz_dict, wall_xy_dict = my_slice.sort_sliced_walls_yz(wall_yz, wall_yz_dict), \
                                                           my_slice.sort_sliced_walls_xz(wall_xz, wall_xz_dict), \
                                                           my_slice.sort_sliced_walls_xy(wall_xy, wall_xy_dict)
        wall_yz_prepared = my_slice.prepare_walls_for_tree_x(wall_yz_dict)
        wall_xz_prepared = my_slice.prepare_walls_for_tree_y(wall_xz_dict)
        wall_xy_prepared = my_slice.prepare_walls_for_tree_z(wall_xy_dict)
        edge_xyz_dict, edge_xy_dict, edge_yz_dict, edge_xz_dict = defaultdict(list), defaultdict(list),\
                                                                  defaultdict(list), defaultdict(list)
        prepared_edges, edges = [], []
        for wall in wall_yz_prepared:
            while sum([mylen(wall.interval_x) == 0, mylen(wall.interval_y) == 0, mylen(wall.interval_z) == 0]) < 2:
                edge, wall = my_slice.slice_wall(wall)
                edges.append(edge)
        for wall in wall_xz_prepared:
            while sum([mylen(wall.interval_x) == 0, mylen(wall.interval_y) == 0, mylen(wall.interval_z) == 0]) < 2:
                edge, wall = my_slice.slice_wall(wall)
                edges.append(edge)
        for wall in wall_xy_prepared:
            while sum([mylen(wall.interval_x) == 0, mylen(wall.interval_y) == 0, mylen(wall.interval_z) == 0])< 2:
                edge, wall = my_slice.slice_wall(wall)
                edges.append(edge)
        edge_dict_xyz, edge_dict_xy, edge_dict_yz, edge_dict_xz = \
            my_slice.sort_sliced_edges(edges, edge_xyz_dict, edge_xy_dict, edge_yz_dict, edge_xz_dict)
        edges_xyz, edges_xy, edges_xz, edges_yz = my_slice.prepare_sliced_edges_x(edge_dict_xyz), \
                                                    my_slice.prepare_sliced_edges_x(edge_dict_xy), \
                                                    my_slice.prepare_sliced_edges_x(edge_dict_xz), \
                                                                  my_slice.prepare_sliced_edges_y(edge_dict_xz)
        while any([len(wall_xy_prepared) != 0, len(wall_xz_prepared) != 0,
                   len(wall_yz_prepared) != 0, len(edges_xyz) != 0, len(edges_xy) != 0, len(edges_xz) != 0,
                   len(edges_yz) != 0]):
            if len(wall_xy_prepared) != 0:
                tree, wall_xy_prepared, iD = algorithm.append_wall_to_tree(iD, wall_xy_prepared, tree)
                iD += 1
            if len(wall_xz_prepared) != 0:
                tree, wall_xz_prepared, iD = algorithm.append_wall_to_tree(iD, wall_xz_prepared, tree)
                iD += 1
            if len(wall_yz_prepared) != 0:
                tree, wall_yz_prepared, iD = algorithm.append_wall_to_tree(iD, wall_yz_prepared, tree)
                iD += 1
            if len(edges_xyz) != 0:
                tree, edges_xyz, iD = algorithm.append_wall_to_tree(iD, edges_xyz, tree)
                iD += 1
            if len(edges_xy) != 0:
                tree, edges_xy, iD = algorithm.append_wall_to_tree(iD, edges_xy, tree)
                iD += 1
            if len(edges_yz) != 0:
                tree, edges_yz, iD = algorithm.append_wall_to_tree(iD, edges_yz, tree)
                iD += 1
            if len(edges_xz) != 0:
                tree, edges_xz, iD = algorithm.append_wall_to_tree(iD, edges_xz, tree)
                iD += 1


