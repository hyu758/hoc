
t=int(input())
while (t>0):
    lst=[]
    res=0
    n=int(input())
    s=input()
    i=0
    while i<n:
        if (s[i:i+1]) not in lst:
            res+=1
            i+=1
        else:
            i+=1
    print(res)
    t-=1