n=int(input())
while n>0:
    sum=0
    lst=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    for i in range(lst[1]):
        sum+=arr[i]
        