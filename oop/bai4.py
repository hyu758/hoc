
import person #person.py la file python da tao san class Person
class Employee(person.Person):
    def __init__(self, ngaycong):
        self.tienCong=None
        self.ngayCong=ngaycong
        self.boPhan=None
        self.chucDanh=None
    def infoInput(self):
        
        self.boPhan=input("Nhap bo phan dang lam: ")
        self.chucDanh=input("Nhap chuc danh: ")
        self.tienCong=int(input("Nhap so tien cong moi ngay: "))
    def tinhTien(self):
        return self.ngayCong*self.tienCong
    def __str__(self):
        return f"Bo phan: {self.boPhan} \nChuc danh: {self.chucDanh}"
ae=Employee(20)
ae.infoInput()
print(person.a)
print(ae)
print(ae.tinhTien())