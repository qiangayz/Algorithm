import random,copy
from cal_time import cal_time,nor_sort

def shell_sort(data):
    gap = len(data) // 2
    print(gap)
    while gap >=1:
        for i in range(gap,len(data)):
            tmp = data[i]
            j = i-gap
            while j >= 0 and tmp < data[j]:
                data[j + gap] = data[j]
                j -=gap
            data[i-gap] = tmp
        gap //=2

data = list(range(10000))
random.shuffle(data)
data1 = copy.deepcopy(data)
print(data)
shell_sort(data)
print(data)
data1 = nor_sort(data1)
print(data1)