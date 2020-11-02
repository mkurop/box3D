import os, sys
sys.path.insert(0, os.path.abspath('..'))
from mainalgo import *
#import głównego modułu
Q = boxStack()
table = []
#deklaracja stosu, tablicy pomocnej i liczby pudełek
table.append(box3D.factory(2, 1, 4, 5, 7, 8))
table.append(box3D.factory(1, 2, 3, 3, 5, 7))
table.append(box3D.factory(2, 3, 2, 4, 7, 7))
#tworzenie pudełek (funkcja factory ma kolejność współrzędnych x_lower y_lower z_lower x_upper, y_upper, z_upper)
#w kolejności x_lower, y_lower, z_lower, x_upper, y_upper, z_upper
for i in table:
    i.__str__()
    print('\n')
#wypisywanie pudełek przed wstawieniem ich do drzewa
pudelka = algorithm.execute(table)
#uruchomienie funkcji execute i rozbicie pudełek
for i in pudelka:
    print(i.__str__())
    #wypisanie pudełek końcowych
