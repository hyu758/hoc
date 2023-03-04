n=int(input("Nhap so luong n: "))
arr=[]
s=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
if arr[0]==1:
    for i in range(len(arr)):
        if arr[i+1]-arr[i]!=1:
            print(arr[i]+1)
            break
else:
    print(1)
# for i in range (max(arr)):
#     s.append(i+1)
# for i in range(max(s)):
#     if arr[i]!=s[i]:
#         print(s[i])
#         break
    