import interval
class algorytm:
    def is_in(self, interval1, interval2):
        return True if all(interval1 | interval2) in interval1 and interval1!=interval2 else False
    def is_equal(self, interval1, interval2):
        return True if interval1==interval2 else False
    def is_out(self, interval1, interval2):
        return False if all(interval1 & interval2) in interval1 else True

algorytmTest = algorytm()
interval1, interval2 =  interval.interval(int(input()),int(input())), interval.interval(int(input()),int(input()))
print('\nIs in: ', algorytmTest.is_in(interval1, interval2), '\nIs equal: ', algorytmTest.is_equal(interval1, interval2), '\nIs out: ', algorytmTest.is_out(interval1, interval2))
