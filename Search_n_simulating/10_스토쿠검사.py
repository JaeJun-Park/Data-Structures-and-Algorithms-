import copy
import sys

sys.stdin = open("10_.txt", "rt")


def check(sudoku):
    for i in range(9):
        ch_r = [0]*10
        ch_c = [0]*10
        for j in range(9):
            ch_r[sudoku[i][j]] = 1
            ch_r[sudoku[i][j]] = 1
        if sum(ch_r) != 9 or sum(ch_c) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch_b = [0]*10
            for k in range(3):
                for s in range(3):
                    ch_b[sudoku[3*i+k][3*j+s]] = 1
            if sum(ch_b) != 9:
                return False
    return True


sudoku = [list(map(int, input().split())) for _ in range(9)]

if check(sudoku):
    print('YES')
else:
    print('NO')
