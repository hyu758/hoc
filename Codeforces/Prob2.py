def xuLy(s):
    f=9
    lst=[]
    while True:
        if f>=s:
            lst.append(s)
            break
        else:
            lst.append(f)
            s-=f
            f-=1
    for i in lst[::-1]:
        print(i,end='')
    print('')
n=int(input())
z=[]
for i in range(n):
    x=int(input())
    z.append(x)
for i in z:
    xuLy(i)
    