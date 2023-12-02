import re
from dataclasses import dataclass

# inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


@dataclass
class Cubes:
    """Dataclass for the number of cubes and number of colored cubes."""

    allowed_red: int
    allowed_green: int
    allowed_blue: int
    red: int = 0
    green: int = 0
    blue: int = 0
    power: int = 0

    def update_green(self, green: int) -> None:
        """Update the number of green cubes in play.

        :param green: new green cubes
        :type green: int
        """
        self.green = max(self.green, green)

    def update_blue(self, blue: int) -> None:
        """Update the number of blue cubes in play.

        :param green: new blue cubes
        :type green: int
        """
        self.blue = max(self.blue, blue)

    def update_red(self, red: int) -> None:
        """Update the number of red cubes in play.

        :param green: new red cubes
        :type green: int
        """
        self.red = max(self.red, red)

    def reset(self) -> None:
        """Reset the dataclass."""
        self.red = 0
        self.blue = 0
        self.green = 0

    def valid_game(self) -> bool:
        """Determine if the game is possible.

        :return: Is a possible game.
        :rtype: bool
        """
        return (
            self.green <= self.allowed_green
            and self.blue <= self.allowed_blue
            and self.red <= self.allowed_red
        )

    def calc_power(self) -> int:
        """Calculate the power of the given game.

        :return: power of the game
        :rtype: int
        """
        self.power = self.green * self.red * self.blue
        return self.power


def flatten(list_in: list) -> list:
    """Flatten a list.

    :param list_in: list to flatten
    :type list_in: list
    :return: flattened list
    :rtype: list
    """
    return [item for sublist in list_in for item in sublist]


if __name__ == "__main__":
    game = Cubes(12, 13, 14)
    games_power = []
    with open("./day2/cube_conundrum/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    for line in inp.splitlines():
        game.reset()
        game_str, cube_str = [s.strip() for s in line.split(":")]
        game_nr = re.findall(r"\d+", game_str)
        turns = flatten([s.split(",") for s in cube_str.split(";")])
        for turn in turns:
            color = re.findall(r"[^\d\W]+", turn)
            res = re.search(r"\d+", turn)
            if res is not None:
                num = int(res.group())
            else:
                break
            if color[0] == "green":
                game.update_green(num)
            elif color[0] == "red":
                game.update_red(num)
            elif color[0] == "blue":
                game.update_blue(num)

        games_power.append(game.calc_power())

    total = sum(games_power)
    print(total)
