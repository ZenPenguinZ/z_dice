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
        if self.is_green:
            return "Green %s" % self.sides[self.side_up]
        elif self.is_yellow:
            return "Yellow %s" % self.sides[self.side_up]
        elif self.is_red:
            return "Red %s" % self.sides[self.side_up]
        else:
            return "error"
    def roll_die(self):
        self.side_up = randrange(self.NUMBER_SIDES)
#is Color series, returns true if match
    def is_green(self):
        return self.sides == self.GREEN
    def is_yellow(self):
        return self.sides == self.YELLOW
    def is_red(self):
        return self.sides == self.RED
#is Action series,  returns true if match
    def is_brains(self):
        return self.sides[self.side_up] == self.BRAINS
    def is_shot(self):
        return self.sides[self.side_up] == self.SHOT
    def is_run(self):
        return self.sides[self.side_up] == self.RUN

d = Die("yellow")
b = 0
r = 0
s = 0
for i in range(999):
    d.roll_die()
    print d
#    print d
    if d.is_brains():
        b +=1
    elif d.is_shot():
        s +=1
    elif d.is_run():
        r +=1
    else:
        print "error",
print ""
print "b",b," r",r," s",s
        
