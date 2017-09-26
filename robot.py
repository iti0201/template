import time


class Robot:
    """
    The three primitives robotic paradigm: sense, plan, act [1].
    Sense - gather information using the sensors
    Plan - create a world model using all the information and plan the next move
    Act - carry out the next step of the plan using actuators

    [1] https://en.wikipedia.org/wiki/Robotic_paradigm
    """
    def __init__(self):
        self.start_timestamp = time.time()
        self.problem_solved = False

    def sense(self):
        print("Sensing...")

    def plan(self):
        print("Planning...")

    def act(self):
        print("Acting...")

    def main(self):
        while not self.problem_solved and time.time() - self.start_timestamp < 1:
            self.sense()
            self.plan()
            self.act()
        if self.problem_solved:
            print("Solved! Good job, robot!")
        else:
            print("Unable to solve! :(")


if __name__ == "__main__":
    robot = Robot()
    robot.main()
