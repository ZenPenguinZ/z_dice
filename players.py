class Player(object):
    """ defines an individual player"""
    WINNING_BRAIN_COUNT = 13
    def __init__(self, name, brain_count = 0):
        self.name = name
        self.brain_count = brain_count
    def __repr__(self):
        return "player " + self.name + " has " + str(self.brain_count) + " brains."
    def has_won(self):
        if self.brain_count >= self.WINNING_BRAIN_COUNT:
            return True
        else:
            return False


