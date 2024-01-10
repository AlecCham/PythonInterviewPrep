class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Truck(Vehicle):
    def move(self):
        print("The truck is moving slowly with a heavy load.")

class Airplane(Vehicle):
    def move(self):
        print("The airplane is flying in the sky.")

# Using the classes
car = Car()
truck = Truck()
airplane = Airplane()

for vehicle in [car, truck, airplane]:
    vehicle.move()
