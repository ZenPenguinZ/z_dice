class Die(object):
    """takes a color attr and defines a die"""
    NUMBER_SIDES = 6
    BRAINS = "brains"
    SHOT = "shot"
    RUN = "run"
    GREEN = (BRAINS,SHOT,RUN,BRAINS,RUN,BRAINS)
    YELLOW = (BRAINS,RUN,SHOT,BRAINS,RUN,SHOT)
    RED = (SHOT,RUN,SHOT,BRAINS,SHOT,RUN)
    assert len(GREEN) ==  NUMBER_SIDES and  len(RED) ==  NUMBER_SIDES and  len(YELLOW) ==  NUMBER_SIDES
    def __init__(self, sides, side_up = 0):
        if self.sides == "green":
            self.sides = GREEN
        elif self.sides == "yellow":
            self.sides = YELLOW
        elif self.sides == "red":
            self.sides = RED
        else:
            return False
    def __repr__(self):
        return slef.sides,self.sides[self.side_up]

d = Die("red")
print d
