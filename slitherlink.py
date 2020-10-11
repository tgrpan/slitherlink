import numpy as np
import random

n = 7

board = np.zeros([n**2],dtype=int)

start = (n+1)*(n//2)

tree = [start]
board[start] = 1

board_print = board.reshape([n,n])
print(board_print)

def up_check(n, point):
    if point >= n:
        if board[point-n] == 0:
            ans = 0
        else:
            ans = 1
    else:
        ans = -1
    return(ans)

def left_check(n, point):
    if point % n > 0:
        if board[point-1] == 0:
            ans = 0
        else:
            ans = 1
    else:
        ans = -1
    return(ans)

def right_check(n, point):
    if point % n > 0:
        if board[point-1] == 0:
            ans = 0
        else:
            ans = 1
    else:
        ans = -1
    return(ans)

def down_check(n, point):
    if point % n > 0:
        if board[point-1] == 0:
            ans = 0
        else:
            ans = 1
    else:
        ans = -1
    return(ans)

while len(tree)<n*(n/3):
    point = tree[random.randrange(len(tree))]
    print("point:",point)
    direction = random.randrange(4)
    print("direction:",direction)
    flag = False
    if direction == 0:
        if point >= n:
            if board[point-n] == 0:
                if point >= 2*n:
                    if board[point-2*n] == 1:
                        continue
                next_point = point-n
                flag = True
    elif direction == 1:
        if point % n > 0:
            if board[point-1] == 0:
                if point % n > 1:
                    if board[point-2] == 1:
                        continue
                next_point = point-1
                flag = True
    elif direction == 2:
        if point % n < n-1:
            if board[point+1] == 0:
                if point % n < n-2:
                    if board[point+2] == 1:
                        continue
                next_point = point+1
                flag = True
    elif direction == 3:
        if point < n*(n-1):
            if board[point+n] == 0:
                if point < n*(n-2):
                    if board[point+2*n] == 1:
                        continue
                next_point = point+n
                flag = True
    print("next_point",next_point)
    if flag:
        tree.append(next_point)
        board[next_point] = 1
    board_print = board.reshape([n,n])
    print(board_print)

