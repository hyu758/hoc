class Coordinate():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"({self.x},{self.y})"
    def khoangCach(self,other):
        a= (self.x - other.x)**2
        b= (self.y - other.y)**2
        return (a+b)*0.5
c=Coordinate(2, 3)
d=Coordinate(3, 5)
print(c)
print(c.khoangCach(d))
        