class Car:
    def move(self):
        print("The car is driving on the road.")

class Truck:
    def move(self):
        print("The truck is moving slowly with a heavy load.")

class Airplane:
    def move(self):
        print("The airplane is flying in the sky.")

def start_moving(vehicle):
    vehicle.move()

car = Car()
truck = Truck()
airplane = Airplane()

start_moving(car)  # "The car is driving on the road."
start_moving(truck)  # "The truck is moving slowly with a heavy load."
start_moving(airplane)  # "The airplane is flying in the sky."
