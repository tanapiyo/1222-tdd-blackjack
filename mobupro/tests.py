import pytest

import blackjack.game
import blackjack.dealer
import blackjack.player

@pytest.fixture
def game_state():
    return {
        "dealer_cards": [],
        "player_state": False,
        "player_cards": []
    }

@pytest.mark.parametrize('cards, expect', [
    (['5', '6'], 11),
    (['2'], 2),
    (['J', '2', '3'], 15),
    (['A'], 11),
    (['10', '10', 'A'], 21),
    (['A', '10', '10'], 21),
    (['A', 'A'], 12),
    (['10', '10', '10'], 30),
])

def test_calc(cards, expect):
    assert blackjack.game.calc(cards) == expect


def test_distribute_cards(game_state):
    assert len(blackjack.dealer.distribute_cards_to_player(game_state)['player_cards']) == 2

@pytest.mark.parametrize('cards, new_num_of_cards', [
    (['5', '6'], 3),
    (['A', '2', '3'], 4)
])
def test_hit(cards, new_num_of_cards, game_state):
    game_state['player_cards'] = cards
    assert len(blackjack.player.hit(game_state)['player_cards']) == new_num_of_cards


def test_is_player_lost():
    assert blackjack.game.is_player_lost(['10', '10', '2'])


def test_is_not_player_lost():
    assert not blackjack.game.is_player_lost(['10', '10', 'A'])


def test_dealer_distribute_cards(game_state):
    assert blackjack.dealer.distribute_cards_to_dealer(game_state)['dealer_cards'] == [blackjack.game.Card(character='2', visible=True), (blackjack.game.Card(character='A', visible=False))]


# def test_stand():
#    assert blackjack.player.stand(game_state) == [blackjack.game.Card(character='2', visible=True), (blackjack.game.Card(character='A', visible=True))]

