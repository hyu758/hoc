class HoaDon(object):
    count=0
    def __init__(self,hoaDon="",benA="",benB="",soTien=0):
        self.hoaDon=hoaDon
        self.benA=benA
        self.benB=benB
        self.soTien=soTien
        HoaDon.count+=1
        self.thuTu=HoaDon.count
    def nhap(self):
        self.hoaDon=input("Nhap ten hoa don: ")
        self.benA=input(" Nhap ten ben A: ")
        self.benB=input("Nhap ten ben B: ")
        self.soTien=float(input("Nhap so tien can thanh toan: "))
    def HienThi(self):
        print(f"""
Ten hoa don: {self.hoaDon}
Ben A: {self.benA}
Ben B: {self.benB}
So tien: {self.soTien} nghin VND
""")
    def get_thuTu(self):
        return self.thuTu
    def __gt__(self,other):
        return self.soTien > other.soTien
    def __str__(self):
        return f"""
Ten hoa don: {self.hoaDon}
Ben A: {self.benA}
Ben B: {self.benB}
So tien: {self.soTien} nghin VND

"""
def max1(hd1,hd2):
    if hd1.soTien > hd2.soTien:
        return hd1
    return hd2
def max2(hd1,hd2):
    if hd1 > hd2:
        return hd1
    return hd2
class HoaDonNuoc(HoaDon):
    def __init__(self,hoaDon="",benA="",benB="",soNuoc=None,donGia=None):
        self.hoaDon=hoaDon
        self.benA=benA
        self.benB=benB
        self.soNuoc=soNuoc
        self.donGia=donGia
    def nhap(self):
        self.hoaDon=input("Nhap ten hoa don: ")
        self.benA=input(" Nhap ten ben A: ")
        self.benB=input("Nhap ten ben B: ")
        self.soNuoc=float(input("Nhap so nuoc: "))
        self.donGia=float(input("Nhap don gia: "))
        
    def HienThi(self):
        self.soTien=self.soNuoc*self.donGia*1.25
        print(f"""
Ten hoa don: {self.hoaDon}
BenA: {self.benA}
BenB: {self.benB}
So tien: {self.soTien} nghin VND
So nuoc: {self.soNuoc}
Don gia: {self.donGia} nghin VND
""")
a=HoaDon()
a.nhap()
b=HoaDon()
b.nhap()
c=HoaDonNuoc()
c.nhap()
c.HienThi()