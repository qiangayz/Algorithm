import time,random
import copy

def cal_time(func):          #该装饰器用来测量函数运行的时间
    def wrapper(*args,**kwargs):
        t1 = time.time()
        res = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return res
    return wrapper

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

@cal_time
def bubble_sort_1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break

@cal_time
def nor_sort(data):
    list = sorted(data)
    return list

@cal_time
def select(data):
    for i in range(len(data)-1):
        min_loc = i
        for j in range(i+1,len(data)):
            if data[j] < data[min_loc]:
                min_loc=j
        data[i],data[min_loc] = data[min_loc],data[i]

@cal_time
def insert(data):
    for i in range(1,len(data)):
        temp = data[i]
        j= i-1
        while j>=0 and temp < data[j]:
            data[j+1] = data[j]
            j=j-1
        data[j+1] = temp


data = list(range(1000))
random.shuffle(data)
data1 = copy.deepcopy(data)
data2 = copy.deepcopy(data)
data3 = copy.deepcopy(data)
data4 = copy.deepcopy(data)
bubble_sort_1(data)
bubble_sort(data1)
data2 = nor_sort(data2)
select(data3)
insert(data4)
print(data,'\n',data1,'\n',data2,'\n',data3,'\n',data4)