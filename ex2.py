class fraction():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x) + "/" + str(self.y)
    def __add__(self,other):
        newX=(self.x * other.y) + (other.x * self.y)
        newY=self.y*other.y
        return fraction(newX, newY)
    def __sub__(self,other):
        newX=(self.x * other.y) - (other.x * self.y)
        newY=self.y*other.y
        return fraction(newX, newY)
    def __float__(self):
        return self.x/self.y
    def nghichDao(self):
        return fraction(self.y, self.x)

a=fraction(3, 4)
b=fraction(2, 5)
print(a)
print(a+b)
print(float(a))
print(a.nghichDao())