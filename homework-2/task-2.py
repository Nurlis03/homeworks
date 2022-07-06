import random
import time
from more_itertools import locate

board = [' '] * 100
# board = list(range(100))
HUMAN = ''
COMPUTER = ''

# Показывает игровую доску
def show_board():
    print("=" * 45, end='')
    print("      ", end='')
    print("=" * 55)
    temp = 10
    count = 0
    for i in range(len(board)):
        if i == temp - 10:
            print("||", end=" ")
        print(f"[{board[i]}]", end=' ')
        if i + 1 == temp:
            print("||", end=' ')
            temp += 10
            print("     ", end='')
            print('||', end=' ')
            if i == 9:
                for k in range(10):
                    print(f" [{count}]", end=' ')
                    count += 1
            else:
                for k in range(10):
                    print(f"[{count}]", end=' ')
                    count += 1
            print("||", end='')
            print()
    print("=" * 45, end='')
    print("     ", end=' ')
    print("=" * 55)


# Рандомно выбираем первого игрока
def who_starts_game():
    first_play = random.choice([HUMAN, COMPUTER])
    if first_play == HUMAN:
        print(f'Starts the game you.')
        return 'human'
    else:
        print(f'Starts the game computer.')
        return 'computer'


# по горизонтали всевозможных выигрышей получается 60. Хранится все варианты в списке all_winnings
def win_horizontally(all_winnings):
    i = 5
    j = 0
    while i < 99:
        temp = j
        while j < temp + 6:
            all_winnings.append(board[j:i])
            j += 1
            i += 1
        i += 4
        j = 0
        j += i - 5


def win_vertically(all_winnings):
    start = 0
    end = 50
    cycle = 0
    temp1 = 0
    while cycle < 60:
        i = 0
        while i < 6:
            all_winnings.append(board[start:end:10])
            start += 11
            end += 11
            i += 1
            cycle += 1
        temp1 += 1
        start = temp1
        end = temp1 + 50

def win_first_diagonal(all_winnings):
    start = 0
    end = 55
    cycle = 0
    j = 6
    temp1 = 1
    while cycle < 21:
        for i in range(j):
            all_winnings.append(board[start:end:11])
            start += 11
            end += 11
            cycle += 1
        start = temp1
        end = 55 + temp1
        temp1 += 1
        j -= 1

    start = 10
    end = 65
    cycle = 0
    j = 5
    temp1 = 10
    while cycle < 15:
        for i in range(j):
            all_winnings.append(board[start:end:11])
            start += 11
            end += 11
            cycle += 1
        start = temp1 + 10
        end = 65 + temp1
        temp1 += 10
        j -= 1

def win_second_diagonal(all_winnings):
    start = 9
    end = 54
    cycle = 0
    j = 6
    temp1 = 1
    while cycle < 21:
        for i in range(j):
            all_winnings.append(board[start:end:9])
            start += 9
            end += 9
            cycle += 1
        start = 9 - temp1
        end = 54 - temp1
        temp1 += 1
        j -= 1

    start = 19
    end = 64
    cycle = 0
    j = 5
    temp1 = 10
    while cycle < 15:
        for i in range(j):
            all_winnings.append(board[start:end:9])
            start += 9
            end += 9
            cycle += 1
        start = temp1 + 19
        end = 64 + temp1 + 1
        temp1 += 10
        j -= 1


def check_win() -> bool:
    all_winnings = []
    win_horizontally(all_winnings)
    win_vertically(all_winnings)
    win_first_diagonal(all_winnings)
    win_second_diagonal(all_winnings)
    for i in range(len(all_winnings)):
        if HUMAN == all_winnings[i][0] == all_winnings[i][1] == all_winnings[i][2] == all_winnings[i][3] == all_winnings[i][4]:
            print("Game over!\nYou won!")
            return True
        elif COMPUTER == all_winnings[i][0] == all_winnings[i][1] == all_winnings[i][2] == all_winnings[i][3] == all_winnings[i][4]:
            print("Game over!\nComputer won!")
            return True
    return False



def input_position(position: int) -> int:
    while 0 > position or position > 99:
        position = int(input('Enter position: '))
        if 0 > position or position > 99:
            print("Invalid input! \nEnter a position between (0-99)")
    return position



# Возвращает true, если поле не заполнена иначе false, если заполнена
def check_free_field(player: str, value: int) -> bool:
    if player == 'human':
        if board[value] == 'X' or board[value] == 'O':
            print('This field is filled. Please enter another field!')
            return False
    else:
        if board[value] == 'X' or board[value] == 'O':
            return False
    return True


def check_field(position):
    if board[position] == ' ':
        return True
    return False


def play_game(player):
    if player == 'human':
        position = input_position(-1)
        while not check_free_field(player, position):
            position = input_position(-1)
        board[position] = HUMAN
    else:
        print("Computer move...")
        time.sleep(2)
        position = -1
        Human_moves = list(locate(board, lambda x: x == HUMAN))
        if Human_moves:
            for i in range(len(Human_moves)):
                if Human_moves[i] + 1 == 1 or Human_moves[i] + 10 == 10 or Human_moves[i] + 11 == 11:
                    if check_field(Human_moves[i] + 1):
                        board[Human_moves[i] + 1] = COMPUTER
                        return
                    elif check_field(Human_moves[i] + 10):
                        board[Human_moves[i] + 10] = COMPUTER
                        return
                    elif check_field(Human_moves[i] - 1):
                        board[Human_moves[i] + 11] = COMPUTER
                        return

            for i in range(len(Human_moves)):
                if Human_moves[i] - 1 == 8 or Human_moves[i] + 10 == 19 or Human_moves[i] + 9 == 18:
                    if check_field(Human_moves[i] + 9):
                        board[Human_moves[i] + 9] = COMPUTER
                        return
                    elif check_field(Human_moves[i] + 10):
                        board[Human_moves[i] + 10] = COMPUTER
                        return
                    elif check_field(Human_moves[i] - 1):
                        board[Human_moves[i] - 1] = COMPUTER
                        return
            for i in range(len(Human_moves)):
                if Human_moves[i] - 10 == 80 or Human_moves[i] + 1 == 91 or Human_moves[i] + 11 == 81:
                    if check_field(i + 11):
                        board[Human_moves[i] + 11] = COMPUTER
                        return
                    elif check_field(Human_moves[i] - 10):
                        board[Human_moves[i] - 10] = COMPUTER
                        return
                    elif check_field(Human_moves[i] + 1):
                        board[Human_moves[i] + 1] = COMPUTER
                        return

            for i in range(len(Human_moves)):
                if Human_moves[i] - 10 == 89 or Human_moves[i] - 1 == 98 or Human_moves[i] - 11 == 88:
                    if check_field(Human_moves[i] - 10):
                        board[Human_moves[i] - 10] = COMPUTER
                        return
                    elif check_field(Human_moves[i] - 1):
                        board[Human_moves[i] - 1] = COMPUTER
                        return
                    elif check_field(Human_moves[i] - 11):
                        board[Human_moves[i] - 11] = COMPUTER
                        return

        while not check_free_field(player, position):
            position = random.randint(0, 99)
        board[position] = COMPUTER


def main():
    show_board()
    check_win()
    global HUMAN
    global COMPUTER
    print('What will you choose: X or O')

    while HUMAN != 'O' and HUMAN != 'X':
        HUMAN = input().upper()
        if HUMAN != "O" and HUMAN != "X":
            print("Invalid input! \nPlease input X or O!!!")
    if HUMAN != 'O':
        COMPUTER = 'O'
    else:
        COMPUTER = 'X'

    player = who_starts_game()
    while not check_win():
        show_board()
        play_game(player)
        if player == 'human':
            player = 'computer'
        else:
            player = 'human'

if __name__ == "__main__":
    main()