class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return f"Animal: {self.name} {self.age}"
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return f"Cat: {self.name} {self.age}"
class Rabbit(Animal):
    tag=1
    def speak(self):
        print("meep")
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=Rabbit.tag 
        Rabbit.tag+=1
    def get_rid(self):
        return self.rid
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __str__(self):
        return f"Rabbit: {self.name}: {self.age}"
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
thotrang=Rabbit(2)
thotrang.set_name("Tho Trang")
thoden=Rabbit(2,"tho trang","tho den")
print(thotrang)
nam= Person("Nam", 45)
anh= Person("Anh", 20)
print(nam)
print(nam.speak())
print(nam.age_diff(anh))