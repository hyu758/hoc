t=int(input())
while (t):
    lst=[]
    res=[]
    i=list(map(int,input().split()))
    a=i[0]
    b=i[1]
    if (a <100 and b<100):
        for i in range(a,b+1):
            lst.append(i)
        for i in lst:
            i=str(i)
            t1=int(i[0])
            t2=int(i[1])
            res.append(t1-t2)
        m = max(res)
        indx=res.index(m)
        print(lst[indx])
    else:
        print(90)
    t-=1