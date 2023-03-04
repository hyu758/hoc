import toado
class Coordinate3D(toado.Coordinate(x, y)):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    def distance(self,other):
        a= (self.x - other.x)**2
        b=(self.y - other.y )**2
        c =(self.z - other.z)**2
        return (a+b+c)**0.5
cor1=Coordinate3D(1, 4, 5)
print(cor1)