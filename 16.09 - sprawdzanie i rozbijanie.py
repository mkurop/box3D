class TEST:

    def permute(self, sortin, permutation):
        assert len(sortin) == len(permutation)
        return [sortin[i] for i in permutation]

    def my_sort(self, inputlist):
        inputlist = zip(inputlist, range(len(inputlist)))
        aux = sorted(inputlist, key = lambda x : x[0])
        sorted2in = [aux[i][1] for i in range(len(aux))]
        list2 = zip(sorted2in, range(len(sorted2in)))
        aux1 = sorted(list2, key = lambda x : x[0])
        in2sorted = [aux1[i][1] for i in range(len(aux1))]
        sort = [aux[i][0] for i in range(len(aux))]
        return sort, in2sorted, sorted2in

    def is_in(self, interval1, interval2):
        union = interval1 & interval2
        return True if ((union == interval1) ^ (union == interval2)) and (interval2.lower != interval1.lower and interval1.upper != interval2.upper)  else False

    def is_out(self, interval1, interval2):
        return True if (interval1.lower != interval2.lower) and (interval2.upper != interval1.upper) and (interval1 & interval2) else False

    def canonical_box(self, inter, inter_i):
        if self.is_in(inter, inter_i):
            if inter.upper < inter_i.upper:
                return 'in I II'
            else:
                return 'in II I'
        elif self.is_out(inter, inter_i):
            if inter.upper < inter_i.upper:
                return 'o I II'
            else:
                return 'o II I'
        elif self.is_separate(inter, inter_i):
            return 's'

    def canonical(self, inter_x, inter_y, inter_z, inter_x_i, inter_y_i, inter_z_i):
        return self.canonical_box(inter_x, inter_x_i),  self.canonical_box(inter_y, inter_y_i),  self.canonical_box(inter_z, inter_z_i)

    def rozbij(self, q, i):
        print(q.interval_x, q.interval_y, q.interval_z)
        print(i.interval_x, i.interval_y, i.interval_z,'\n')
        sort, in2sorted, sorted2in = self.my_sort(self.canonical(q.interval_x, q.interval_y, q.interval_z, i.interval_x, i.interval_y, i.interval_z))

        perm_q = self.permute([q.interval_x, q.interval_y, q.interval_z], in2sorted)
        perm_i = self.permute([i.interval_x, i.interval_y, i.interval_z], in2sorted)


        '''
        min_x_u, min_x_l, max_x_u, max_x_l, min_y_u, min_y_l, max_y_u, max_y_l, min_z_u, min_z_l, max_z_u, max_z_l = \
            min(q.interval_x.upper, i.interval_x.upper), min(q.interval_x.lower, i.interval_x.lower), max(q.interval_x.upper, i.interval_x.upper), max(q.interval_x.lower, i.interval_x.lower), \
            min(q.interval_y.upper, i.interval_y.upper), min(q.interval_y.lower, i.interval_y.lower), max(q.interval_y.upper, i.interval_y.upper), max(q.interval_y.lower, i.interval_y.lower),\
            min(q.interval_z.upper, i.interval_z.upper), min(q.interval_z.lower, i.interval_z.lower), max(q.interval_z.upper, i.interval_z.upper), max(q.interval_z.lower, i.interval_z.lower)
        inter = [[q.interval_x, q.interval_y, q.interval_z],[i.interval_x, i.interval_y, i.interval_z],
                    [closed(min_y_l, max_y_l), closed(max_y_l, min_y_u), closed(min_y_u, max_y_u)],
                    [closed(min_y_l, max_y_l), closed(max_y_l, min_y_u), closed(min_y_u, max_y_u)],
                    [closed(min_z_l, max_z_l), closed(max_z_l, min_z_u), closed(min_z_u, max_z_u)]]
        '''

        if sort == ['in I II', 'in I II', 'in I II']:
            return [box3D(i.interval_x, i.interval_y, i.interval_z)]
        elif sort == ['in II I', 'in II I', 'in II I']:
            return [box3D(q.interval_x, q.interval_y, q.interval_z)]
        elif sort == ['in I II', 'in I II', 'in II I']:
            box1 = self.permute([perm_q[0], perm_q[1], perm_q[2]], sorted2in)
            box2 = self.permute([perm_i[0], perm_i[1], closed(min(perm_q[2].lower, perm_i[2].lower), max(perm_q[2].lower, perm_i[2].lower))], sorted2in)
            box3 = self.permute([perm_i[0], perm_i[1], closed(min(perm_i[2].upper, perm_q[2].upper), max(perm_i[2].upper, perm_q[2].upper))], sorted2in)
            return [box3D(box1[0], box1[1], box1[2]),
                    box3D(box2[0], box2[1], box2[2]),
                    box3D(box3[0], box3[1], box3[2])]
        elif sort == ['in I II', 'in II I', 'in II I']:
            box1 = self.permute([perm_q[0], perm_q[1], perm_q[2]], sorted2in)
            box2 = self.permute([closed(min(perm_q[0].lower, perm_i[0].lower), max(min(perm_q[0].lower, perm_i[0].lower))),  perm_i[1], perm_i[2]], sorted2in)
            box3 = self.permute([closed(perm_i[0].upper, perm_q[0].upper), perm_i[1]], perm_i[2])
            return [box3D(box1[0], box1[1], box1[2]),
                   box3D(box2[0], box2[1], box2[2]),
                   box3D(box3[0], box3[1], box3[2])]
        #--------------------------------------------------------#
        elif sort == ['in I II', 'in I II', 'o I II']:
            box1 = self.permute([perm_i[0], perm_i[1], perm_i[2]], sorted2in)
            box2 = self.permute([perm_q[0], perm_q[1], closed(min(perm_i[2].lower, perm_q[2].lower), max(perm_i[2].lower, perm_q[2].lower))], sorted2in)
            return [box3D(box1[0], box1[1], box1[2]),
                   box3D(box2[0], box2[1], box2[2])]
        elif sort == ['in I II', 'in I II', 'o II I']:
            box1 = self.permute([perm_i[0], perm_i[1], perm_i[2]], sorted2in)
            box2 = self.permute([perm_q[0], perm_q[1], closed(min(perm_q[2].upper, perm_i[2].upper), max(perm_q[2].upper, perm_i[2].upper))], sorted2in)
            return [box3D(box1[0], box1[1], box1[2]),
                    box3D(box2[0], box2[1], box2[2])]



class box3D:
    def __init__(self, interval_x, interval_y, interval_z):
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.interval_z = interval_z

    def get_interval_x(self):
        return self.interval_x

    def get_interval_y(self):
        return self.interval_y

    def get_interval_z(self):
        return self.interval_z

    @staticmethod
    def factory(x1, y1, z1, x2, y2, z2):
        return box3D(closed(x1, x2), closed(y1, y2), closed(z1, z2))
from portion import closed
tst = TEST()
int1 = tst.rozbij(box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())), box3D(closed(input(), input()), closed(input(), input()), closed(input(), input())))

for i in range(len(int1)):
    print(int1[i].interval_x, int1[i].interval_y, int1[i].interval_z)
