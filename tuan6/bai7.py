def findNum(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            return i
    return -1
print(findNum([2,63,7,6,2], 5))