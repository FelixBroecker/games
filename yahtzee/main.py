import random
import time
import sys
from Draw import Draw
#import tty
#import termios

class Yahtzee():
    def __init__(self):
        self.dices = [0, 0, 0, 0, 0]
        self.hold = [False, False, False, False, False]
        self.players = []
        self.dw = Draw()

    def get_key(self):
        """get key from user"""
    #    fd = sys.stdin.fileno()
    #    old_settings = termios.tcgetattr(fd)
    #    try:
    #        tty.setraw(fd)
    #        key = sys.stdin.read(1)  # Read a single character
    #    finally:
    #        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        self.dw.draw_information("Which dices do you want to hold? Please give the positions as numbers without spaces in between.")
        key = input()
        return key

    def ask_player_amount(self):
        self.dw.draw_information("How many players want to play?")
        player_amount = input()
        return int(player_amount)

    def add_player(self):
        self.dw.draw_information("Please add the name of a player.")
        player = input()
        self.players.append(player)

    def roll(self):
        """Roll the dices that are not hold"""
        for i in range(5):
            if not self.hold[i]:
                self.dices[i] = random.randint(1, 6)
        self.reset_dices()
        self.dw.draw_all_dices(self.dices)
        ...

    def keep_dice(self):
        """
        Function that asks user to choose which dices to hold or to stop rolling.
        """
        key = self.get_key()
        to_hold_string  = list(key)
        to_hold = [int(i)-1 for i in to_hold_string]
        for i in to_hold:
            self.hold[i] = True
        ...

    def reset_dices(self):
        """Reset the dices to not hold"""
        self.hold = [False, False, False, False, False]

    def main(self):
        """Main function that runs the game"""
        player_amount = self.ask_player_amount()
        for i in range(player_amount):
            self.add_player()
        self.dw.draw_information("Let's start.")
        for j in range(2):#eigentlich 13 rounds
            self.dw.draw_information(f"Round {j+1}")
            for k in self.players:
                self.dw.draw_information(f"{k} rolls the dices.")
                for i in range(3):
                    if all(self.hold) == True:
                        break
                    self.roll()
                    if i < 2:
                        self.keep_dice()
                #TODO: initialize game card for each player
                #TODO: show game card
                #TODO: load dices in game card
                #TODO: choose category
                #TODO: show updated game card
                self.reset_dices()
        self.dw.draw_information("Game Over")
        # TODO iterate over rounds (13 max)
        # TODO ask player to make choice
        # TODO update score card
        # TODO visualize score card and dices
        # TODO collect all points of each player from card and determine winner

game = Yahtzee()
game.main()
