from typing import List, NamedTuple

from typing_extensions import TypedDict
'''
課題1の分
'''

Card = NamedTuple('Card', [('character', str), ('visible', bool)])
GameState = TypedDict('GameState', {'dealer_cards': List[Card], 'player_standed': bool, 'player_cards': List[Card]})

game_state: GameState = {
    "dealer_cards": [],
    "player_stand": False,
    "player_cards": []
}
# player = {
#     "player_state": False,
#     "player_cards": []
# }


def __to_number(accumurator: int, card: str) -> int:
    if card == 'A':
        if accumurator <= 10:
            return 11
        else:
            return 1
    elif card in {'J', 'Q', 'K'}:
        return 10
    return int(card)


def calc(cards: List[str]) -> int:
#def calc(game_state: GameState) -> int:
    def f(accumurator: int, cards: List[str]) -> int:
        if not cards:
            return accumurator
        head, *tail = cards
        return f(accumurator + __to_number(accumurator, head), tail)

    return f(0, sorted(cards, key=lambda card: card == 'A'))

#def is_player_lost(cards: List[str]) -> bool:
def is_player_lost(player_cards: List[Card]) -> bool:
    """プレイヤーがブタならTrueを返します。それ以外はFalseを返します。
    """
    return calc(player_cards) > 21
