import time,random,copy
from cal_time import cal_time,nor_sort

def sift(data,low,high):   #来一次调整
    i= low         #low为根节点，父节点
    j= 2 * i + 1    #i的左孩子
    tmp = data[i]
    while j <= high: #没有超过数组范围时
        if j < high and data[j] < data[j + 1 ]:#如果j小于high也就是说左孩子小于最边界的high那么这个节点肯定有右孩子，
            j +=1   #这个时候对比左孩子和右孩子的大小，如果右孩子大于左孩子，那么这个时候把J置为右孩子，J的左右就是表示两个孩子里面最大的那个
        if tmp < data[j]: #如果父亲的值小于孩子的值，这个时候开始换位置
            data[i] = data[j]    #j的值换为父亲，i的值换为孩子
            i =j             #把I的位置调整到之前比父亲大的那个孩子的位置，
            j = 2* i + 1     #开始比较当前这个孩子和他自己孩子的大小，找到它的左孩子，定义为j
        else:     #如果两个孩子都没父亲大
            break    #什么也不干，跳出当前循环
    data[i] = tmp    #把最初始i的值赋给调整之后的位置

@cal_time
def heap_sort(data):
    n = len(data)
    for i in range(n //2 -1,-1,-1):#取最后一个有孩子的父节点，倒序遍历
        sift(data,i,n-1)  #调整
    for i in range(n-1,-1,-1):
        data[0],data[i] = data[i],data[0]
        sift(data,0,i-1)

data = list(range(10000))
random.shuffle(data)
data1 = copy.deepcopy(data)
print(data)
heap_sort(data)
print(data)
data1 = nor_sort(data1)
print(data1)
