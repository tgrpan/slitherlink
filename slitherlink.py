import numpy as np
import random

n = 7

board = np.zeros([n**2],dtype=int)

start = (n+1)*(n//2)

tree = [start]
board[start] = 1

board_print = board.reshape([n,n])
print(board_print)

def up_check(point):
    if point >= n:
        if board[point-n] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def left_check(point):
    if point % n > 0:
        if board[point-1] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def right_check(point):
    if point % n < n-1:
        if board[point+1] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

def down_check(point):
    if point < n*(n-1):
        if board[point+n] == 0:
            status = 0
        else:
            status = 1
    else:
        status = -1
    return(status)

while len(tree)<n*2:
    point = tree[random.randrange(len(tree))]
    print("point:",point)
    direction = random.randrange(4)
    print("direction:",direction)
    flag = False
    if direction == 0:
        status = up_check(point)
        if status == 0:
            next_point = point - n
            status_up = up_check(next_point)
            status_left = left_check(next_point)
            status_right = right_check(next_point)
            if status_up == status_left == status_right == 0:
                up_two_point = point - 2*n
                status_up_left = left_check(up_two_point)
                status_up_right = right_check(up_two_point)
                if status_up_left == status_up_right == 0:
                    flag = True
    elif direction == 1:
        status = left_check(point)
        if status == 0:
            next_point = point - 1
            status_left = left_check(next_point)
            status_up = up_check(next_point)
            status_down = down_check(next_point)
            if status_left == status_up == status_down == 0:
                left_two_point = point - 2
                status_up_left = up_check(left_two_point)
                status_down_left = down_check(left_two_point)
                if status_up_left == status_down_left == 0:
                    flag = True
    elif direction == 2:
        status = right_check(point)
        if status == 0:
            next_point = point + 1
            status_right = right_check(next_point)
            status_up = up_check(next_point)
            status_down = down_check(next_point)
            if status_right == status_up == status_down == 0:
                right_two_point = point + 2
                status_up_right = up_check(right_two_point)
                status_down_right = down_check(right_two_point)
                if status_up_right == status_down_right == 0:
                    flag = True
    elif direction == 3:
        status = down_check(point)
        if status == 0:
            next_point = point + n
            status_down = down_check(next_point)
            status_left = left_check(next_point)
            status_right = right_check(next_point)
            if status_down == status_left == status_right == 0:
                down_two_point = point + 2*n
                status_down_left = left_check(down_two_point)
                status_down_right = right_check(down_two_point)
                if status_down_left == status_down_right == 0:
                    flag = True
    print("next_point",next_point)
    if flag:
        tree.append(next_point)
        board[next_point] = 1
    board_print = board.reshape([n,n])
    print(board_print)

print("------------")

puzzle = np.zeros([n**2],dtype=int)
for i in range(n**2):
    status_up = up_check(i)
    status_left = left_check(i)
    status_right = right_check(i)
    status_down = down_check(i)
    count = sum([max(status_up, 0), max(status_left, 0), max(status_right, 0), max(status_down, 0)])
    if board[i] == 1:
        count = 4 - count
    puzzle[i] = count

puzzle_print = puzzle.reshape([n,n])
print("puzzle")
print(puzzle_print)




