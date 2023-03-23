def maxNum(n):
    count=0
    for i in n:
        if count==0:
            max=i
            count+=1
        else:
            if i > max:
                max=i
    return max
print(maxNum([1,5,67,6,3,7,78]))
#O(n)=n