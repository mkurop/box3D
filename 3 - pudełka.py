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
        def __init__(self, num1, num2, num3, num4, num5, num6):
                self.box3d = interval([num1,num2],[num3, num4],[num5, num6])
        def get_box3d(self):
                return self.box3d
class boxStack:
        def __init__(self):
                self.stack = []
        def get_stack(self):
                return self.stack
        def AddToStack(self, element):
                self.stack.extend(element)
        def RemoveFromStack(self):
                return self.stack.pop()
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
                return None

        #początek funkcji głównej
        def algorytm(Q, tree):
                q = []
                iD=0
                #główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
                while not len(Q)==0:
                        #komenda pop
                        q = Q.RemoveFromStack()
                        print(q,Q)
                        #sprawdzanie czy w drzewie pudełko q się przecina
                        if tree.intersection((q(-1))):
                                #zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                                i = list(tree.intersection((q)))[0]
                                #dodanie na koniec zbioru Q "rozbitego" pudełka q
                                Q.AddToStack(rozbij(q.astype(np.int), i))
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
        Q.set_Stack.AddToStack((int(num) for num in input('\nPodaj 6 liczb dla jednego z pudełek oddzielone spacją oraz przecinkiem: ').split()))

algorytm(Q, tree())
