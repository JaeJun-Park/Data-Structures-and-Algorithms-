import sys


def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True


sys.stdin = open('11_.txt', "rt")

mtx = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7):
    for j in range(3):

        for k in range(5//2):
            if mtx[j+k][i] != mtx[j+5-k-1][i]:
                break
        else:
            cnt += 1

        for k in range(5//2):
            if mtx[i][j+k] != mtx[i][j+5-k-1]:
                break
        else:
            cnt += 1

        # col = []
        # row = []
        # # for k in range(5):
        #     col.append(mtx[j+k][i])
        #     row.append(mtx[i][j+k])
        # if (check(col)):  # col == col[::-1]
        #     cnt += 1
        # if (check(row)):
        #     cnt += 1
print(cnt)
