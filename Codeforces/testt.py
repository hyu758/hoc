t=int(input())
res={}
while (t>0):
    s=input()
    for i in range(len(s)):
        if s[i]==s[i+1]:
            i+=1
        else:
            res.add(s[i])
    res.sort()
    for i in res:
        print(i,end="")
    print("")
    t-=1