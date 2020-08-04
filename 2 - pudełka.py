#import bibliotek
import numpy as np
import os
import rtree
#usuwanie plików z poprzedniego działania programu
try:
        os.remove('3d_index.idx')
        os.remove('3d_index.dat')
except:
        pass
class boxStack:
        def __init__(self, attr_1 = None, attr_2 = None, attr_3 = None, attr_4 = None, attr_5 = None, attr_6 = None):
                self.attr_1 = attr_1
                self.attr_2 = attr_2
                self.attr_3 = attr_3
                self.attr_4 = attr_4
                self.attr_5 = attr_5
                self.attr_6 = attr_6
        def get_attr_1(self):
                return self.attr_1
        def set_attr_1(self, attr):
                self.attr_1=attr
        def get_attr_2(self):
                return self.attr_2
        def set_attr_2(self,attr):
                self.attr_2=attr
        def get_attr_3(self):
                return self.attr_3
        def set_attr_3(self, attr):
                self.attr_3=attr
        def get_attr_4(self):
                return self.attr_4
        def set_attr_4(self,attr):
                self.attr_4=attr
        def get_attr_5(self):
                return self.attr_5
        def set_attr_5(self, attr):
                self.attr_5=attr
        def get_attr_6(self):
                return self.attr_6
        def set_attr_6(self,attr):
                self.attr_6=attr


class tree:
        def __init__(self):
                #tworzenie drzewa
                self.properties = rtree.index.Property()
                #ustawienia drzewa
                self.properties.dimension = 3
                self.tree = rtree.index.Index('3d_index', properties = self.properties)
        def get_tree(self):
                return self.tree
        def set_tree(self, new_tree):
                self.tree=new_tree
class algorytm:
        #funkcja rozbij
        def rozbij(self, q, i):
                #rozbijanie pudełek
                if([q.attr_1, q.attr_2]==[i.attr_1, i.attr_2] and [q.attr_3, q.attr_4] == [i.attr_3, i.attr_4] and [q.attr_5, q.attr_6] == [i.attr_5, i.attr_6]):
                        return None
                elif([q.attr_1, q.attr_2]==[i.attr_1, i.attr_2]):
                        if([q.attr_3, q.attr_4]==[i.attr_3, i.attr_4]):
                                return [boxStack(q.attr_1,q.attr_2, q.attr_5, q.attr_6), boxStack(q.attr_3, q.attr_4, q.attr_5, q.attr_6), boxStack(q.attr_3, q.attr_4, q.attr_1, q.attr_2)]
                        elif([q.attr_5, q.attr_6]==[i.attr_5, i.attr_6]):
                                return []
                        else:

                elif([q.attr_3, q.attr_4]==[i.attr_3, i.attr_4]):

                        if([q.attr_5, q.attr_6]==[i.attr_5, i.attr_6]):

                        else:

                elif([q.attr_5, q.attr_6]==[i.attr_5, i.attr_6]])

                else:

        #początek funkcji głównej
        def algorytm(Q, tree):
                q = []
                iD=0
                #główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
                while not len(Q)==0:
                        #komenda pop
                        q = Q.pop()
                        print(q,Q)
                        #sprawdzanie czy w drzewie pudełko q się przecina
                        if tree.intersection((q(-1))):
                                #zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                                i = list(tree.intersection((q)))[0]
                                #dodanie na koniec zbioru Q "rozbitego" pudełka q
                                Q.extend(rozbij(q.astype(np.int), i))
                        else:
                                #w przeciwnym wypadku dodanie do drzewa nowego pudełka
                                tree.insert(iD, list(int(num) for num in q))
                                print(tree.intersection(q))
                                #zwiększenie zmiennej iD
                                iD+=1
                        #wypisanie drzewa
                        print(tree)
                        #zwrócenie drzewa
                        return tree
#zmienna, która wskazuje ile chcemy pudełek wprowadzić
pudelka=int(input('\nIle pudełek?\n'))

Q=[]
#pętla do wczytywania współrzędnych dla każdego pudełka i
for i in range(pudelka):
        Q[i] = boxStack()
        Q[i].attr_1, Q[i].attr_2, Q[i].attr_3, Q[i].attr_4, Q[i].attr_5, Q[i].attr_6 \
                = (int(num) for num in input('\nPodaj liczby dla jednego z pudełek oddzielone spacją oraz przecinkiem: ').split())

algorytm(Q, tree())
