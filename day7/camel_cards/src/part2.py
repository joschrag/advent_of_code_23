import functools
from collections import Counter, OrderedDict, defaultdict

inp = """2345A 2
Q2Q2Q 13
2345J 5
J345A 3
32T3K 7
T55J5 19
KK677 11
KTJJT 29
QQQJA 23
JJJJJ 31
JAAAA 43
AAAAJ 53
AAAAA 59
2AAAA 17
2JJJJ 47
JJJJ2 34"""


@functools.total_ordering
class Card:
    val_rank_dict = {
        "1": 2,
        "2": 3,
        "3": 4,
        "4": 5,
        "5": 6,
        "6": 7,
        "7": 8,
        "8": 9,
        "9": 10,
        "T": 11,
        "J": 1,
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
        self.num_joker = sum((c.strength == 1 for c in self.cards))
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
                if self.num_joker in [1, 4]:
                    return [7, *[c.strength for c in self.cards]]
                return [6, *[c.strength for c in self.cards]]
            if hand_vals == [3, 2]:
                if self.num_joker in [2, 3]:
                    return [7, *[c.strength for c in self.cards]]
                return [5, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 3:
            if hand_vals == [3, 1, 1]:
                if self.num_joker in [1, 3]:
                    return [6, *[c.strength for c in self.cards]]
                return [4, *[c.strength for c in self.cards]]
            if hand_vals == [2, 2, 1]:
                if self.num_joker == 1:
                    return [5, *[c.strength for c in self.cards]]
                if self.num_joker == 2:
                    return [6, *[c.strength for c in self.cards]]
                return [3, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 4:
            if self.num_joker in [1, 2]:
                return [4, *[c.strength for c in self.cards]]
            return [2, *[c.strength for c in self.cards]]
        if len(set(hand_str_list)) == 5:
            if self.num_joker == 1:
                return [2, *[c.strength for c in self.cards]]
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
        player_bets.append((int(bet), hand.strength, cards))
    player_bets = sorted(player_bets, key=lambda x: tuple(x[1]))
    # print("\n".join([str(c) for c in player_bets]))
    total = sum(((i + 1) * pb[0] for i, pb in enumerate(player_bets)))
    print(total)
