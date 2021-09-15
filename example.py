#przykładowy program należy wywołać wewnątrz katalogu ./boxes3D
from mainalgo import *
#import głównego modułu
table = []
#deklaracja tablicy zawierającej pudełka na wejściu do algorytmu
table.append(box3D.factory(0, 0, 0, 4, 4, 1))
table.append(box3D.factory(2, 2, 0, 6, 6, 1))
print(table[0])
print(table[1])
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
for box_list in pudelka:
    for box in box_list:
        print(box, "box={0}, wall={1}, edge={2}, point={3} \n".format(box.box, box.wall, box.edge, box.point))
    #wypisanie pudełek na wyjściu programu
