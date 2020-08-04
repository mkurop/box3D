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
class drzewo:

        def __init__(self):
                #tworzenie drzewa
                self.properties = rtree.index.Property()
                #ustawienia drzewa
                self.properties.dimension = 3
                self.tree = rtree.index.Index('3d_index', properties = self.properties)
                #zmienna id potrzebna do wprowadzania danych do drzewa
                self.iD=0
                self.Q=[]
                self.dodatkowePudelka=[]
        #funkcja rozbij
        def rozbij(self, q, i):
                #usuwanie elementów, które się powtarzają

                #zwracanie zedytowanego q
                return q
        #początek funkcji głównej
        def algorytm(self, Q):
                #tworzenie
                q = []
                #główna pętla trwająca do skrócenia długości wejściowego zbioru do wartości 0
                while not len(self.Q)==0:
                        #komenda pop
                        q = self.Q.pop()
                        print(q,Q)
                        #sprawdzanie czy w drzewie pudełko q się przecina
                        if self.tree.intersection((q(-1))):
                                #zwrócenie z drzewa pierwszego obiektu, z którym pudełko się przecina
                                self.i = list(self.tree.intersection((q)))[0]
                                #dodanie na koniec zbioru Q "rozbitego" pudełka q
                                self.Q.append(self.rozbij(q.astype(np.int), i))
                        else:
                                #w przeciwnym wypadku dodanie do drzewa nowego pudełka
                                self.tree.insert(self.iD, list(int(num) for num in q))
                                print(self.tree.intersection(q))
                                #zwiększenie zmiennej iD
                                self.iD+=1
                #wypisanie drzewa
                print(self.tree)
                #zwrócenie drzewa
                return self.tree
#zmienna, która wskazuje ile chcemy pudełek wprowadzić
pudelka=int(input('\nIle pudełek?\n'))
#macierz zer o rozmiarze równym ilości pudełek x 6 (gdyż każde pudełko ma 6 współrzędnych)
Q = []
#pętla do wczytywania współrzędnych dla każdego pudełka i
for i in range(pudelka):
        Q.append(int(num) for num in input('\nPodaj liczby dla jednego z pudełek oddzielone spacją oraz przecinkiem: ').split())
drzewko = drzewo()
drzewko.algorytm(Q)
