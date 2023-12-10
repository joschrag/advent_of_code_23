import math
import re

import numpy as np

inp = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


if __name__ == "__main__":
    with open("./day8/haunted_wasteland/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    map_dict = {}
    total = 0
    direct = inp.splitlines()[0]
    for line in inp.splitlines()[2:]:
        key, val1, val2 = re.findall(r"\w{3}", line)
        map_dict[key] = (val1, val2)
    cur_nodes = [node for node in map_dict.keys() if node[-1] == "A"]
    loop = np.zeros(len(cur_nodes), dtype=np.int32)
    while any((node[-1] != "Z" for node in cur_nodes)):
        ind = 0 if direct[total % len(direct)] == "L" else 1
        total += 1
        cur_nodes = [map_dict[node][ind] for node in cur_nodes]
        for i, node in enumerate(cur_nodes):
            if loop[i] == 0 and node[-1] == "Z":
                loop[i] = total
        if all(loop):
            break
    print(math.lcm(*loop))
