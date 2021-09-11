#przykładowy program należy wywołać wewnątrz katalogu ./boxes3D
from mainalgo import *
#import głównego modułu
table = []
#deklaracja tablicy zawierającej pudełka na wejściu do algorytmu
table.append(box3D.factory(0, 0, 0, 4, 4, 1))
table.append(box3D.factory(2, 2, 0, 6, 6, 1))
#  table.append(box3D.factory(2, 3, 2, 4, 7, 7))
#tworzenie pudełek (funkcja factory ma kolejność współrzędnych x_lower y_lower z_lower x_upper, y_upper, z_upper)
#w kolejności x_lower, y_lower, z_lower, x_upper, y_upper, z_upper
#  for box in table:
    #  print(box)
    #  print('\n')
#wypisywanie pudełek przed wstawieniem ich do drzewa
pudelka = algorithm.execute(table)
#uruchomienie funkcji execute i rozbicie pudełek
print("Wynik")
for box in pudelka:
    print(box)
    #wypisanie pudełek na wyjściu programu
