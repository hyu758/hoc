def lmao(l1,l2):
    result=[]
    for i in l1:
        if i not in l2:
            result.append(i)
    return result
print(lmao([2,1,5,26,3],[3,2,4,8,3,20]))