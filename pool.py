#!/usr/bin/python
# Filename: dice.py

from dice import Die
from random import shuffle

class Dice_Cup(object):
    NUMBER_RED = 3
    NUMBER_GREEN = 6
    NUMBER_YELLOW = 4
    POOL_SIZE = 13
    cup = []
    assert NUMBER_RED + NUMBER_GREEN + NUMBER_YELLOW  == POOL_SIZE
    def __init__(self):
        print "init"
        for x in range(self.NUMBER_RED):
             self.cup.append(Die("red"))
        for x in range(self.NUMBER_GREEN):
            self.cup.append(Die("green"))
        for x in range(self.NUMBER_YELLOW):
            self.cup.append(Die("yellow"))
        self.shuffle()
    def __repr__(self):
        result = []
        for d in self.cup:
              result.append(str(d))
        return "\n ".join(result)
    def shuffle(self):
        return shuffle(self.cup)
    def get_die(self):
        self.shuffle()
        return self.cup.pop()


pool = Dice_Cup()
print len(pool.cup)
print pool
pool.shuffle()
print ""

print pool.get_die()
print len(pool.cup)
print pool.get_die()
print len(pool.cup)
print pool.get_die()
print len(pool.cup)
print pool.get_die()
print len(pool.cup)
print pool.get_die()
print len(pool.cup)
print pool.get_die()
print len(pool.cup)
