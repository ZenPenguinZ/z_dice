#!/usr/bin/python
# Filename: dice.py

from dice import Die
from pool import Dice_Cup

class Hand(object):
    HAND_SIZE = 3
    def __init__(self, shots = 0, brains = 0):
        self.shots = shots
        self.brains = brains
        self.dice = []
    def __repr__(self):
        result = []
        for d in self.dice:
            result.append(d.__repr__())
        return "|".join(result) + "\n"
    def fill_hand(self, dice_cup):
        if len(self.dice) == self.HAND_SIZE:
            return self.dice
        for x in range(len(self.dice),self.HAND_SIZE):
            self.dice.append(dice_cup.get_die())
    def roll_hand(self):
        for d in self.dice:
            d.roll_die()
    def score_hand(self):
        for i in range(len(self.dice)):
            temp_die = self.dice.pop(0)  #pop first die in hand
            if temp_die.is_brains():
                self.brains += 1
            if temp_die.is_shot():
                if self.shots >= 2:
                    print "Your Dead! End of turn"
                    return False  #your Dead, turn over
                self.shots += 1
            if temp_die.is_run():
                self.dice.append(temp_die) #append back to last die in hand
        return True #you survived



p = Dice_Cup()
print p
p.shuffle()
h = Hand()

h.fill_hand(p)
h.roll_hand()
print h
while h.score_hand() and h.brains < 13:
    print "brains = ",h.brains,"shots = ",h.shots
    h.fill_hand(p)
    print "rolling"
    h.roll_hand()
    print h
print "You win with %s brains in the bag" % (h.brains)
