import re

inp = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


if __name__ == "__main__":
    with open("./day8/haunted_wasteland/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    map_dict = {}
    total = 0
    direct = inp.splitlines()[0]
    for line in inp.splitlines()[2:]:
        key, val1, val2 = re.findall(r"\w{3}", line)
        map_dict[key] = (val1, val2)
    cur_key = "AAA"
    while cur_key != "ZZZ":
        ind = 0 if direct[total % len(direct)] == "L" else 1
        total += 1
        cur_key = map_dict[cur_key][ind]
    print(total)
