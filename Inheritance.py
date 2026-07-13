#step 1 Swimmer Inherits from Athlete
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

athlete = Athlete("yehosh", 26)
athlete.introduce()

class Swimmer(Athlete):
    def __init__(self,name, age):
        super().__init__(name, age)

swimming = Swimmer("tom", 22)
swimming.introduce()


## step 2 
class Athlete:
    def __init__(self, name, age,sport):
        self.name = name 
        self.age = age
        self.sport = sport

    def describe(self):
        print(f"{self.name} competes in {self.sport}")
athlete=Athlete("bob", 25, "Dance")
athlete.describe()

class Runner(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age, "Running")

Ratzen=Runner("sara", 25)
Ratzen.describe()


##step 3
class Athlete:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete")

athlete = Athlete("yehosh", 26)
athlete.introduce()

class Cyclist(Athlete):
    def __init__(self, name, age,bike_brand ):
        super().__init__(name, age )
        self.bike = bike_brand



    def describe_gear(self):
             print(f"Cyclist {self.name} rides a {self.bike}.")

riding= Cyclist("Mike", 30, "Trek")
riding.introduce()
riding.describe_gear()

##step 4
class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet(self):
        print(f"{self.name} represents {self.country}")

class Swimmer(Athlete):
    def __init__(self, name, country,stroke_style):
        super().__init__(name, country)
        self.stroke = stroke_style

class Runner(Athlete):
    def __init__(self, name, country, best_distance):
        super().__init__(name, country)
        self.best = best_distance

class Cyclist(Athlete):
    def __init__(self, name, country, race_type):
        super().__init__(name, country)
        self.race = race_type

swimming = Swimmer("Lior", "Israel", "freestyle")
running = Runner("Avi", "Kenya", "marathon")
riding = Cyclist("Jan", "France", "road")
swimming.greet()
running.greet()
riding.greet()

                

        