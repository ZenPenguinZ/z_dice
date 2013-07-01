#!/usr/bin/python
# Filename: dice.py

from random import randrange

class Die(object):
    """takes a color attr and defines a die"""
    NUMBER_SIDES = 6
    BRAINS = "brains"
    SHOT = "shot"
    RUN = "run"
    GREEN =    (BRAINS,SHOT,RUN,BRAINS,RUN,BRAINS)
    YELLOW = (BRAINS,RUN,SHOT,BRAINS,RUN,SHOT)
    RED =         (SHOT,RUN,SHOT,BRAINS,SHOT,RUN)
    assert len(GREEN) ==  NUMBER_SIDES and  len(RED) ==  NUMBER_SIDES and  len(YELLOW) ==  NUMBER_SIDES
    def __init__(self, sides, side_up = 0):
        if sides == "green":
            self.sides = self.GREEN
        elif sides == "yellow":
            self.sides = self.YELLOW
        elif sides == "red":
            self.sides = self.RED
        else:
            return False
        self.side_up = side_up
    def __repr__(self):
        return  "the dice has 6 sides the side that is up is %s" % self.sides[self.side_up]
    def roll_die(self):
        self.side_up = random.randrange(self.NUMBER_SIDES)

