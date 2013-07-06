#!/usr/bin/python
# Filename: dice.py

from dice import Die
from pool import Dice_Cup
from hand import Hand
from players import Player, Players_Group

play_group = Players_Group()
for player in ["Dave","Dawn","Dugg"]:
    play_group.add_player(player)
    


play_group.shuffle_players()
game_on = True

while game_on:
    for current_player in play_group.player_group:
        print play_group
        print "---- Ok %s, it's your turn ----" %(current_player.name)
        cup = Dice_Cup()    #init dice cup
        cup.shuffle()       #shuffle the 13 die
        hand = Hand()       #init hand
        turn = True
        while turn:
            print "brains = %s shots = %s" %(hand.brains,hand.shots)
            print "hand -> %s" %(hand)
            input = raw_input("(y) to roll, (n) to quit and bank your brains")
            if str(input.lower()) == "n":
                current_player.bank_brains(hand.brains)
                if current_player.has_won():
                    print "))))---- YOU WON! ----((((("
                    game_on == False
                    break
                else:
                    turn = False

            else:
                hand.fill_hand(cup) #fill hand from cup
                hand.roll_hand()    #roll hand
                print hand
                #input = raw_input("this is your roll")
                if not hand.score_hand():
                    print "Bang! your dead, turn over"
                    turn = False
                else:
                    if current_player.has_won():
                        print "))))---- YOU WON! ----((((("
                        game_on == False
                        #break
                    else:
                        print "you servived this time ", current_player.name
        print "end of turn loop"

