import time
import random
import sys
import tty
import termios
from CardDeck import CardDeck
from DrawCard import DrawCard

class Krich:
    def __init__(self):
        self.wait = 1.5
        self.fieldwidth = 100
        self.fieldspace = 10
        self.value = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "B": 11,
            "D": 12,
            "K": 13,
            "A": 14,
            "S": 15,
        }

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def get_depiction(self, card, typ="plain"):
        """"""
        symbol = {
            "diamonds": "♦️",
            "clubs": "♣️",
            "hearts": "♥️",
            "spades": "♠️",
        }
        if typ == "plain":
            return(card)
        elif typ == "illustrate":
            u=  f"{card[1]:<9}"
            l=  f"{card[1]:>2}"
            return(
f"""/===========\\
| {u} |
|           |
|     {symbol[card[0]]}     |
|           |
|        {l} |
\\===========/
""")

    def print_out(self, out, length):
        """"""
        print("\033[H\033[J", end="")
        for line in out:
            print(line)
        print("\n" * (length - len(out)))

    def show_cards(self, cards_a: list, cards_b: list, mask=[]):
        """"""
        space = 2
        cardlength = 7
        cardwidth = 13

        filler = (self.fieldwidth//2 - len(cards_a) *
                  (space+cardwidth) + self.fieldspace//2)

        if not mask:
            mask = [True for _ in cards_a]
            print(mask)

        for i, card in enumerate(cards_a):
            if not mask[i]:
                card = ["?", "?"]
            a = DrawCard([])
            a.get_depiction(card)
            s = DrawCard([])
            s.card_space(space,cardlength)
            if i == 0:
                res_a = s + a
            else:
                res_a = (res_a + s) + a

        s = DrawCard([])
        s.card_space(filler,cardlength)
        res = res_a + s

        if cards_b:
            for i, card in enumerate(cards_b):
                if not mask[i]:
                    card = ["?", "?"]
                a = DrawCard([])
                a.get_depiction(card)
                s = DrawCard([])
                s.card_space(space,cardlength)
                if i == 0:
                    res_b = a
                else:
                    res_b = (res_b + s) + a

            res = res + res_b
        return res.cards

    def game_round(self, card_deck):
        """"""
        length = 12
        user_input = True

        space = " "
        format_1word = f"{{:<{self.fieldwidth+self.fieldspace}}}"
        format_2words = f"{{:^{self.fieldwidth//2}}}{self.fieldspace*space}{{:^{self.fieldwidth//2}}}"
        format_4words = f"{{:^{self.fieldwidth//4}}}{{:^{self.fieldwidth//4}}}{self.fieldspace*space}{{:^{self.fieldwidth//4}}}{{:^{self.fieldwidth//4}}}"

        out = []
        out.append("Shuffle the cards.")
        self.print_out(out, length)

        random.shuffle(card_deck)
        time.sleep(self.wait)

        out.append("Deal the cards.")
        self.print_out(out, length)

        hand_a = card_deck[:len(card_deck)//2]
        hand_b = card_deck[len(card_deck)//2:]
        discard_pile_a = []
        discard_pile_b = []
        time.sleep(self.wait)

        out.append(f"Player A got {len(hand_a)} cards.")
        out.append(f"Player B got {len(hand_b)} cards.")
        self.print_out(out, length)

        time.sleep(self.wait)

        out.append("Player A begins!")
        self.print_out(out, length)

        time.sleep(self.wait)


        while len(hand_a)+len(discard_pile_a) and len(hand_b)+len(discard_pile_b):
            out = []
            out.append(format_2words.format("Player A", "Player B"))
            out.append(format_4words.format(
                "pile", "discard pile", "pile", "discard pile"
                ))
            out.append(format_4words.format(
                f"{len(hand_a)}", f"{len(discard_pile_a)}",
                f"{len(hand_b)}", f"{len(discard_pile_b)}"
                ))
            out.append("")
            self.print_out(out, length)

            time.sleep(self.wait)

            if user_input:
                invalid = True
                while invalid:
                    key = self.get_key()
                    if key == "a":
                        invalid = False
                    elif key == "p":
                        invalid = False
                        user_input = False
                    elif key == "f":
                        invalid = False
                        user_input = False
                        self.wait = 0
                    elif key == "w":
                        out.append("Felix won the game!")
                        self.print_out(out,length)
                        exit()
                    elif key == "e":
                        out.append("Brutal kill")
                        self.print_out(out,length)
                        exit()


            cards = self.show_cards([hand_a[-1]],[])
            out += cards
            self.print_out(out, length)
            del out[-7:]

            if user_input:
                invalid = True
                while invalid:
                    key = self.get_key()
                    if key == "b":
                        invalid = False

            cards = self.show_cards([hand_a[-1]],[hand_b[-1]])
            out += cards
            self.print_out(out, length)

            time.sleep(self.wait)

            if self.value[hand_a[-1][1]] > self.value[hand_b[-1][1]]:

                out.append("A is larger.")
                self.print_out(out, length)
                del out[-1]

                discard_pile_a.append(hand_a[-1])
                discard_pile_a.append(hand_b[-1])
                del hand_a[-1]
                del hand_b[-1]

            elif self.value[hand_b[-1][1]] > self.value[hand_a[-1][1]]:

                out.append("B is larger.")
                self.print_out(out, length)
                del out[-1]

                discard_pile_b.append(hand_a[-1])
                discard_pile_b.append(hand_b[-1])
                del hand_a[-1]
                del hand_b[-1]

            else:
                out.append(format_1word.format("KRICH!!!"))
                self.print_out(out, length)
                del out[-1]

                time.sleep(self.wait)

                same = True
                n=3

                while same:
                    # check if Krisch is possible
                    if len(hand_a) + len(discard_pile_a) < n:
                        hand_b += hand_a.copy()
                        hand_b += discard_pile_a.copy()
                        hand_a = []
                        discard_pile_a = []
                        break
                    elif len(hand_a) + len(discard_pile_a) < n:
                        hand_a += hand_b.copy()
                        hand_a += discard_pile_b.copy()
                        hand_a = []
                        discard_pile_b = []
                        break
                    # check if discarded pile has to be unied with hand cards
                    if len(hand_a)<n:
                        hand_a = discard_pile_a.copy() + hand_a
                        discard_pile_a = []
                    if len(hand_b)<n:
                        hand_b = discard_pile_b.copy() + hand_b
                        discard_pile_b = []

                    same = self.value[hand_a[-n][1]] == self.value[hand_b[-n][1]]

                    del out[-7:]

                    cards = self.show_cards(
                        hand_a[-n:][::-1],
                        [],
                        mask = [True,False,True]*(n//3)
                        )
                    out += cards

                    if user_input:
                        invalid = True
                        while invalid:
                            key = self.get_key()
                            if key == "a":
                                invalid = False

                    self.print_out(out, length)
                    del out[-7:]

                    cards = self.show_cards(
                        hand_a[-n:][::-1],
                        hand_b[-n:][::-1],
                        mask = [True,False,True]
                        )
                    out += cards

                    if user_input:
                        invalid = True
                        while invalid:
                            key = self.get_key()
                            if key == "b":
                                invalid = False

                    self.print_out(out, length)
                    time.sleep(self.wait)

                    del out[-7:]

                    cards = self.show_cards(
                        hand_a[-n:][::-1],
                        hand_b[-n:][::-1],
                        )
                    out += cards
                    self.print_out(out, length)


                    time.sleep(2*self.wait)

                    if self.value[hand_a[-n][1]] > self.value[hand_b[-n][1]]:

                        out.append("A is larger.")
                        self.print_out(out, length)
                        del out[-1]


                        discard_pile_a += hand_a[-n:]
                        discard_pile_a += hand_b[-n:]
                        del hand_a[-n:]
                        del hand_b[-n:]
                    elif self.value[hand_b[-n][1]] > self.value[hand_a[-n][1]]:

                        out.append("B is larger.")
                        self.print_out(out, length)
                        del out[-1]

                        discard_pile_b += hand_b[-n:]
                        discard_pile_b += hand_a[-n:]
                        del hand_a[-n:]
                        del hand_b[-n:]
                    else:
                        n += 3

            if not hand_a:
                hand_a = discard_pile_a.copy()
                discard_pile_a = []
            if not hand_b:
                hand_b = discard_pile_b.copy()
                discard_pile_b = []

            time.sleep(self.wait)

        if hand_a:
            out.append("Player A won!")
        else:
            out.append("Player B won!")
        self.print_out(out, length)




deck  = input("Choose a deck to play with (32, 52, 55, 2x32, 2x52, 2x55)")
print("\033[H\033[J", end="")
cD = CardDeck(deck=deck, pattern="german")
deck = cD.card_deck
game = Krich()
game.game_round(deck)
