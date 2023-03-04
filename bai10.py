def maxList(a):
    assert isinstance(a, list),"vui long nhap vao 1 danh sach"
    assert len(a)!=0,"vui long khong nhap vao 1 danh sach rong"
    f=True
    for i in a:
        if not isinstance(i, int):
            f=False
    assert f==True, "Vui long nhap vao danh sach la so nguyen"   
    
    max =a[0]
    for i in range (len(a)):
        if a[i]>max:
            max=a[i]
         
    print(max)
maxList(12)
