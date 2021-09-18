import math
import os, sys
from mainalgo import algorithm
sys.path.append('..')
from split_intervals import split 
import portion
from cut_box import *
from signatures_setup import split as TEST
from portion import closed, closedopen, openclosed
from cut_box import myInterval
from preparing_boxes import Slice
#unit testy
import random as rnd
import unittest
class algorithm_check(unittest.TestCase):

    out_interval_bigger = closed(3, 6)
    interval_smaller = closed(2, 5)
    in_interval_bigger = closed(1, 6)
    tst = TEST()

    def random_point_from_a_box(self, box):
        num_x = rnd.randint(box.interval_x.lower, box.interval_x.upper)
        num_y = rnd.randint(box.interval_y.lower, box.interval_y.upper)
        num_z = rnd.randint(box.interval_z.lower, box.interval_z.upper)
        return [num_x, num_y, num_z]

    def loop_test(self, boxes_in, boxes_out):
        b = rnd.choice(boxes_in)
        x = self.random_point_from_a_box(b)
        num_in = sum([b.__contains__(x) for b in boxes_out])
        num_boundary = sum([b.__ror__(x) for b in boxes_out])
        if (num_in == 1) or (num_in >= num_boundary >= 0):
            return True
        else:
            if num_in != 1 & num_in != num_boundary:
                print('\ncontains error')
            else:
                print('\n__ror__ error')
            print('\n', b.interval_x, b.interval_y, b.interval_z, '\n', x)
            return False

    def point_is_in(self, b, x):
        return True if all([self.point_is_in_x(b, x), self.point_is_in_y(b, x), self.point_is_in_z(b, x)]) else False

    def point_is_in_x(self, b, x):
        return True if x[0] >= b.interval_x.lower >= x[0] else False

    def point_is_in_y(self, b, x):
        return True if x[1] >= b.interval_y.lower >= x[1] else False

    def point_is_in_z(self, b, x):
        return True if x[2] >= b.interval_z.lower >= x[2] else False

    def point_is_ror(self, b, x):
        return sum([self.point_is_ror_x(b, x), self.point_is_ror_y(b, x), self.point_is_ror_z(b, x)])

    def point_is_ror_x(self, b, x):
        return True if x[0] == b.interval_x.lower or x[0] == b.interval_x.lower else False

    def point_is_ror_y(self, b, x):
        return True if x[1] == b.interval_y.lower or x[1] == b.interval_y.lower else False

    def point_is_ror_z(self, b, x):
        return True if x[2] == b.interval_z.lower or x[2] == b.interval_z.lower else False


    def evaluate(self, boxes_in, boxes_out, checks_num = 1000):
        for i in range(checks_num):
            if self.loop_test(boxes_in, boxes_out):
                continue
            else:
                return False
        return True

    def test_oI_II_oI_II_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.out_interval_bigger, self.out_interval_bigger, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().oI_II_oI_II_oI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_oI_II_oI_II_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.out_interval_bigger)
        box1 = box3D(self.out_interval_bigger, self.out_interval_bigger, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().oI_II_oI_II_oII_I(box0, box1)]
        self.assertEqual(True , self.evaluate([box0, box1], assert_box))
        
    def test_oI_II_oII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.out_interval_bigger, self.out_interval_bigger)
        box1 = box3D(self.out_interval_bigger, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().oI_II_oII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))
        
    def test_oII_I_oII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.out_interval_bigger, self.out_interval_bigger, self.out_interval_bigger)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().oII_I_oII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))
        
    def test_iI_II_iI_II_iI_II(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.in_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iI_II_iI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_iI_II_iII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.in_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iI_II_iII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_iII_I_iII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.in_interval_bigger, self.in_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iII_I_iII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iII_I_iII_I_iII_I(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.in_interval_bigger)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_iII_I_iII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_iI_II_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.out_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iI_II_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))
 
    def test_iII_I_oI_II_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.interval_smaller, self.out_interval_bigger, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_oI_II_oI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_oI_II_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.out_interval_bigger, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_oI_II_oI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_oI_II_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.out_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.out_interval_bigger, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_oI_II_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))


    def test_iII_I_oI_II_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.interval_smaller, self.out_interval_bigger)
        box1 = box3D(self.interval_smaller, self.out_interval_bigger, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_oI_II_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))


    def test_iII_I_oII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.out_interval_bigger, self.out_interval_bigger)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_oII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_oII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.out_interval_bigger, self.out_interval_bigger)
        box1 = box3D(self.in_interval_bigger, self.interval_smaller, self.interval_smaller)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_oII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_iII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.in_interval_bigger, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.interval_smaller, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))
        
    def test_iI_II_iI_II_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iI_II_oI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_iI_II_iII_I_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.interval_smaller, self.in_interval_bigger, self.interval_smaller)
        box1 = box3D(self.in_interval_bigger, self.interval_smaller, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iI_II_iII_I_oI_II(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))
        
    def test_iII_I_iII_I_oI_II(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.interval_smaller)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.out_interval_bigger)
        assert_box = [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_iII_I_oI_II(box0, box1)]
        self.assertEqual(True, self.evaluate([box0, box1], assert_box))
        
    def test_iII_I_iII_I_oII_I(self):
        my_int = myInterval()
        box0 = box3D(self.in_interval_bigger, self.in_interval_bigger, self.out_interval_bigger)
        box1 = box3D(self.interval_smaller, self.interval_smaller, self.interval_smaller)
        assert_box =  [my_int.box_uncut(temp_box) for temp_box in TEST().iII_I_iII_I_oII_I(box0, box1)]
        self.assertEqual(True ,self.evaluate([box0, box1], assert_box))

    def test_slice_box(self):
        Sliced = Slice()
        box = box3D.factory(rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(11, 20),
                            rnd.randint(11, 20), rnd.randint(11, 20))
        slice_list = []
        x, y, z, box_cut = Sliced.slice_box(box)
        slice_list.extend(x)
        slice_list.extend(y)
        slice_list.extend(z)
        slice_list.append(box_cut)
        self.assertEqual(True, self.evaluate([box], slice_list))

    def test_slice_boxes(self):
        Sliced, slice_list = Slice(), []
        box1 = box3D.factory(rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(11, 20),
                    rnd.randint(11, 20), rnd.randint(11, 20))
        box2 = box3D.factory(rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(11, 20),
                            rnd.randint(11, 20), rnd.randint(11, 20))
        box3 = box3D.factory(rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(1, 10), rnd.randint(11, 20),
                            rnd.randint(11, 20), rnd.randint(11, 20))
        x, y, z, box_ret = Sliced.slice_boxes([box1, box2, box3])
        slice_list.extend(x)
        slice_list.extend(y)
        slice_list.extend(z)
        slice_list.append(box_ret)
        self.assertEqual(True, self.evaluate([box1, box2, box3], slice_list))

    def test_walls(self):
        table = []
        for i in range(random.randint(30, 40), random.randint(41, 50)):
            table.append(box3D.random())
        boxes = algorithm.execute(table)
        boxes = [wall for wall in boxes[1] if wall.wall]
        self.assertEqual(True, self.evaluate(table, boxes))

    def test_edges(self):
        table = []
        for i in range(random.randint(30, 40), random.randint(41, 50)):
            table.append(box3D.random())
        boxes = algorithm.execute(table)
        boxes = [edge for edge in boxes[2] if edge.edge]
        self.assertEqual(True, self.evaluate(table, boxes))

    def test_points(self):
        table = []
        for i in range(random.randint(30, 40), random.randint(41, 50)):
            table.append(box3D.random())
        points = algorithm.execute(table)
        boxes = [box for box in points[0] if box.box]
        points = [point for point in points[3] if point.point]
        self.assertEqual(True, self.evaluate(table, points))

if __name__ == '__main__':
    unittest.main()
