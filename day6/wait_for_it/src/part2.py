import re

import numpy as np

inp = """Time:      7  15   30
Distance:  9  40  200"""


def find_records(time: int, dist: int) -> int:
    num_records = 0
    for t0 in range(1, int(np.ceil(time / 2))):
        if t0 * (time - t0) > dist:
            num_records += 2
    if time % 2 == 0:
        num_records += 1
    return num_records


if __name__ == "__main__":
    with open("./day6/wait_for_it/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    time = int("".join(re.findall(r"\d+", inp.splitlines()[0])))
    distance = int("".join(re.findall(r"\d+", inp.splitlines()[1])))
    total = find_records(time, distance)
    print(total)
