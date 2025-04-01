from termcolor import colored

table = list(range(1, 10))
winner = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


def print_table():
    j = 1
    for i in table:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "O":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "X":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def can_move(tbl, mve):
    if mve in range(1, 10) and isinstance(tbl[mve-1], int):
        return True
    return False


def make_move(tbl, plyr, mve, undo=False):
    if can_move(tbl, mve):
        tbl[mve-1] = plyr
        win = is_winner(tbl, plyr)
        if undo:
            tbl[mve-1] = mve
        return True, win
    return False, False


def is_winner(tbl, plyr):
    win = True
    for tup in winner:
        win = True
        for j in tup:
            if tbl[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def empty_space():
    return table.count("X") + table.count("O") != 9


def pc_mve():
    mv = -1
    for i in range(1, 10):
        if make_move(table, computer, i, True)[1]:
            mv = i
            break
    if mv == -1:
        for j in range(1, 10):
            if make_move(table, player, j, True)[1]:
                mv = j
                break
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(table, m):
                    mv = m
                    break
    return make_move(table, computer, mv)


player, computer = "X", "O"
print("pc is:", computer, "\nplayer is:", player, "\n")
while empty_space():
    print_table()
    move = int(input("Enter your move(1-9): "))
    moved, won = make_move(table, player, move)
    if not moved:
        print("wrong input, try again")
        continue
    if won:
        print(colored("Congratulations, You did it!", "green"))
    elif pc_mve()[1]:
        print(colored("game over", "yellow"))
        break

print_table()
