#import bibliotek
import numpy as np
import os
import rtree
from interval import interval
#usuwanie plików z poprzedniego działania programu
try:
        os.remove('3d_index.idx')
        os.remove('3d_index.dat')
except:
        pass
class box:
        def __init__(self, interval_x, interval_y, interval_z):
                self.interval_x=interval_x
                self.interval_y=interval_y
                self.interval_z=interval_z
        def get_interval_x(self):
                return self.interval_x
        def get_interval_y(self):
                return self.interval_y
        def get_interval_z(self):
                return self.interval_z
        @staticmethod
        def factory(self,x1,x2,y1,y2,z1,z2):
                return box(interval([x1, x2]),interval([y1,y2]), interval([z1,z2]))
class boxStack:
        def __init__(self):
                self.stack = []
        def get_stack(self):
                return self.stack
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
                if(q.get_interval_x in i.get_interval_x):
                        if(q.get_interval_y in i.get_interval_x):  #jeśli wszystkie na siebie nachodzą
                                if(q.get_interval_z in i.get_interval_z):
                                else:                              #jeśli tylko 2 na siebie nachodzą (x oraz y)
                        elif(q.get_interval_y in i.get_interval_y):
                                if(q.get_interval_z in i.get_interval_z):#jeśli y oraz z na siebie nachodzą
                                else:                                   #jeśli tylko y na siebie nachodzi
                        elif(q.get_interval_z in i.get_interval_z):     #jeśli tylko z na siebie nachodzą
                        else:                                           #każdy inny przypadek


                #rozbijanie pudełek
                return None

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

Q=boxStack()
#pętla do wczytywania współrzędnych dla każdego pudełka i
for i in range(pudelka):
        Q.extend(box.factory(int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielone spacją oraz przecinkiem: ').split().sep(' ')))

algorytm(Q, tree())
