class Vehicle:
    def __init__(self,color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer

    def drive(self):
        print("Iam driving my {} {}".format(self.color, self.manufacturer))

    def gas(self):
        print("Fuel the car")


class Motorcycle(Vehicle):
    def helmet(self):
        print("Put on your helmet")
class car(Vehicle):
    def wipe(self):
        print("Wipe your windshield")


my_car = car('Black', 'Honda')
print(my_car.color)
print(my_car.manufacturer)
my_car.drive()
my_car.gas()
my_car.wipe()
