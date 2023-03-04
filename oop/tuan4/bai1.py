import datetime
class Person(object):

    def __init__(self, name):

        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName
    def __str__(self):
        return self.name
    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    def getAge(self):
        Today=datetime.date.today()
        if self.birthday==None:
            raise ValueError
        return Today.year-self.birthday.year
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
class MITPerson(Person):
    nextIdNum = 0 # biến lớp idNumber
    def __init__(self, name):
        Person.__init__(self, name) #khởi tạo thuộc tính
        self.idNum = MITPerson.nextIdNum #MITPerson unique ID
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sắp xếp theo ID number
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
    MITPerson.__init__(self, name)
    self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

    class Grad(Student):
        pass
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,1984)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,1983)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,1955)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
personList = [p1, p2, p3, p4, p5]
print(p1)
print(p1.getAge())