from cut_box import *

class Slice:
    def slice_boxes(self, box_list):
        sliced_x, sliced_y, sliced_z, sliced_boxes = [], [], [], []
        for box in box_list:
            x, y, z, box_temp = self.slice_box(box)
            sliced_x.extend(x)
            sliced_y.extend(y)
            sliced_z.extend(z)
            sliced_boxes.extend(box_temp)
        return sliced_x, sliced_y, sliced_z, sliced_boxes

    def slice_box(self, box):
        my_int = myInterval()
        box = my_int.box_uncut(box)
        sliced_x, sliced_y, sliced_z = [], [], []
        if self.x_sliceable(box):
            sliced_x.extend(self.x_slice(box))
            box = self.x_cut_off(box)
        if self.y_sliceable(box):
            sliced_y.extend(self.y_slice(box))
            box = self.y_cut_off(box)
        if self.z_sliceable(box):
            sliced_z.extend(self.z_slice(box))
            box = self.z_cut_off(box)
        return sliced_x, sliced_y, sliced_z, [box]

    def x_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower >= 2 else False

    def x_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.lower + 1),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.upper - 1, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))

        return [slice_lower, slice_upper]

    def y_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower >= 2 else False

    def y_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.lower + 1),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.upper - 1, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def z_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower >= 2 else False

    def z_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.lower + 1))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.upper - 1, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def x_cut_off(self, box):
        return box3D(my_closed(box.interval_x.lower + 1, box.interval_x.upper - 1), box.interval_y, box.interval_z)

    def y_cut_off(self, box):
        return box3D(box.interval_x, my_closed(box.interval_y.lower + 1, box.interval_y.upper - 1), box.interval_z)

    def z_cut_off(self, box):
        return box3D(box.interval_x, box.interval_y, my_closed(box.interval_z.lower + 1, box.interval_z.upper - 1))

