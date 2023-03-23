tuDien={
    "a":1
}
def char(c, n):
    return chr(ord(c) + n)
count=2
n="a"
tmp=0
while count<27:
    tmp+=1
    tuDien[char(n,tmp)]=count
    count+=1
def solve(a,b):
    count=0
    st=""
    for i in a:
        if count + tuDien[i]<b+1:
            count+=tuDien[i]
            st+=i
    print(st)

n=int(input())
stt=[]
numm=[]
for i in range(n):
    st=input()
    stt.append(st)
    num=int(input())
    numm.append(num)
for i in range (n):
    solve(stt[i],numm[i])
