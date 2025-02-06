class DrawCard:
    def __init__(self, cards):
        self.cards = cards
        self.string = ""

    def __add__(self, other):
        if isinstance(other, DrawCard):
            # Perform element-wise addition
            return DrawCard([a.replace("\n","") + b for a, b in zip(self.cards, other.cards)])
        else:
            raise TypeError("Unsupported operand type(s) for +: 'CustomList' and other")

    def __repr__(self):
        return f"{self.cards}"

    def get_cards(self):
        return self.cards

    def get_depiction(self, card: list,):
        """"""
        symbol = {
            "diamonds": "♦️",
            "clubs": "♣️",
            "hearts": "♥️",
            "spades": "♠️",
            "star": "🤡",
            "?": "⍰",
        }

        u=  f"{card[1]:<9}"
        l=  f"{card[1]:>2}"
        self.cards = [
                f"/============\\",
                f"| {u}  |",
                f"|            |",
                f"|     {symbol[card[0]]}      |",
                f"|            |",
                f"|         {l} |",
                f"\\============/",
            ]

    def lst_to_str(self) -> str:
        """"""
        out = ""
        for i, line in enumerate(self.cards):
            out += line
            if i != len(self.cards)-1:
                out += "\n"
        self.string = out

    def card_space(self, width: int, lines: int, linebr=False) -> str:
        """"""
        out = []
        for i in range(lines):
            tmp = ""
            tmp += width * " "
            if i != lines-1 and linebr:
                tmp += "\n"
            out.append(tmp)
        self.cards = out
