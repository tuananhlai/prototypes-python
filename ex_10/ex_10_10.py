class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class SmartPhone:
    def does(self):
        return 'ring'
    
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        result = f"""
Laser: {self.laser.does()}
Claw: {self.claw.does()}
SmartPhone: {self.smartphone.does()}"""
        return result.strip()

robot = Robot()
print(robot.does())