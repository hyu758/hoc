n,m=map(int,input().split())
count=0
res=[]
temp=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    for j in range (temp,m):
        if b[i]>a[j]:
            count+=1
        else:
            temp=j
            res.append(count)
            break
print(res)
