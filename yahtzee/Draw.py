import time
import random
import sys
class Draw:
    def __init__(self):
        ...
        # TODO maybe initialize a dice (can have different number of sides and
        # pips)

    def draw_single_dice(self, n_pip: int) -> list[str]:
        """Function that prints a single dice in terminal"""
        # initalize ascii art for dice

        dice_faces = {
            1: "-----\n|   |\n| * |\n|   |\n-----",
            2: "-----\n|*  |\n|   |\n|  *|\n-----",
            3: "-----\n|*  |\n| * |\n|  *|\n-----",
            4: "-----\n|* *|\n|   |\n|* *|\n-----",
            5: "-----\n|* *|\n| * |\n|* *|\n-----",
            6: "-----\n|* *|\n|* *|\n|* *|\n-----"
        }
        
        # Print dice faces in the same row (for multiple dice)
        # Split the dice face into lines
        return dice_faces[n_pip].split('\n')

    def draw_all_dices(self, n_pips: list[int], hold: list[bool], round: int, player_round: int) -> None:
        """Function that prints all dices in terminal
        
        This will roll each dices after another with small animation effect.
        """
        all_dice_faces = [self.draw_single_dice(pip) for pip in n_pips]
        # dice roll animation effect
        
        #if player_round != 0:
        #    # clear previous line
        #    sys.stdout.write("\033[F")
        #    print("")
        #    print("\033[F"  * 7, end="")
        #    
        for i in range(10):  

            # only randomize where hold is False
            randomized_faces = [
                self.draw_single_dice(random.randint(1, 6)) if not hold[i] else all_dice_faces[i]
                for i in range(len(n_pips))
            ]
            #print(randomized_faces)
            print("\n".join("   ".join(face) for face in zip(*randomized_faces)))
            # label the dice with numbers (1-5)
            
            # clear the dice output
            print("\033[F"  * 5, end="")  # Move cursor up to overwrite dice
            time.sleep(0.3)

        # Print the final result
        print("\n".join("   ".join(face) for face in zip(*all_dice_faces)))
        print(f" (1)     (2)     (3)     (4)     (5)  ")
    

    def draw_game_card(self, gamecard) -> None:
        """Function that draws a card in terminal"""
        print(gamecard.keys())

    def draw_information(self, information) -> None:
        """Function that draws information in terminal"""
        print(information)

#test
#game = Draw()
#game.draw_single_dice(3)
#game.draw_all_dices([1, 2, 3, 4, 5])
#gamecard = {"Ones": {"score": [], "occupied": [], "value": 1}, "Twos": {"score": [], "occupied": [], "value": 2}}
#game.draw_game_card(gamecard)