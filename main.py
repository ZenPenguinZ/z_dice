#!/usr/bin/python
# Filename: dice.py

from dice import Die
from pool import Dice_Cup
from hand import Hand


games = 0
while True:
    p = Dice_Cup()
    p.shuffle()
    h = Hand()
    rolls = 0
    h.fill_hand(p)
    h.roll_hand()
    #print h
    while h.score_hand()and h.brains < 13:
        #print "brains = ",h.brains,"shots = ",h.shots
        h.fill_hand(p)
        #print "rolling"
        h.roll_hand()
        rolls += 1
        #print h
    print "End of Game, rolles = ",rolls," brains = ",h.brains
    games += 1
    if h.shots < 3:
        print "You win with %s brains in the bag" % (h.brains)
        print "------------------ Winner! ----------------------------"
        break
print "games = ",games

