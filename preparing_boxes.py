from cut_box import *
from split_intervals import mylen


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

    def sort_sliced_walls_xz(self, sliced, sorted_walls):
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
                             box.interval_y, box.interval_z, True)
            prepared_walls.append(wall)
        return prepared_walls

    def prepare_walls_for_tree_y(self, wall_list):
        prepared_walls = []
        for key, value in wall_list.items():
            for box in value:
                wall = box3D(box.interval_x,
                             my_closed(box.interval_y.lower_meps, box.interval_y.upper_eps),
                             box.interval_z, True)
        prepared_walls.append(wall)
        return prepared_walls

    def prepare_walls_for_tree_z(self, wall_list):
        prepared_walls = []
        for key, value in wall_list.items():
            for box in value:
                wall = box3D(box.interval_x, box.interval_y,
                             my_closed(box.interval_z.lower_meps, box.interval_z.upper_eps), True)
        prepared_walls.append(wall)
        return prepared_walls

    def x_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower >= 2 else False

    def x_partially_sliceable(self, box):
        return True if box.interval_x.upper - box.interval_x.lower == 1 else False

    def x_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.lower),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper), True)
        slice_upper = box3D(my_closed(box.interval_x.upper, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper), True)
        return [slice_lower, slice_upper]

    def x_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.lower),
                           my_closed(box.interval_y.lower, box.interval_y.upper),
                           my_closed(box.interval_z.lower, box.interval_z.upper), True)
        return slice_wall

    def y_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower >= 2 else False

    def y_partially_sliceable(self, box):
        return True if box.interval_y.upper - box.interval_y.lower == 1 else False

    def y_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.lower),
                            my_closed(box.interval_z.lower, box.interval_z.upper), True)
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.upper, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.upper), True)
        return [slice_lower, slice_upper]

    def y_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                           my_closed(box.interval_y.lower, box.interval_y.lower),
                           my_closed(box.interval_z.lower, box.interval_z.upper), True)
        return slice_wall

    def z_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower >= 2 else False

    def z_partially_sliceable(self, box):
        return True if box.interval_z.upper - box.interval_z.lower == 1 else False

    def z_slice(self, box):
        slice_lower = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.lower, box.interval_z.lower), True)
        slice_upper = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                            my_closed(box.interval_y.lower, box.interval_y.upper),
                            my_closed(box.interval_z.upper, box.interval_z.upper), True)
        return [slice_lower, slice_upper]

    def z_part_slice(self, box):
        slice_wall = box3D(my_closed(box.interval_x.lower, box.interval_x.upper),
                           my_closed(box.interval_y.lower, box.interval_y.upper),
                           my_closed(box.interval_z.lower, box.interval_z.lower), True)
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

    def slice_wall_xyz_cond(self, wall):
        return all([mylen(wall.interval_x) == 0, mylen(wall.interval_y) == 0,
                    mylen(wall.interval_z) == 0])

    def slice_wall_xy_cond(self, wall):
        return mylen(wall.interval_x) == 0 and mylen(wall.interval_y) == 0

    def slice_wall_xz_cond(self, wall):
        return mylen(wall.interval_x) == 0 and mylen(wall.interval_z) == 0

    def slice_wall_yz_cond(self, wall):
        return mylen(wall.interval_y) == 0 and mylen(wall.interval_z) == 0

    def slice_wall_xy(self, wall):
        edge = box3D(wall.interval_x, wall.interval_y, my_closed(wall.interval_z.lower, wall.interval_z.lower),
                     False, True)
        wall = self.z_cut_off(wall, True)
        wall = box3D(wall.interval_x, wall.interval_y, wall.interval_z, True)
        return edge, wall

    def slice_wall_xz(self, wall):
        edge = box3D(wall.interval_x, my_closed(wall.interval_y.lower, wall.interval_y.lower), wall.interval_z,
                     False, True)
        wall = self.y_cut_off(wall, True)
        wall = box3D(wall.interval_x, wall.interval_y, wall.interval_z, True)
        return edge, wall

    def slice_wall_yz(self, wall):
        edge = box3D(my_closed(wall.interval_x.lower, wall.interval_x.lower), wall.interval_y, wall.interval_z,
                     False, True)
        wall = self.x_cut_off(wall, True)
        wall = box3D(wall.interval_x, wall.interval_y, wall.interval_z, True)
        return edge, wall

    def slice_wall_x_cond(self, wall):
        return mylen(wall.interval_x) == 0

    def slice_wall_y_cond(self, wall):
        return mylen(wall.interval_y) == 0

    def slice_wall_z_cond(self, wall):
        return mylen(wall.interval_z) == 0

    def prepare_edge_for_tree_x(self, edge):
        edge = box3D(my_closed(edge.interval_x.lower_meps, edge.interval_x.upper_eps), edge.interval_y,
                     edge.interval_z, False, True)
        return edge

    def prepare_edge_for_tree_y(self, edge):
        edge = box3D(edge.interval_x, my_closed(edge.interval_y.lower_meps, edge.interval_y.upper_eps),
                     edge.interval_z, False, True)
        return edge

    def prepare_edge_for_tree_z(self, edge):
        edge = box3D(edge.interval_x, edge.interval_y,
                     my_closed(edge.interval_z.lower_meps, edge.interval_z.upper_eps), False, True)
        return edge

    def slice_wall_x(self, wall):
        edge = box3D(wall.interval_x, my_closed(wall.interval_y.lower, wall.interval_y.lower), wall.interval_z, False,
                     True)
        wall = self.y_cut_off(wall, True)
        return edge, wall

    def slice_wall_y(self, wall):
        edge = box3D(wall.interval_x, wall.interval_y, my_closed(wall.interval_z.lower, wall.interval_z.lower), False,
                     True)
        wall = self.z_cut_off(wall, True)
        return edge, wall

    def slice_wall_z(self, wall):
        edge = box3D(my_closed(wall.interval_x.lower, wall.interval_x.lower), wall.interval_y, wall.interval_z, False,
                     True)
        wall = self.x_cut_off(wall, True)
        return edge, wall

    def slice_wall(self, wall):
        my_int = myInterval()
        wall = my_int.box_uncut(wall)
        if self.slice_wall_xyz_cond(wall):
            return wall, None
        if self.slice_wall_xy_cond(wall):
            return self.slice_wall_xy(wall)
        if self.slice_wall_xz_cond(wall):
            return self.slice_wall_xz(wall)
        if self.slice_wall_yz_cond(wall):
            return self.slice_wall_yz(wall)
        if self.slice_wall_x_cond(wall):
            return self.slice_wall_x(wall)
        if self.slice_wall_y_cond(wall):
            return self.slice_wall_y(wall)
        if self.slice_wall_z_cond(wall):
            return self.slice_wall_z(wall)

    def prepare_sliced_edges_x(self, sorted_edges):
        prepared_edges = []
        for key, value in sorted_edges.items():
            for edge in value:
                if mylen(edge.interval_x) == 0:
                    edge = self.prepare_edge_for_tree_x(edge)
                if mylen(edge.interval_y) == 0:
                    edge = self.prepare_edge_for_tree_y(edge)
                if mylen(edge.interval_z) == 0:
                    edge = self.prepare_edge_for_tree_z(edge)
                prepared_edges.append(edge)
        return prepared_edges

    def prepare_sliced_edges_y(self, sorted_edges):
        prepared_edges = []
        for key, value in sorted_edges.items():
            for wall in value:
                edge = self.prepare_edge_for_tree_y(wall)
            if mylen(edge.interval_z) == 0:
                edge = self.prepare_edge_for_tree_y(edge)
            prepared_edges.append(edge)
        return prepared_edges

    def prepare_sliced_edges_z(self, sorted_edges):
        prepared_edges = []
        for key, value in sorted_edges.items():
            for wall in value:
                edge = self.prepare_edge_for_tree_z(wall)
            prepared_edges.append(edge)
        return prepared_edges

    def sort_sliced_edges(self, edges, edge_xyz_dict, edge_xy_dict, edge_yz_dict, edge_xz_dict):
        for edge in edges:
            if self.slice_wall_xyz_cond(edge):
                edge_xyz_dict = self.sort_sliced_edge_xyz(edge, edge_xyz_dict)
            if self.slice_wall_xy_cond(edge) or self.slice_wall_x_cond(edge):
                edge_xy_dict = self.sort_sliced_edge_xy(edge, edge_xy_dict)
            if self.slice_wall_yz_cond(edge) or self.slice_wall_y_cond(edge):
                edge_yz_dict = self.sort_sliced_edge_yz(edge, edge_yz_dict)
            if self.slice_wall_xz_cond(edge) or self.slice_wall_z_cond(edge):
                edge_xz_dict = self.sort_sliced_edge_xz(edge, edge_xz_dict)
        return edge_xyz_dict, edge_xy_dict, edge_yz_dict, edge_xz_dict

    def sort_sliced_edge_xy(self, wall, sorted_edges):
        sorted_edges[wall.interval_x.lower, wall.interval_y.lower].append(wall)
        return sorted_edges

    def sort_sliced_edge_yz(self, wall, sorted_edges):
        sorted_edges[wall.interval_y.lower, wall.interval_z.lower].append(wall)
        return sorted_edges

    def sort_sliced_edge_xz(self, wall, sorted_edges):
        sorted_edges[wall.interval_x.lower, wall.interval_z.lower].append(wall)
        return sorted_edges

    def sort_sliced_edge_xyz(self, wall, sorted_edges):
        sorted_edges[wall.interval_x.lower, wall.interval_y.lower, wall.interval_z.lower].append(wall)
        return sorted_edges

    def slice_points(self, edge, sorted_points):
        if all([mylen(edge.interval_x) == 0, mylen(edge.interval_y) == 0, mylen(edge.interval_z) == 0]):
            point = box3D(edge.interval_x, edge.interval_y, edge.interval_z, False, False, True)
            sorted_points.append(point)
            return sorted_points, 0
        if self.slice_point_xy_cond(edge):
            sorted_points.append(self.slice_point_xy(edge))
            edge = self.z_cut_off(edge, True)
            edge = box3D(edge.interval_x, edge.interval_y, edge.interval_z, False, False, True)
            return sorted_points, edge
        if self.slice_point_yz_cond(edge):
            sorted_points.append(self.slice_point_yz(edge))
            edge = self.x_cut_off(edge, True)
            edge = box3D(edge.interval_x, edge.interval_y, edge.interval_z, False, False, True)
            return sorted_points, edge
        if self.slice_point_xz_cond(edge):
            sorted_points.append(self.slice_point_xz(edge))
            edge = self.y_cut_off(edge, True)
            edge = box3D(edge.interval_x, edge.interval_y, edge.interval_z, False, False, True)
            return sorted_points, edge

    def slice_point_xy_cond(self, edge):
        return True if mylen(edge.interval_x) == 0 and mylen(edge.interval_y) == 0 else False

    def slice_point_xz_cond(self, edge):
        return True if mylen(edge.interval_x) == 0 and mylen(edge.interval_z) == 0 else False

    def slice_point_yz_cond(self, edge):
        return True if mylen(edge.interval_y) == 0 and mylen(edge.interval_z) == 0 else False

    def slice_point_yz(self, edge):
        return box3D(my_closed(edge.interval_x.lower, edge.interval_x.lower), edge.interval_y, edge.interval_z,
                     False, False, True)

    def slice_point_xz(self, edge):
        return box3D(edge.interval_x, my_closed(edge.interval_y.lower, edge.interval_y.lower), edge.interval_z,
                     False, False, True)

    def slice_point_xy(self, edge):
        return box3D(edge.interval_x, edge.interval_y, my_closed(edge.interval_z.lower, edge.interval_z.lower),
                     False, False, True)

    def sort_sliced_points(self, points_list, points_dict):
        for point in points_list:
            points_dict[point.interval_x.lower, point.interval_y.lower, point.interval_z.lower].append(point)
        return points_dict

    def prepare_sliced_points(self, sorted_points):
        prepared_points = []
        for key, value in sorted_points.items():
            for point in value:
                point = self.prepare_point_for_tree_x(point)
                point = self.prepare_point_for_tree_y(point)
                point = self.prepare_point_for_tree_z(point)
            prepared_points.append(point)
        return prepared_points


    def prepare_point_for_tree_x(self, edge):
        edge = box3D(my_closed(edge.interval_x.lower_meps, edge.interval_x.upper_eps), edge.interval_y,
                     edge.interval_z, False, False, True)
        return edge

    def prepare_point_for_tree_y(self, edge):
        edge = box3D(edge.interval_x, my_closed(edge.interval_y.lower_meps, edge.interval_y.upper_eps),
                     edge.interval_z, False, False, True)
        return edge

    def prepare_point_for_tree_z(self, edge):
        edge = box3D(edge.interval_x, edge.interval_y,
                     my_closed(edge.interval_z.lower_meps, edge.interval_z.upper_eps), False, False, True)
        return edge
