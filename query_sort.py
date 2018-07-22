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

def query_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        query_sort(data,left,mid-1)
        query_sort(data,mid+1,right)

def partition(data,left,right):
    temp = data[left]
    while left < right:
        while left<right and data[right] >= temp:
            right -=1
        data[left] = data[right]
        while left<right and data[left] <= temp:
            left +=1
        data[right] = data[left]
    data[left] = temp
    return left

@cal_time
def query_sort_h(data):
    query_sort(data,0,len(data)-1)

@cal_time
def sort_fun(data):
    data.sort()
data = list(range(10000))
random.shuffle(data)
data1 = copy.deepcopy(data)
print(data)
query_sort_h(data)
sort_fun(data1)
print(data)