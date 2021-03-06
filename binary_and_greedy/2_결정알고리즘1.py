import sys

sys.stdin = open("2.txt", "rt")


def Count(lst, mid):
    cnt = 0
    for e in lst:
        cnt += e // mid
    return cnt


k, n = map(int, input().split())
line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(line, mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
