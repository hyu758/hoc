import bai1
import random
class Student(bai1.Person):
    def __init__(self, name, age, major=None):
        bai1.Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major= major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
            return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
tu=Student("Tu",20)
tu.change_major("IT")
print(tu)
