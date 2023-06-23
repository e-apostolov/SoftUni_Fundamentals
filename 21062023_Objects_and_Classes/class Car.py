
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}\'s engine is starting")

    def drive(self, distance):
        print(f"The {self.make} {self.model} is driving {distance} kilometers")

    def stop_engine(self):
        print(f"The {self.make} {self.model}\'s engine is stopping")


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Mercedes", "S500", 2021)

print(car1.make)
print(car2.year)

car1.start_engine()
car2.start_engine()
car2.drive(300)