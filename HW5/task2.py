# игра крестики-нолики


COLORS = {
    'red': '\033[31m',
    'green': '\033[32m',
    'reset': '\033[0m'
}

field = [
    '', '', '',
    '', '', '',
    '', '', '',
]

def print_field():
    print(f' {colour(field[0]) or 1} | {colour(field[1]) or 2} | {colour(field[2]) or 3} ')
    print('---+---+---')
    print(f' {colour(field[3]) or 4} | {colour(field[4]) or 5} | {colour(field[5]) or 6} ')
    print('---+---+---')
    print(f' {colour(field[6]) or 7} | {colour(field[7]) or 8} | {colour(field[8]) or 9} ')

def turn(player):
    cell_number = input('Enter cell number: ')
    while (
        not cell_number.isdigit() or
        int(cell_number) < 1 or
        int(cell_number) > 9 or
        field[int(cell_number) - 1] != ''
    ):
        cell_number = input('Enter cell number: ')
    i = int(cell_number) - 1
    field[i] = player


def is_over():
    if field[0] == field[1] == field[2] != '':
        return field[0]
    if field[3] == field[4] == field[5] != '':
        return field[3]
    if field[6] == field[7] == field[8] != '':
        return field[6]
    if field[0] == field[3] == field[6] != '':
        return field[0]
    if field[1] == field[4] == field[7] != '':
        return field[1]
    if field[2] == field[5] == field[8] != '':
        return field[2]
    if field[0] == field[4] == field[8] != '':
        return field[0]
    if field[2] == field[4] == field[6] != '':
        return field[2]

    for cell in field:
        if cell == '':
            return ''

    return 'XO'

def colour(character):
    if character == 'X':
        return f'{COLORS["red"]}X{COLORS["reset"]}'
    elif character == 'O':
        return f'{COLORS["green"]}O{COLORS["reset"]}'
    else:
        return character

player1 = input(f'Select a shape ({colour("X")} or {colour("O")}): ').upper()

while player1 != 'X' and player1 != 'O':
    print('Try again')
    player1 = input('Select a shape (X or O): ').upper()

player2 = 'O' if player1 == 'X' else 'X'

current_player = player1

while True:
    print_field()
    turn(current_player)
    winner = is_over()
    if winner:
        break
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

print_field()
if winner == 'XO':
    print('Nobody!')
    print(f'{colour("X")}{colour("O")}-' * 4, end='')
    print(f'{colour("X")}{colour("O")}')
else:
    print(f'{colour(winner)} wins!')
