#!/usr/bin/python
# Filename: dice.py

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

class Players_Group(object):
    """Defines the group of players in a round robbin linked list"""
    player_group = []
    def __init__(self, player_group=None):
        if player_group is None:
            player_group = []
            self.player_group = player_group
    def __repr__(self):
        temp = []
        for i in self.player_group:
            temp.append(i.__repr__())
        return "\n".join(temp)
    def add_player(self, name):
        self.player_group.append(Player(name))



        
        
