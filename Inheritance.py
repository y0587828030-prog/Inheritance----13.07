#step 1 Swimmer Inherits from Athlete
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

a = Athlete("yehosh", 26)
a.introduce()

class Swimmer(Athlete):
    def __init__(self,name, age):
        super().__init__(name, age)

b = Swimmer("tom", 22)
b.introduce()