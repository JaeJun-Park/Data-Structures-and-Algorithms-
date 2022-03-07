import sys

sys.stdin = open("9_.txt", "rt")

n = int(input())

mapp = list()
for i in range(n+2):
    if i == 0 or i == n+1:
        mapp.append([0]*(n+2))
    else:
        mapp.append([0]+list(map(int, input().split()))+[0])

cnt = 0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         altitude = mapp[i][j]
#         if altitude > max(mapp[i-1][j], mapp[i][j+1], mapp[i+1][j], mapp[i][j-1]):
#             cnt += 1
#             j += 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(mapp[i][j] > mapp[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
