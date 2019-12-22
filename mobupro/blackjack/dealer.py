from .game import Card, GameState
from typing import List
import copy
'''
課題3の分と課題2の一部
'''
def distribute_cards_to_player(game_state: GameState) -> GameState:
    new_game_state: Final = copy.deepcopy(game_state)
    new_game_state['player_cards'] = [
       Card(character='2', visible=True),
        Card(character='3', visible=True)
    ]
    return new_game_state


def distribute_cards_to_dealer(game_state: GameState) -> GameState:
    new_game_state: Final = copy.deepcopy(game_state)
    new_game_state['dealer_cards'] = [
        Card(character='2', visible=True), 
        Card(character='A', visible=False)
    ]
    return new_game_state