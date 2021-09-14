from cut_box import *
from collections import defaultdict


class Slice:

    def slice_boxes(self, box_list):
        sliced_yz, sliced_xz, sliced_xy, sliced_boxes = [], [], [], []
        for box in box_list:
            x, y, z, sliced_boxes = self.slice_box(box)
            sliced_yz.extend(x)
            sliced_xz.extend(y)
            sliced_xy.extend(z)
        return sliced_yz, sliced_xz, sliced_xy, sliced_boxes

    def slice_box(self, box):
        my_int = myInterval()
        box = my_int.box_uncut(box)
        sliced_yz, sliced_xz, sliced_xy = [], [], []
        if self.x_sliceable(box):
            sliced_yz.extend(self.x_slice(box))
            box = self.x_cut_off(box)
        if self.y_sliceable(box):
            sliced_xz.extend(self.y_slice(box))
            box = self.y_cut_off(box)
        if self.z_sliceable(box):
            sliced_xy.extend(self.z_slice(box))
            box = self.z_cut_off(box)
        if self.x_partially_sliceable(box):
            sliced_yz.append(self.x_part_slice(box))
            box = self.x_cut_off(box, True)
        if self.y_partially_sliceable(box):
            sliced_xz.append(self.y_part_slice(box))
            box = self.y_cut_off(box, True)
        if self.z_partially_sliceable(box):
            sliced_xy.append(self.z_part_slice(box))
            box = self.z_cut_off(box, True)

        return sliced_yz, sliced_xz, sliced_xy, box

    def sort_sliced_walls_yz(self, sliced, sorted_walls):
        for wall in sliced:
            sorted_walls[wall.interval_x.lower].append(wall)
        return sorted_walls

    def sort_sliced_walls_xz(self,  sliced, sorted_walls):
        for wall in sliced:
            sorted_walls[wall.interval_y.lower].append(wall)
        return sorted_walls


    def sort_sliced_walls_xy(self, sliced, sorted_walls):
        for wall in sliced:
            sorted_walls[wall.interval_z.lower].append(wall)
        return sorted_walls

    def prepare_walls_for_tree_x(self, wall_list):
        prepared_walls = []
        for key, value in wall_list.items():
            for box in value:
                wall = box3D(my_closed(box.interval_x.lower_meps, box.interval_x.upper_eps),
                                            box.interval_y, box.interval_z)
            prepared_walls.append(wall)
        return prepared_walls

    def prepare_walls_for_tree_y(self, wall_list):
        prepared_walls = []
        for key, value in wall_list.items():
            for box in value:
               wall = box3D(box.interval_x,
                                        my_closed(box.interval_y.lower_meps, box.interval_y.upper_eps),
                                        box.interval_z)
        prepared_walls.append(wall)
        return prepared_walls

    def prepare_walls_for_tree_z(self, wall_list):
        prepared_walls = []
        for key, value in wall_list.items():
            for box in value:
                wall = box3D(box.interval_x, box.interval_y,
                                            my_closed(box.interval_z.lower_meps, box.interval_z.upper_eps))
        prepared_walls.append(wall)
        return prepared_walls

    def x_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower >= 2 else False

    def x_partially_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower == 1 else False

    def x_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.lower),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.upper, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def x_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.lower),
                           my_closed(box.interval_y.lower, box.interval_y.upper),
                           my_closed(box.interval_z.lower, box.interval_z.upper))
        return slice_wall

    def y_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower >= 2 else False

    def y_partially_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower == 1 else False

    def y_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.lower),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.upper, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def y_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                           my_closed(box.interval_y.lower, box.interval_y.lower),
                           my_closed(box.interval_z.lower, box.interval_z.upper))
        return slice_wall

    def z_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower >= 2 else False

    def z_partially_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower == 1 else False

    def z_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.lower))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.upper, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def z_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                           my_closed(box.interval_y.lower, box.interval_y.upper),
                           my_closed(box.interval_z.lower, box.interval_z.lower))
        return slice_wall

    def x_cut_off(self, box, part=False):
        if part:
            return box3D(my_closed(box.interval_x.lower + 1, box.interval_x.upper), box.interval_y, box.interval_z)
        else:
            return box3D(my_closed(box.interval_x.lower + 1, box.interval_x.upper - 1), box.interval_y, box.interval_z)

    def y_cut_off(self, box, part=False):
        if part:
            return box3D(box.interval_x, my_closed(box.interval_y.lower + 1, box.interval_y.upper), box.interval_z)
        else:
            return box3D(box.interval_x, my_closed(box.interval_y.lower + 1, box.interval_y.upper - 1), box.interval_z)

    def z_cut_off(self, box, part=False):
        if part:
            return box3D(box.interval_x, box.interval_y, my_closed(box.interval_z.lower + 1, box.interval_z.upper))
        else:
            return box3D(box.interval_x, box.interval_y, my_closed(box.interval_z.lower + 1, box.interval_z.upper - 1))
