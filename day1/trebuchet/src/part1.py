import numpy as np


def get_digits(text: str) -> int:
    """Get the sum of the first and last digit in text.

    :param text: input text
    :type text: str
    :return: stringsum of first and last digit (can be dame digit)
    :rtype: int
    """
    digits = list(filter(str.isdigit, text))
    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    with open("./day1/trebuchet/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    arr = np.array(inp.splitlines())
    total = np.sum(list(map(get_digits, arr)))
    print(total)
