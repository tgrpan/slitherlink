import numpy as np
import random

while True:
    input_str = input("size(int) : ")
    try:
        n = int(input_str)
        if n > 3:
            break
    except ValueError:
        pass
    print("input error")

board = np.zeros([n*n],dtype=int)

start = (n+1)*(n//2)

tree = [start]
board[start] = 1

#board_print = board.reshape([n,n])
#print(board_print)

def up_check(point, n, board):
    if point >= n:
        if board[point-n] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def left_check(point, n, board):
    if point % n > 0:
        if board[point-1] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def right_check(point, n, board):
    if point % n < n-1:
        if board[point+1] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def down_check(point, n, board):
    if point < n*(n-1):
        if board[point+n] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

while len(tree)<n*(n//3):
    point = tree[random.randrange(len(tree))]
    #print("point:",point)
    direction = random.randrange(4)
    #print("direction:",direction)
    flag = False
    if direction == 0:
        status = up_check(point, n, board)
        if status == 0:
            next_point = point - n
            status_up = up_check(next_point, n, board)
            status_left = left_check(next_point, n, board)
            status_right = right_check(next_point, n, board)
            if status_up == status_left == status_right == 0:
                up_two_point = point - 2*n
                status_up_left = left_check(up_two_point, n, board)
                status_up_right = right_check(up_two_point, n, board)
                if status_up_left == status_up_right == 0:
                    flag = True
    elif direction == 1:
        status = left_check(point, n, board)
        if status == 0:
            next_point = point - 1
            status_left = left_check(next_point, n, board)
            status_up = up_check(next_point, n, board)
            status_down = down_check(next_point, n, board)
            if status_left == status_up == status_down == 0:
                left_two_point = point - 2
                status_up_left = up_check(left_two_point, n, board)
                status_down_left = down_check(left_two_point, n, board)
                if status_up_left == status_down_left == 0:
                    flag = True
    elif direction == 2:
        status = right_check(point, n, board)
        if status == 0:
            next_point = point + 1
            status_right = right_check(next_point, n, board)
            status_up = up_check(next_point, n, board)
            status_down = down_check(next_point, n, board)
            if status_right == status_up == status_down == 0:
                right_two_point = point + 2
                status_up_right = up_check(right_two_point, n, board)
                status_down_right = down_check(right_two_point, n, board)
                if status_up_right == status_down_right == 0:
                    flag = True
    elif direction == 3:
        status = down_check(point, n, board)
        if status == 0:
            next_point = point + n
            status_down = down_check(next_point, n, board)
            status_left = left_check(next_point, n, board)
            status_right = right_check(next_point, n, board)
            if status_down == status_left == status_right == 0:
                down_two_point = point + 2*n
                status_down_left = left_check(down_two_point, n, board)
                status_down_right = right_check(down_two_point, n, board)
                if status_down_left == status_down_right == 0:
                    flag = True
    #print("next_point",next_point)
    if flag:
        tree.append(next_point)
        board[next_point] = 1
    #board_print = board.reshape([n,n])
    #print(board_print)

board_print = board.reshape([n,n])
print(board_print)

#print("------------")

puzzle = np.zeros([n**2],dtype=int)
for i in range(n**2):
    status_up = up_check(i, n, board)
    status_left = left_check(i, n, board)
    status_right = right_check(i, n, board)
    status_down = down_check(i, n, board)
    count = sum([max(status_up, 0), max(status_left, 0), max(status_right, 0), max(status_down, 0)])
    if board[i] == 1:
        count = 4 - count
    puzzle[i] = count

puzzle_print = puzzle.reshape([n,n])
#print(puzzle_print)

print("------------")
print("puzzle")

puzzle_board = []
for i in range(n):
    line = "+ " * n + "+"
    puzzle_board.append(line)
    line = ""
    for j in range(n):
        line += " " + str(puzzle[i*n+j])
    puzzle_board.append(line)
line = "+ " * n + "+"
puzzle_board.append(line)

for line in puzzle_board:
    print(line)


print("------------")
print("answer")

#board_sizeup = np.concatenate([board_print, np.zeros([1,n],dtype=int)], axis=0)
#board_sizeup = np.concatenate([board_sizeup, np.zeros([n+1,1],dtype=int)], axis=1)
#board_sizeup = board_sizeup.reshape([(n+1)**2])
#print(board_sizeup)

answer_board = []
for i in range(n):
    line_1 = ""
    for j in range(n):
        line_1 += "+"
        status_up = up_check((n*i+j), n, board)
        if board[i*n+j] == 0:
            if not status_up == 1:
                line_1 += " "
            else:
                line_1 += "-"
        else:
            if status_up == 1:
                line_1 += " "
            else:
                line_1 += "-"
    line_1 += "+"
    answer_board.append(line_1)
    line_2 = ""
    for j in range(n):
        status_left = left_check((n*i+j), n, board)
        if board[i*n+j] == 0:
            if not status_left == 1:
                line_2 += " "
            else:
                line_2 += "|"
        else:
            if status_left == 1:
                line_2 += " "
            else:
                line_2 += "|"
        line_2 += str(puzzle[n*i+j])
    status_right = right_check((n*(i+1)-1), n, board)
    if board[i] == 0:
        if not status_right == 1:
            line_2 += " "
        else:
            line_2 += "|"
    else:
        if status_right == 1:
            line_2 += " "
        else:
            line_2 += "|"
    answer_board.append(line_2)
line_1 = ""
for j in range(n):
    line_1 += "+"
    status_down = down_check((n*(n-1)+j), n, board)
    if board[i] == 0:
        if not status_down == 1:
            line_1 += " "
        else:
            line_1 += "-"
    else:
        if status_down == 1:
            line_1 += " "
        else:
            line_1 += "-"
line_1 += "+"
answer_board.append(line_1)

for line in answer_board:
    print(line)
