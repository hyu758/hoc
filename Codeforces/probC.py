def xuLy(x,y):
    y=x-y
    if y==0:
        print(preCost[x-1])
    else:
        print(preCost[x-1]-preCost[y-1])
s=[]
z=[]
a,b=map(int,input().split())
costt=map(int,input().split())
cost=list(costt)
cost.sort(reverse=True)
preCost=[0]*len(cost)
preCost[0]=cost[0]
for i in range (1,len(cost)):
    preCost[i]=preCost[i-1]+cost[i]
for i in range (b):
    x,y=map(int,input().split())
    s.append(x)
    z.append(y)
for i in range (len(s)):
    xuLy(s[i],z[i])

    

        
    
    