import time

class Robot:
    """
    The three primitives robotic paradigm: sense, plan, act [1].
    Sense - gather information using the sensors
    Plan - create a world model using all the information and plan the next move
    Act - carry out the next step of the plan using actuators

    [1] https://en.wikipedia.org/wiki/Robotic_paradigm
    """
    def __init__(self, team_id):
        self.team_id = team_id

    def sense(self):
        print("Sensing...")

    def plan(self):
        print("Planning...")

    def act(self):
        print("Acting...")
        time.sleep(1)

    def main(self):
        self.problem_solved = False
        while not self.problem_solved:
            self.sense()
            self.plan()
            self.act()


if __name__ == "__main__":
    robot = Robot(123)
    robot.main()
