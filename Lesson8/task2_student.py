class human:
    def __init__ (self, name, gender, age, height, weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

class Student(human):
    def __init__ (self, name, gender, age, height, weight, homework):
        super().__init__(name, gender, age, height, weight)
        self.homework = homework

    def __eq__(self, homework):
        return self.homework == homework

    def __ne__(self, homework):
        return self.homework != homework

    def __lt__(self, homework):
        return self.homework < homework

    def __gt__(self, homework):
        return self.homework > homework

    def __le__(self, homework):
        return self.homework <= homework

    def __ge__(self, homework):
        return self.homework >= homework

Tom = Student('Tom', 'male', 16, 170, 68, 15)
Bob = Student('Bob', 'male', 16, 165, 60, 10)


print(Tom == Bob)
print(Tom != Bob)
print(Tom < Bob)
print(Tom > Bob)
print(Tom <= Bob)
print(Tom >= Bob)