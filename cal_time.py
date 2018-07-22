import time

def cal_time(func):          #该装饰器用来测量函数运行的时间
    def wrapper(*args,**kwargs):
        t1 = time.time()
        res = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return res
    return wrapper

@cal_time
def nor_sort(data):
    list = sorted(data)
    return list