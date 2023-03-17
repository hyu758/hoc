def average(n):
    sum=0
    for i in n:
        sum+=i
    return sum/len(n)
print(average([2,26,7]))
#O(n)=n