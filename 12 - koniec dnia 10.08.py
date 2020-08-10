def permute(self, i, num, sort, reverse, new_tab=[]):
    if i == len(sort):
        return new_tab
    else:
        i+=1
    if(not reverse):
        if(factorial(num)==sort[i] or num==sort[id]):
            return new_tab.append(num)
        else:
            return self.permute(i, num+1, sort, False)
    else:
        return new_tab.append(factorial(num))def my_sort(self, sorted):
     sorted = sorted.sort()
     in2sorted = self.permute(0,0, sorted, False)
     sorted2in = self.permute(0,0, in2sorted, True)
     return sorted, in2sorted, sorted2in
     
     print(algorytm().my_sort([4,1,3]))
