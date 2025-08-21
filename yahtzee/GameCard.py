class GameCard:
    def __init__(self):
        self.players = []
        self.dices = []
        self.possible_categories = [False] * 13
        self.upper_block = [
            "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"
            ]
        self.lower_block = [
            "Three of a kind", "Four of a kind", "Full House",
                       "Small Straight", "Large Straight", "Cnivvel", "Chance"
                       ]
        self.card = {
            "Ones": {
                "score": [],
                "occupied": [],
                "value": 1,
            },
            "Twos": {
                "score": [],
                "occupied": [],
                "value": 2,
            },
            "Threes": {
                "score": [],
                "occupied": [],
                "value": 3,
            },
            "Fours": {
                "score": [],
                "occupied": [],
                "value": 4,
            },
            "Fives": {
                "score": [],
                "occupied": [],
                "value": 5,
            },
            "Sixes": {
                "score": [],
                "occupied": [],
                "value": 6,
            },
            "Three of a kind": {
                "score": [],
                "occupied": [],
                "value": 0,
            },
            "Four of a kind": {
                "score": [],
                "occupied": [],
                "value": 0,
            },
            "Full House": {
                "score": [],
                "occupied": [],
                "value": 25,
            },
            "Small Straight": {
                "score": [],
                "occupied": [],
                "value": 30,
            },
            "Large Straight": {
                "score": [],
                "occupied": [],
                "value": 40,
            },
            "Cnivvel": {
                "score": [],
                "occupied": [],
                "value": 50,
            },
            "Chance": {
                "score": [],
                "occupied": [],
                "value": 0,
            },
        }

    def get_sum_of_pips_i(self, list_of_dices: list[int], pip) -> int:
        """Function that returns the sum of all dices"""
        if pip not in list_of_dices:
            return 0
        else:
            return list_of_dices.count(pip) * pip

    def get_sum_of_all_pips(self, list_of_dices: list[int]) -> int:
        """Function that returns the sum of all dices"""
        return sum(list_of_dices)


    def check_possible_categories(self) -> list[str]:
        """
        Function that gets the possible categories and calculates the values
        """
        # check upper block
        for key in self.upper_block:
            val = self.get_sum_of_pips_i(
                self.dices, self.card[key]["value"]
                )
            #print(val)
        return ["Ones", "Three of a kind", "Four of a kind", "Knivvel", "Chance"]


    def get_value(self, category: str) -> int:
        """"""
        ...

    def add_player(self, player: str) -> None:
        """Add player to the game"""
        self.players.append(player)
        for key in self.card:
            self.card[key]["score"].append(0)
            self.card[key]["occupied"].append(False)

    def choose_category(self, player: str, category: str, ) -> None:
        """
        Function that checks if category is not occupied yet for that player.
        Calculate score and update the card
        """
        print(f"Category '{category}' has been chose for {player}")
        print("Card will be updated")



    def get_all_points(self) -> int:
        """Function that returns the list winners from largest to smallest score"""
        return 42


# test
Player1 = GameCard()
Player1.add_player("Felix")
print(Player1.card.keys())
#print(game.check_possible_categories([1, 2, 3, 4, 5]))
dices = [1, 2, 3, 4, 5]

Player1.dices = dices # load dices in game card of player
print(Player1.dices)

possibilities = Player1.check_possible_categories()  # return list of possible categories
print(possibilities)
Player1.choose_category("Felix", possibilities[0])  # choose category for player

n_points = Player1.get_all_points()
print(n_points)
