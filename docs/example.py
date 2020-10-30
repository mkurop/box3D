Q = boxStack()
table = []
pudelka = int(input())
#deklaracja stosu, tablicy pomocnej i liczby pudełek
for i in range(pudelka):
    table.append(box3D.factory(int(input()), int(input()), int(input()), int(input()), int(input()), int(input())))
#pętla tworząca pudełka na podstawie podanych danych
#w kolejności x_lower, y_lower, z_lower, x_upper, y_upper, z_upper
Q.extend(table)
#dodanie pudełek do stosu
algorithm().algorytm(Q, tree())
#uruchomienie algorytmu i rozbicie pudełek

