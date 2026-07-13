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


## step 2 
class Athlete:
    def __init__(self, name, age,sport):
        self.name = name 
        self.age = age
        self.sport = sport

    def describe(self):
        print(f"{self.name} competes in {self.sport}")
a=Athlete("bob", 25, "Dance")
a.describe()

class Runner(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age, "Running")

b=Runner("sara", 25)
b.describe()


##step 3
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

a = Athlete("yehosh", 26)
a.introduce()

class Cyclist(Athlete):
    def __init__(self, name, age,bike_brand ):
        super().__init__(name, age )
        self.bike = bike_brand



    def describe_gear(self):
             print(f"Cyclist {self.name} rides a {self.bike}.")

b= Cyclist("Mike", 30, "Trek")
b.introduce()
b.describe_gear()
         

        