def Ngtocheck(x):
    global count
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        return True
    return False
while True:
    n=int(input("Nhap so nguyen duong: "))
    if n>0:
        break
if Ngtocheck(n):
    print(n,"la so nguyen to")
else:
    print(n,"khong la so nguyen to")
            