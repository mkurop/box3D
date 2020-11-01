Q = boxStack()
table = []
pudelka = int(input())
#deklaracja stosu, tablicy pomocnej i liczby pudełek
table.append(box3D.factory(2, 1, 4, 5, 7, 8))
table.append(box3D.factory(1, 2, 3, 3, 5, 7))
table.append(box3D.factory(2, 3, 2, 4, 7, 7))
#tworzenie pudełek (funkcja factory ma kolejność współrzędnych x_lower y_lower z_lower x_upper, y_upper, z_upper)
#w kolejności x_lower, y_lower, z_lower, x_upper, y_upper, z_upper
Q.extend(table)
#dodanie pudełek do stosu
algorithm().algorytm(Q, tree())
#uruchomienie algorytmu i rozbicie pudełek

