from games.models import GameResult


def game_calculation(number_of_players, characters, cards, number_of_squares=None, number_of_cards=None):
    winner = None
    rounds = None
    split_cards = cards.split(',')

    for turn, card in enumerate(split_cards):
        if len(card) == 1:
            place = characters.find(card)
        else:
            place = characters.find(card[1], characters.find(card[0]) + 1)
        rounds = turn + 1
        if place == -1:
            winner = (turn - (turn // number_of_players) * number_of_players) + 1
            break
        characters = characters[0:place] + '_' + characters[place + 1:]
    if winner is None:
        GameResult.objects.create(result=f'No​ player​ won​ after​ {rounds} cards.')
    else:
        GameResult.objects.create(result=f'Player​ {winner} won​ after​ {rounds} cards.')
    return winner, rounds
