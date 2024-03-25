# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.
from random import shuffle

def generate_deck(copies = 2, joker = True, shuff = True):
    deck = list('A23456789') + ['10'] + list('JQKA')

    deck_copy = []

    for _ in range(copies):
        for c in deck:
            deck_copy.append(c)
    
    if joker:
        deck_copy.extend(['JK1', 'JK2'])
    
    if shuff:
        shuffle(deck_copy)

    return deck_copy

def show_deck(deck):
    print(f'Number of cards in the deck: {len(deck)}')
    print('Cards: ')
    print(', '.join(deck))

def give_cards(deck, players = 1, amount = 4):
    card_player = {}
    

    for i in range(players):
        cards = []
        while len(cards) < amount and len(cards) < len(deck):
            card = deck.pop(0)
            cards.append(card)
        
        if len(cards) == 4:
            nome = f'player {i + 1}'
            card_player[nome] = cards

    return card_player

def show_players(card_player):
    for k, v in card_player.items():
        print(f'{k} => {len(v)} cards \n\t---> {v}\n')
    return



deck = generate_deck()
show_deck(deck)
print(give_cards(deck, 7))