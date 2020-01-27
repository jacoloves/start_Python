class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return '''T have many attachments:
    My laser, to %s.
    My Claw, to %s.
    My smartphone, to %s.''' % (
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does()
        )

robbie = Robot()
print(robbie.does())