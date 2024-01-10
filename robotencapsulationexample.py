class Robot:
    def __init__(self):
        self.__battery_level = 100  # Private attribute

    def charge_battery(self):
        self.__battery_level = 100

    def check_battery(self):
        return self.__battery_level

    def talk(self):
        if self.__battery_level > 10:
            self.__battery_level -= 10
            print("Hello!")
        else:
            print("Battery too low. Charging...")
            self.charge_battery()

robot = Robot()
robot.talk()  # "Hello!"
print(robot.check_battery())  # 90
#print(robot.__battery_level)  # This would cause an error as __battery_level is private
robot.talk()  # 80
print(robot.check_battery())
robot.talk()  # 70
print(robot.check_battery())  # 70
robot.talk()  # 60
print(robot.check_battery())  # 60
robot.talk()  # 50
print(robot.check_battery())  # 50
robot.talk()  # 40
print(robot.check_battery())  # 40
robot.talk()  # 30
print(robot.check_battery())
robot.talk()  # 30
print(robot.check_battery())  # 30
robot.talk()  # 20
print(robot.check_battery())  # 20
robot.talk()  # 100
print(robot.check_battery())  # 100
robot.talk()  # 90
print(robot.check_battery())  # 90
