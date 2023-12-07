import functools
from collections import OrderedDict, defaultdict

inp = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


@functools.total_ordering
class Card:
    val_rank_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __init__(self, val: str):
        self.val = val
        self.strength = __class__.val_rank_dict[val]

    def _is_valid_operand(self, other: object) -> bool:
        return hasattr(other, "strength")

    def __eq__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.strength == other.strength

    def __lt__(self, other: object) -> bool:
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.strength < other.strength


class Hand:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards
        self.strength = self._get_strength()

    def _get_strength(self) -> list[int]:
        values = [c.strength for c in self.cards]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        v_descending = OrderedDict(
            sorted(value_counts.items(), key=lambda v: v[1], reverse=True)
        )
        hand_vals = list(v_descending.values())
        hand_str_list = list(v_descending.keys())
        if len(set(hand_str_list)) == 1:
            return [7, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 2:
            if hand_vals == [4, 1]:
                return [6, *[c.strength for c in self.cards]]
            if hand_vals == [3, 2]:
                return [5, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 3:
            if hand_vals == [3, 1, 1]:
                return [4, *[c.strength for c in self.cards]]
            if hand_vals == [2, 2, 1]:
                return [3, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 4:
            return [2, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 5:
            return [1, *[c.strength for c in self.cards]]
        raise ValueError()


if __name__ == "__main__":
    with open("./day7/camel_cards/input.txt", "r", encoding="utf-8") as f:
        inp = f.read()
    player_bets = []
    for line in inp.splitlines():
        cards, bet = line.split(" ")
        card_list = [Card(card) for card in cards]
        hand = Hand(card_list)
        player_bets.append((int(bet), hand.strength))
    player_bets = sorted(player_bets, key=lambda x: tuple(x[1]))
    total = sum(((i + 1) * pb[0] for i, pb in enumerate(player_bets)))
    print(total)
