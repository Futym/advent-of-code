from functools import cmp_to_key
cards = {"T": "B", "J": "C", "Q": "D", "K": "E", "A": "F"}


def get_hand_type(hand):
    hand_cards = {}
    for ch in hand:
        if ch in hand_cards:
            hand_cards[ch] += 1
        else:
            hand_cards[ch] = 1

    if len(hand_cards) == 1:
        return 7

    if len(hand_cards) == 2:
        if 4 in hand_cards.values():
            return 6
        return 5

    if len(hand_cards) == 3:
        if 3 in hand_cards.values():
            return 4
        return 3

    if len(hand_cards) == 4:
        return 2
    return 1


def compare_hands(hand1, hand2):
    hand1_cards = hand1[0]
    hand2_cards = hand2[0]

    if get_hand_type(hand1_cards) != get_hand_type(hand2_cards):
        return get_hand_type(hand1_cards) - get_hand_type(hand2_cards)
    for ch in hand1_cards:
        hand1_cards = hand1_cards.replace(ch, cards.get(ch, ch))
    for ch in hand2_cards:
        hand2_cards = hand2_cards.replace(ch, cards.get(ch, ch))
    return 1 if hand1_cards > hand2_cards else -1


def calculate_result(filename):
    with open(filename, "r") as file:
        hands = [(x.strip().split()[0], int(x.strip().split()[1])) for x in file.readlines()]
        sorted_hands = sorted(list(hands), key=cmp_to_key(compare_hands))
        return sum([i * bid for i, (_, bid) in enumerate(sorted_hands, 1)])


if __name__ == "__main__":
    result = calculate_result("input.txt")
    print(result)
