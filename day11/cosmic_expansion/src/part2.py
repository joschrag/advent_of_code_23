import re
from dataclasses import dataclass
from itertools import combinations

import numpy as np

inp = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


@dataclass
class Galaxy:
    row: int
    col: int


if __name__ == "__main__":
    with open("./day11/cosmic_expansion/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    galaxies = []
    n = len(inp.splitlines())
    m = len(inp.splitlines()[0])
    rows: set = set()
    cols: set = set()
    total = 0
    factor = 1_000_000
    for i, line in enumerate(inp.splitlines()):
        res = re.finditer(r"#", line)
        for obj in res:
            galaxies.append(Galaxy(i, obj.start()))
            rows.add(i)
            cols.add(obj.start())

    double_rows = set(range(n)).difference(rows)
    double_cols = set(range(m)).difference(cols)
    for g1, g2 in combinations(galaxies, 2):
        r_start, r_stop = sorted([g1.row, g2.row])
        c_start, c_stop = sorted([g1.col, g2.col])
        num_double_rows = [
            factor - 1 if r_start < row < r_stop else 0 for row in double_rows
        ]
        num_double_cols = [
            factor - 1 if c_start < col < c_stop else 0 for col in double_cols
        ]
        dist = (
            abs(g1.row - g2.row)
            + abs(g1.col - g2.col)
            + sum(num_double_rows)
            + sum(num_double_cols)
        )
        total += dist
    print(total)
