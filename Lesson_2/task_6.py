# Завдання 6

# Використовуючи код example_10, 
# створіть класовий метод ( для 
# створення використовуйте декоратор 
# @classmethod ). Метод має підраховувати 
# кількість об'єктів цього класу 
# які досягли повноліття, для вирішення 
# задачі використовуйте статичний метод 
# створенний в завданні 5

from datetime import date


class MyClass1:
    adult_count = 0

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age


        if self.is_adult(age):
            MyClass1.adult_count += 1
        

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def count_adults(cls):        
        return cls.adult_count    

class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

print(f"Кількість повнолітніх осіб: {MyClass1.count_adults()}")