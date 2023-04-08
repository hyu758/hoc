def search1(n,lst):
    for i in range (len(lst)-1,0,-1):
        if lst[i]==n:
            return True
    return False
def search2(n,lst):
    if lst[i] < n:
        return False
    else:
        for i in lst:
            if i==n:
                return True
        return False
def binary_search(n,lst):
    l=0
    r=len(lst)-1
    while l<=r:
        m=l+r//2
        if lst[m]==n:
            return True
        elif lst[m]>n:
            l=m+1
        else:
            r=m-1
    return False
lst=[15,12,9,7,5,3,1]
print(binary_search(11,lst))
    