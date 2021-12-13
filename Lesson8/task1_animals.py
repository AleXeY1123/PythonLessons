class animals:
    def __init__ (self, title, height, weight):
        self.title = title
        self.height = height
        self.weight = weight

class mammals(animals):
    def __init__ (self, title, height, weight, gender, age):
        super().__init__(title, height, weight)
        self.gender = gender
        self.age = age

class human(mammals):
    def __init__ (self, name, nationality, language, title, height, weight, gender, age):
        super().__init__(title, height, weight, gender, age)
        self.name = name
        self.nationality = nationality
        self.language = language
    
    def working(self):
        print(f'{self.name} working')

class cat(mammals):
    def __init__ (self, name, breed, title, height, weight, gender, age):
        super().__init__(title, height, weight, gender, age)
        self.breed = breed
        self.name = name
    
    def hunting(self):
        print(f'{self.name} hunting')

    def make_sound(self):
        print('Meow')

class dog(mammals):
    def __init__ (self, name, breed, title, height, weight, gender, age):
        super().__init__(title, height, weight, gender, age)
        self.breed = breed
        self.name = name

    def hunting(self):
        print(f'{self.name} hunting')

    def make_sound(self):
        print('Gav')

Tom = human('Tom','British','Eng','Human',175,80,'male',25)
Cat = cat('Barsik','bengal','cat',20,7,'female',6)
Tom.working()
Cat.make_sound()
Cat.hunting()
