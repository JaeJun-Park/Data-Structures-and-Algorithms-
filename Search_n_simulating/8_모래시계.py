from shutil import which
import sys


sys.stdin = open("8_.txt", "rt")

n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
# commands[][0]: row num(1~), [1]: 0 left 1 right, [2]: num of block

for _ in range(m):
    whichrow, direction, howmuch = map(int, input().split())
    # if direction:
    #     howmuch *= -1
    for _ in range(howmuch):
        if direction == 1:
            farm[whichrow-1].insert(0, farm[whichrow-1].pop())
        else:
            farm[whichrow-1].append(farm[whichrow-1].pop(0))
    # farm[whichrow-1] = farm[whichrow-1][howmuch:] + farm[whichrow-1][:howmuch]

cnt = 0

s, e = 0, n
for i in range(n):
    cnt += sum(farm[i][s:e])
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(cnt)
