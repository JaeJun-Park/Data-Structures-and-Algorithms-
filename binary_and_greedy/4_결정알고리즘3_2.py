import sys


def Count(coords, diff):
    cnt = 1
    stall = coords[0]
    for i in range(1, n):
        distDiff = coords[i] - stall
        if distDiff >= diff:  # mid는 추정 가장가까운 두말의 최대 거리
            stall = coords[i]
            cnt += 1
    return cnt


sys.stdin = open("4.txt", "rt")

n, c = map(int, input().split())
coords = [int(input()) for _ in range(n)]
coords.sort()

lt, rt = 1, coords[-1]

res = 0
while lt <= rt:  # 찾고자하는 값인 res를 이분탐색, 이분탐색의 인풋을 if 조건으로 활용하자
    mid = (lt+rt)//2

    cnt = Count(coords, mid)

    if cnt < c:  # 가장 가까운 말의 최대거리가 그 모양이면 말이 다 못들어가는데요?
        rt = mid-1
    elif cnt >= c:  # 가장 가까운 말의 최대거리가 Mid일떄 말이 제대로 들어가거나 오히려 더 많이 들어감
        lt = mid+1
        res = mid  # 최적이 되는 res를 계속 찾아나가자
print(res)
