from typing import (
  List,
)
from typing_extensions import Final
from .game import GameState
import copy

def hit(game_state: GameState) -> GameState:
    new_game_state: Final = copy.deepcopy(game_state)
    new_game_state['player_cards'] += ['3']
    return new_game_state
