import rtree
from portion import closed
from cut_box import box3D


class boxStack:
    '''
    Klasa przechowująca dane\n
    stosu pudełek z wejścia programu
    '''

    def __init__(self):
        '''Stos pudełek'''
        self.stack = []

    def empty(self):
        '''
        Czy pusty stos?\n
        :return: informację czy stos jest pusty\n
        :rtype: bool
        '''
        return not bool(self.get_stack())

    def get_stack(self):
        '''
        Funkcja get stosu\n
        :return: Obecny stos\n
        :rtype: boxStack
        '''
        return self.stack

    def set_stack(self, new_stack):
        '''
        Funkcja set stosu \n
        :param new_stack: aktualizowanie stanu stosu
        '''
        self.stack = new_stack

    def extend(self, added):
        '''
        Funkcje extend stosu\n
        :param added: element, który posłuży do rozszerzenia stosu o nowe elementy
        '''
        self.stack.extend(added)

    def pop(self):
        '''
        Funkcje pop stosu\n
        :return: stos pomniejszony o ostatni element\n
        :rtype: boxStack
        '''
        return self.stack.pop()


class tree:
    '''Klasa przechowująca instrukcje drzewa'''

    def __init__(self):
        '''Tworzenie drzewa'''
        self.properties = rtree.index.Property()
        self.properties.dimension = 3
        self.tree = rtree.index.Index('3d_index', properties=self.properties)

    def get_tree(self):
        '''
        Funkcje get drzewa\n
        :return: drzewo rtree na którym algorytm główny zamieszcza pudełka\n
        :rtype: rtree
        '''
        return self.tree

    def set_tree(self, new_tree):
        '''
        Funkcje set drzewa\n
        :param new_tree: nowe drzewo
        '''
        self.tree = new_tree

    def ret_boxes(self):
        '''
    	Funkcja zwracająca pudełka w drzewie
    	:return: pudełka znajdujące się w drzewie
    	:rtype: list
    	'''
        boxes, elem_ret, boxes_ret, walls_ret, edges_ret, points_ret = \
            self.tree.intersection(self.tree.get_bounds(), True), [], [], [], [], []
        for item in boxes:
            if item.object.wall:
                walls_ret.append(item.bbox)
            elif item.object.edge:
                edges_ret.append(item.bbox)
            elif item.object.point:
                points_ret.append(item.bbox)
            else:
                boxes_ret.append(item.bbox)

        boxes = [box3D.factory(int(round(item[0])), int(round(item[1])), int(round(item[2])),
                               int(round(item[3])), int(round(item[4])), int(round(item[5]))) for item in boxes_ret]
        walls_ret = [box3D.factory(int(round(item[0])), int(round(item[1])), int(round(item[2])),
                                   int(round(item[3])), int(round(item[4])), int(round(item[5])), True)
                     for item in walls_ret]
        edges_ret = [box3D.factory(int(round(item[0])), int(round(item[1])), int(round(item[2])),
                                   int(round(item[3])), int(round(item[4])), int(round(item[5])), False, True)
                     for item in edges_ret]
        points_ret = [box3D.factory(int(round(item[0])), int(round(item[1])), int(round(item[2])),
                                    int(round(item[3])), int(round(item[4])), int(round(item[5])), False, False, True)
                      for item in points_ret]
        elem_ret.append(boxes)
        elem_ret.append(walls_ret)
        elem_ret.append(edges_ret)
        elem_ret.append(points_ret)
        return elem_ret
