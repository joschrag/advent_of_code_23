import re

import numpy as np

inp = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


if __name__ == "__main__":
    with open("./day9/mirage_maintenance/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    next_values = []
    total = 0
    for line in inp.splitlines():
        history = np.array(list(map(int, re.findall(r"-?\d+", line))))
        diffs = [history]
        while any(diffs[-1] != 0):
            diffs.append(np.diff(diffs[-1]))
        step = 0
        for obj in diffs[::-1]:
            step = obj[0] - step
        total += step
    print(total)
