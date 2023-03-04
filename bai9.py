def soChan(a):
    assert len(a)!=0,"vui long khong nhap vao 1 danh sach rong"
    result=[]
    for i in range (len(a)):
        if a[i]%2==0:
            result.append(a[i])
    print(result)
soChan([])