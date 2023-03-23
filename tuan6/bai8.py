def bubbleSort(lst):
    f=False
    for n in range(len(lst)-1,0,-1):
        for i in range(n):
            if lst[i] > lst[i+1]:
                f=True
                lst[i],lst[i+1]=lst[i+1],lst[i]
        if not f:
            return
lst=[5,2,6,2,88,52,22,21,1]
bubbleSort(lst)
print(lst)
