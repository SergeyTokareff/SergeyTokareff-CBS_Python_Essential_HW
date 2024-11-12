# Завдання 7

# Створіть ієрархію класів транспортних засобів. 
# У загальному класі опишіть загальні всім 
# транспортних засобів поля, у спадкоємцях – 
# специфічні їм. Створіть кілька екземплярів. 
# Виведіть інформацію щодо кожного транспортного засобу.

class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def print_info(self):
        print(f"{self.__class__.__name__} Info:")
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Рік: {self.year}")
        print(f"Колір: {self.color}")
        
class Car(Vehicle):
    def __init__(self, brand, model, year, color, number_of_doors, engine_type):
        super().__init__(brand, model, year, color)
        self.number_of_doors = number_of_doors
        self.engine_type = engine_type

    def print_info(self):
        super().print_info()
        print(f"Кількість дверей: {self.number_of_doors}")
        print(f"Тип двигуна: {self.engine_type}")
        print()

class Truck(Vehicle):
    def __init__(self, brand, model, year, color, carrying_capacity):
        super().__init__(brand, model, year, color)
        self.carrying_capacity = carrying_capacity

    def print_info(self):
        super().print_info()
        print(f"Вантажопідйомність: {self.carrying_capacity} tons")
        print()

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, color, engine_capacity):
        super().__init__(brand, model, year, color)
        self.engine_capacity = engine_capacity

    def print_info(self):
        super().print_info()
        print(f"Об'єм двигуна: {self.engine_capacity} cc")
        print()

car = Car("Toyota", "Camry", 2020, "Blue", 4, "Petrol")
truck = Truck("Mercedes-Benz", "Actros", 2018, "White", 20)
motorcycle = Motorcycle("Yamaha", "MT-07", 2022, "Black", 689)

car.print_info()
truck.print_info()
motorcycle.print_info()