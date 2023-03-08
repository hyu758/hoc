
def xuLy(s):
    lst=[]
    count=0
    for i in range(len(s)):
        if s[i] not in lst:
            lst.append(s[i])
            if len(lst)>3:
                lst=[]
                count+=1
                lst.append(s[i])
    if len(lst)!=0:
        count+=1
    print(count)
n=int(input())
b=[]
for i in range(n):
    a=input()
    b.append(a)
for i in b:
    xuLy(i)
