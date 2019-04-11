# EMA Exponential Moving Average
# EMA today = a * Price today + (1 - a) * EMA yesterday
a = 2 / (12 + 1)


def getEMA(list):
    sum = 0
    for i in len(list):
        sum += (1 - a) * sum + a * list[i]
    return sum


