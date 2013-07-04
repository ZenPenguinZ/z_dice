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
              result.append(str(d))
        return "\n ".join(result)
    def fill_hand(self, dice_cup):
        if len(self.dice) == self.HAND_SIZE:
            return self.dice
        for x in range(len(self.dice),self.HAND_SIZE):
            self.dice.append(dice_cup.get_die())
    def score_hand(self):
        for i,d in enumerate(self.dice):
            pass #waiting for some logic functions in Die()

p = Dice_Cup()
h = Hand()

print "len of hand = ",len(h.dice)
h.fill_hand(p)
print "len of hand = ",len(h.dice)
print h
