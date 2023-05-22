t=int(input())
while (t):
    n=int(input())
    s=input()
    res=0
    lst=[]
    for x in s:
        if x in lst:
            res+=1
        else:
            res+=2
        lst.append(x)
    t-=1
    print(res)

    