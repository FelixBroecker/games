from sys import argv

if __name__ == "__main__":
    if len(argv) == 3 and all(
        arg.isdigit() and int(arg) > 0 for arg in argv[1:]
    ):
        n_rows = int(argv[1])
        move_limit = int(argv[2])
        rows = [2 * i + 1 for i in range(n_rows)]
        width = rows[-1]
        pads = [" " * (n_rows - i - 1) for i in range(n_rows)]
        i = 0
        idxs = ("1st", "2nd")
        while len(rows) > 0:
            print()
            for row, pad in zip(rows, pads):
                string = "|" * row + pad
                print(" " * (width - len(string)) + string + f" {row}")
            num = ""
            while not num.isdigit() or not (
                1 <= int(num) <= min(move_limit, rows[0])
            ):
                num = input(f"{idxs[i]} player: ")
            i = (i + 1) % 2
            rows[0] -= int(num)
            if rows[0] == 0:
                del rows[0]
                del pads[0]
        print()
        print(f"{idxs[i]} player wins!")
    else:
        print("Usage: python nim.py <number-of-rows> <move-limit>")
