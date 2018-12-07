def findMinAndMax(L):
    if(len(L) == 0) :return None;
    min = L[0]
    max = L[-1]
    for x in L :
        if(x < min): min = x
        if(x > max): max = x

    return (min,max)


# print(findMinAndMax([1,2,3,4,5]))
d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([key + '=' + value for key, value in d])
for key in d:
    print(key)

