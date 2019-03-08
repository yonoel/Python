# EMA Exponential Moving Average
a = 2 / (12 + 1)


def getEMAToday(list):
    sum = 0
    for i in len(list):
        sum += (1 - a) * list[i - 1] + a * list[i]
    return sum


def handleData(num):
    return a * num
