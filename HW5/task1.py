# Игра с конфетами
import random


COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'reset': '\033[0m'
}

def man_turn():
    while True:
        man = int(input('your turn: '))
        if man > 28 or man <= 0 or man > candy:
            print(f'enter number from 1 to {min(28, candy)}')
        else: 
            return man

def stupid_bot_turn():
    bot = random.randint(1, 28)
    if bot > candy:
        bot = candy
    print(f'bot turn: {bot}')
    return bot

def clever_bot_turn():
    bot = candy % 29
    if bot == 0:
        bot = random.randint(1, 28)
    print(f'bot turn: {bot}')
    return bot



print('1. Stupid bot')
print('2. Clever bot')
opponent = 0
while opponent < 1 or opponent > 2:
    opponent = int(input('choose an opponent: '))


bot_turn = stupid_bot_turn if opponent == 1 else clever_bot_turn

candy = 120

while candy > 0:
    candy -= man_turn()
    print(f'{candy} candy reminds')
    if candy == 0:
        print(f'{COLORS["green"]}man wins{COLORS["reset"]}')
        break
    candy -= bot_turn()
    print(f'{candy} candy reminds')
    if candy == 0:
        print(f'{COLORS["red"]}bot wins{COLORS["reset"]}')
        break

