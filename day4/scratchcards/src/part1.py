import re

# inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

pattern = re.compile(r"\d+")

if __name__ == "__main__":
    with open("./day4/scratchcards/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    total = 0
    for line in inp.splitlines():
        i = 0
        first_half, second_half = line.split("|")
        win_numbers = pattern.findall(first_half.split(":")[1])
        my_numbers = pattern.findall(second_half)
        for number in win_numbers:
            if number in my_numbers:
                i += 1

        total += 2 ** (i - 1) if i > 0 else 0
    print(total)
