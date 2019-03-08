# 计算一个list的平均值

def pjs(list):
    sum = .0
    for i in list:
        sum += i
    return sum / len(list)

print("{:.2f}".format(pjs([1,2,3,5,3.3])))
