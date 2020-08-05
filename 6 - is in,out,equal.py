import portion
class algorytm:
    def is_in(self, interval1, interval2):
        return True if (interval2 == (interval1 & interval2) and interval1!=interval2) else False
    def is_equal(self, interval1, interval2):
        return True if interval1==interval2 else False
    def is_out(self, interval1, interval2):
        return False if (interval2 in (interval1 & interval2)) else True

algorytmTest = algorytm()
interval1, interval2 =  portion.closed(int(input()),int(input())), portion.closed(int(input()),int(input()))
print('\nIs in: ', algorytmTest.is_in(interval1, interval2), '\nIs equal: ', algorytmTest.is_equal(interval1, interval2), '\nIs out: ', algorytmTest.is_out(interval1, interval2))
