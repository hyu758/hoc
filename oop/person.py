def checkLeapYear(n):
    if (n % 400 == 0):
        return True
    return (n%4==0 and n%100!=0)
class Date():
    def __init__(self,day,month,year):
        self.day=day 
        self.month=month
        self.year=year
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
    def dayCheck(self):
        dayOfMonth={
            1:31,
            2:28,
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31
        }
        if checkLeapYear(self.year):
            dayOfMonth["2"]=29
        if self.day < 1 or self.day > dayOfMonth[self.month]:
            return "Ngay khong hop le"
        else:
            return Date(self.day, self.month, self.year)
class Person():
    def __init__(self):
        self.name=""
        self.num=""
        self.date=Date(15,12,2004)
    def infoInput(self):
        self.name=input("Nhap ho va ten: ")
        self.num=input("Nhap can cuoc cong dan hoac cmnd: ")
        day=int(input("Nhap ngay sinh: "))
        month=int(input("Nhap thang sinh: "))
        year=int(input("Nhap nam sinh: "))
        print("-----------------------")
        self.date=Date(day,month,year)
    def __str__(self):
        return f"--------------------\nHo va ten: {self.name}\nCCCD: {self.num}\nNgay sinh: {self.date}"
a=Person()
a.infoInput()
        