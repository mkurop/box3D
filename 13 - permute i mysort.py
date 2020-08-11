def permute(sortin, order, iterator=0, new_tab = [], j = 0):
    return [sortin[sortin.index(i)] for j in range(len(sortin)) for i in sortin  if sortin.index(i) == order.index(j)]
def my_sort(sortin, order):
    return permute(sortin, order)



print(my_sort([4,1,3,5], [1,2,0,3]))

