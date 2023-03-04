import bai4
class TeamLeader(bai4.Employee):
    flag=0
    def __init__(self,ngaycong,giodaotao):
        self.ngayCong=ngaycong
        self.gioDaotao=giodaotao
    def infoInput(self):
        self.gioDaotao=input("Nhap so gio dao tao")
        if self.gioDaotao==42:
            flag=1
    def tienLuong(self):
        
        