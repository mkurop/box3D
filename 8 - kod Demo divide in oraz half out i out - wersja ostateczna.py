from itertools import combinations_with_replacement
from math import floor, ceil
from portion import closed
class algorytm:
    def divide_in(self, inter1, inter2):
        return inter1 & inter2
    def divide_half_out(self, inter1, inter2):
        listin = [inter1.upper, inter1.lower, inter2.upper, inter2.lower]
        listin.sort()
        return closed(listin[0], floor((listin[0] + listin[3])/2)), closed(ceil((listin[0]+listin[3])/2),listin[3])
    def divide_out(self, inter1, inter2):
        listin = [inter1.upper, inter1.lower, inter2.upper, inter2.lower]
        listin.sort()
        return closed(listin[0], listin[1]), closed(listin[0], listin[1]) & closed(listin[1], listin[2]), closed(listin[1], listin[2])
algorytmTest = algorytm()
interval1, interval2 =  closed(int(input()),int(input())), closed(int(input()),int(input()))
print('\nDivide in: ', algorytmTest.divide_in(interval1, interval2), '\nDivide half out: ', algorytmTest.divide_half_out(interval1, interval2),'\nDivide out: ', algorytmTest.divide_out(interval1, interval2) )
