def permute(sortin, permutation):
    assert len(sortin) == len(permutation)
    return [sortin[i] for i in permutation]
def my_sort(inputed):
    sorted = inputed.copy()
    sorted.sort()
    sort2in, in2sort  = [inputed.index(sorted[inputed.index(i)]) for i in inputed] , [sorted.index(inputed[sorted.index(i)]) for i in sorted]
    return sorted, in2sort, sort2in



print(my_sort(['d','f','g', 'a', 'c']))

