import re

import numpy as np


def get_digits(text: str) -> int:
    """Get the sum of the first and last digit in text.

    :param text: input text
    :type text: str
    :return: stringsum of first and last digit (can be dame digit)
    :rtype: int
    """
    text = pattern.sub(lambda x: word_to_num[x.group()], text)
    # sub twice to replace overlapping numbers
    text = pattern.sub(lambda x: word_to_num[x.group()], text)
    digits = list(filter(str.isdigit, text))
    return int(digits[0] + digits[-1])


# Add first and last letter for overlapping numbers e.g. twoneight
word_to_num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

pattern = re.compile("|".join(re.escape(k) for k in word_to_num))

if __name__ == "__main__":
    with open("./day1/trebuchet/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    arr = np.array(inp.splitlines())
    total = np.sum(list(map(get_digits, arr)))
    print(total)
