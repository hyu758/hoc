t=int(input())
while t:
    n=int(input())
    a=list(map(int,input().split()))
    res=[]
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            res.append(a[i]*a[j])
    t-=1
    print(max(res))
