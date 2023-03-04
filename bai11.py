
def reverse(a):
    assert isinstance(a, list),"vui long nhap vao 1 list"
    result=[]
    for i in range(len(a)-1,-1,-1):
        result.append(a[i])
    print(result)
    
reverse([1,2,5,6,9])