class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def fly(self):
        print(f'Я вмію літати.')

    def swim(self):
        print(f'Я вмію плавати.')

class Bird(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def fly(self):
        print(f'Я {self.name}, мені {self.age} років.')
        super().fly()
        
class Fish(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def swim(self):
        print(f'Я {self.name}, мені {self.age} роки.')
        super().swim()

class SwimmingBird(Bird, Fish):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def swimming_fly(self):
        super().fly()
        super().swim() 

eagle = Bird('Орел', 10)
crucian = Fish('Карась', 2)
swan = SwimmingBird('Лебідь', 1)

eagle.fly()
crucian.swim()
swan.swimming_fly()

# eagle.swim()

print(Animal.__mro__)
print(Bird.__mro__)
print(Fish.__mro__)
print(SwimmingBird.__mro__)

# У виклику метода swimming_fly() одразу super().fly()
# звертається до Bird, там викликається метод fly(),
# потім звертається до класу Fish. 
# Там нема метода fly(), MRO переходить до класу Animal
# і викликається метод fly().
# Потім super().swim() у SwimmingBird  звертається до Bird, 
# де нема методу swim.
# Потім до класу Fish, а потім знов до Animal.

# Питання: коли я викликаю eagle.swim(), він виконується,
# а метода swim() у eagle немає. Мабуть, я неправильно
# щось зробив?



