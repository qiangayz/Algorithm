import time,random,copy
from cal_time import cal_time,nor_sort

def merge(data,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if data[i]<data[j]:
            ltmp.append(data[i])
            i += 1
        else:
            ltmp.append(data[j])
            j += 1
    while i <= mid:
        ltmp.append(data[i])
        i += 1
    while j <= high:
        ltmp.append(data[j])
        j +=1
    data[low:high+1] = ltmp

def _merge_sort(data,low,high):
    if low<high:
        mid = (low+high)//2
        _merge_sort(data,low,mid)
        _merge_sort(data,mid+1,high)
        merge(data,low,mid,high)

@cal_time
def merge_sort(data):
    _merge_sort(data,0,len(data)-1)

data = list(range(10000))
random.shuffle(data)
data1 = copy.deepcopy(data)
print(data)
merge_sort(data)
nor_sort(data1)
print(data)