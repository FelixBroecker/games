class Draw:
    def __init__(self):
        ...
        # TODO maybe initialize a dice (can have different number of sides and
        # pips)

    def draw_single_dice(self, n_pip: int) -> None:
        """Function that prints a single dice in terminal"""
        print(n_pip)

    def draw_all_dices(self, n_pips: list[int]) -> None:
        """Function that prints all dices in terminal"""
        for pip in n_pips:
            self.draw_single_dice(pip)

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