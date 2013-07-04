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
    def score_hand(self):
        for i in range(len(self.dice)):
            temp_die = self.dice.pop(0)  #pop first die in hand
            if temp_die.is_brains():
                self.brains += 1
                print "score brains"
            if temp_die.is_shot():
                if self.shots >= 2:
                    print "end of turn"
                self.shots += 1
            if temp_die.is_run():
                self.dice.append(temp_die) #append back to last die in hand



        """
        for i,d in enumerate(self.dice):
            print "in score_hand ",i
            if d.is_brains():
                self.brains += 1
                print "score brains"
                del d  #self.dice[i]
            elif d.is_shot():
                if self.shots >= 2:
                    print "end of turn"
                self.shots += 1
                del d  #self.dice[i]
                print   "score shot"
            elif d.is_run():
                print "runner, keep in hand"
            else:
                print "error"
"""
p = Dice_Cup()
h = Hand()
#print "empty hand ",h, "length",len(h.dice)

h.fill_hand(p)
print "filled hand ",h, "length",len(h.dice)
h.score_hand()
print "brains = ", h.brains, "shots = ",h.shots
print "hand after scoreing",h, "length",len(h.dice)

