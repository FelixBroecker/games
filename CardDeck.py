
class CardDeck:
    def __init__(self, deck="52", pattern="german"):
        self.deck = deck
        self.pattern = pattern
        self.card_base = []
        self.card_deck = []
        self.n = []
        self.suits = [
            "diamonds", 
            "clubs", 
            "hearts", 
            "spades"
        ]
        self.load_card_base()
        self.load_card_deck()

    def load_card_base(self):
        """"""
        numbers = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
        ]
        pattern = self.get_pattern(self.pattern)
        self.card_base = numbers + pattern


    def load_card_deck(self):
        """"""
        if self.deck == "52":
            self.card_deck = self.generate_card_deck(self.suits,0,12)
        elif self.deck == "32":
            self.card_deck = self.generate_card_deck(self.suits,5,12)
        elif self.deck == "55":
            self.card_deck = self.generate_card_deck(self.suits,0,12) + self.get_joker(3)
        elif self.deck == "2x52":
            deck = self.generate_card_deck(self.suits,0,12)
            self.card_deck = deck + deck.copy()
        elif self.deck == "2x32":
            deck = self.generate_card_deck(self.suits,5,12)
            self.card_deck = deck + deck.copy()
        elif self.deck == "2x55":
            deck = self.generate_card_deck(self.suits,0,12) + self.get_joker(3)
            self.card_deck = deck + deck.copy()

    def generate_card_deck(self, card_suits, lower, upper):
        """"""
        allowed_suits = [
            "diamonds", 
            "clubs", 
            "hearts", 
            "spades"
            ]
        
        deck = []

        for suit in card_suits:
            assert suit in allowed_suits, "card suit is not allowed"
            for card in self.card_base[lower:upper+1]:
                deck.append([suit, card])
        return deck
        
    
    def get_pattern(self, typ):
        """"""
        allowed_typ = [
            "english",
            "french",
            "german",
            "polish",
            "danish",
            "dutch",
            "icelandic",
            "swedish",
            "latvian",
            "russian"
        ]

        assert typ in allowed_typ, "selected pattern does not exist"

        if typ == "english":
            return ["J", "Q", "K", "A"]
        elif typ == "french":
            return ["V", "D", "R", "1"]
        elif typ == "german":
            return ["B", "D", "K", "A"]
        elif typ == "polish":
            return ["W", "D", "K", "A"]
        elif typ == "danish":
            return ["Kn", "D", "K", "Es"]
        elif typ == "dutch":
            return ["B", "V", "H", "A"]
        elif typ == "icelandic":
            return ["G", "D", "K", "A"]
        elif typ == "swedish":
            return ["Kn", "D", "K", "E"]
        elif typ == "latvian":
            return ["S", "D", "K", "1"]
        elif typ == "russian":
            return ["В", "Д", "K", "T"]
        else:
            return []
        
    def get_joker(self, n):
        """"""
        joker = []
        for _ in range(n):
            joker.append(["star", "S"])
        return joker