from cut_box import *
from collections import defaultdict

class Slice:

    def slice_boxes(self, box_list):
        sliced_yz, sliced_xz, sliced_xy, sliced_boxes = [], [], [], []
        for box in box_list:
            x, y, z, box_temp = self.slice_box(box)
            sliced_yz.extend(x)
            sliced_xz.extend(y)
            sliced_xy.extend(z)
            sliced_boxes.extend(box_temp)
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
        return sliced_yz, sliced_xz, sliced_xy, [box]

    def sort_sliced_walls(self, sliced, sorted_walls=None):
        if sorted_walls is None:
            sorted_walls = defaultdict(list)
        for wall in sliced:
            if wall.interval_x.empty:
                sorted_walls[wall.interval_x.lower].extend(wall)
            if wall.interval_y.empty:
                sorted_walls[wall.interval_y.lower].extend(wall)
            if wall.interval_z.empty:
                sorted_walls[wall.interval_z.lower].extend(wall)
        return sorted_walls

    def prepare_walls_for_tree(self, wall_list):
        prepared_walls = []
        for walls in wall_list:
            for wall in walls:
                    if not self.x_sliceable(wall):
                        prepared_walls.append(box3D(my_closed(wall.interval_x.lower_meps, wall.interval_x.upper_eps),
                                               wall.interval_y, wall.interval_z))
                    if not self.y_sliceable(wall):
                        prepared_walls.append(box3D(wall.interval_x, my_closed(wall.interval_y.lower_meps,
                                                                              wall.interval_y.upper_eps), wall.interval_z))
                    if not self.z_sliceable(wall):
                        prepared_walls.append(box3D(wall.interval_x, wall.interval_y,
                                         my_closed(wall.interval_z.lower_meps, wall.interval_z.upper_eps)))
        return prepared_walls



    def x_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower >= 2 else False

    def x_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.lower),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.upper, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def y_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower >= 2 else False

    def y_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.lower),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.upper, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def z_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower >= 2 else False

    def z_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.lower))
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.upper, box.interval_z.upper))
        return [slice_lower, slice_upper]

    def x_cut_off(self, box):
        return box3D(my_closed(box.interval_x.lower + 1, box.interval_x.upper - 1), box.interval_y, box.interval_z)

    def y_cut_off(self, box):
        return box3D(box.interval_x, my_closed(box.interval_y.lower + 1, box.interval_y.upper - 1), box.interval_z)

    def z_cut_off(self, box):
        return box3D(box.interval_x, box.interval_y, my_closed(box.interval_z.lower + 1, box.interval_z.upper - 1))

