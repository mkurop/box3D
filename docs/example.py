#przykładowy program należy wywołać wewnątrz katalogu ./Praktyki
from mainalgo import *
#import głównego modułu
table = []
#deklaracja tablicy pomocnej
table.append(box3D.factory(2, 1, 4, 5, 7, 8))
table.append(box3D.factory(1, 2, 3, 3, 5, 7))
table.append(box3D.factory(2, 3, 2, 4, 7, 7))
#tworzenie pudełek (funkcja factory ma kolejność współrzędnych x_lower y_lower z_lower x_upper, y_upper, z_upper)
#w kolejności x_lower, y_lower, z_lower, x_upper, y_upper, z_upper
for box in table:
    print(box)
    print('\n')
#wypisywanie pudełek przed wstawieniem ich do drzewa
pudelka = algorithm.execute(table)
#uruchomienie funkcji execute i rozbicie pudełek
for box in pudelka:
    print(box)
    #wypisanie pudełek końcowych
