# -*- coding: utf-8 -*-
import sys

sys.stdin = open("6_.txt", "rt")

n = int(input())
# mtx = list()
# for _ in range(n):
#     mtx.append(list(map(int, input().split())))

mtx = [list(map(int, input().split())) for _ in range(n)]

tots = list()

for i in range(n):
    tots.append(sum(mtx[i]))

for i in range(n):
    tot = 0
    for j in range(n):
        tot += mtx[j][i]
    tots.append(tot)

tot = 0
for i in range(n):
    tot += mtx[i][i]
tots.append(tot)

tot = 0
for i in range(n):
    tot += mtx[i][n-i-1]
tots.append(tot)

print(tots)
print(max(tots))
