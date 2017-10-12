from ev3dev import ev3
import time

class Robot:
    def __init__(self):
        self.speed = 100
        self.btn = ev3.Button()
        self.motor_left = ev3.LargeMotor('outA')
        self.motor_right = ev3.LargeMotor('outD')

    def drive(self):
        self.motor_left.run_forever(speed_sp=self.speed * 4)
        self.motor_right.run_forever(speed_sp=self.speed * 4)

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()

def main():
    robot = Robot()

    while not robot.btn.any():
        time.sleep(0.2)
        robot.drive()
    robot.stop()

if __name__ == "__main__":
    main()
