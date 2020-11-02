.. _Podstawowe_informacje:

Podstawowe informacje
=====================

Licencja
--------
Program jest udostępniany na licencji GNU General Public License
https://www.gnu.org/licenses/licenses.pl.html 

Założenia działania programu
----------------------------
Program bierze dowolną liczbę pudełek, które mogą się przecinać i zwraca pudełka nieprzecinające się mające jako unię, unię pudełek na wejściu

Przecinanie - pudełka przecinają się, jeżeli tworzące je interwały mają niepustą cześć wspólną dla osi x, y i z.

Rozbicie - jeśli dwa pudełka się przecinają, zostaje zwrócona niekoniecznie
taka sama liczba pudełek, które unię mają równą pudełkom przecinającym się,
lecz się nie przecinają. 

Przykład wywołania programu
---------------------------

.. literalinclude:: example.py
  


wyjście programu przykładowego:
  
.. literalinclude:: example-output.py
   

Układ współrzędnych kartezjańskich
----------------------------------
Jest to układ współrzędnych oparty na trzech osiach: x, y oraz z.
Więcej informacji 
https://en.wikipedia.org/wiki/Cartesian_coordinate_system

Interwały
---------
Interwał to odcinek o dwóch atrybutach granicznych.

Pudełka
-------
Pudełka to obiekty przedstawione przez trzy interwały, 
po jednym na każdą z osi. Można je sobie wyobrazić
jako zwykłe prostopadłościany.

Drzewo
------
Drzewo korzystające z 3-wymiarowych węzłów.

