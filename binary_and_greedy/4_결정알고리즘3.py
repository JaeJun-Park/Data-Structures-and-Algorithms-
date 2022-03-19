'''
해결방법..
1 2 8 4 9
1          
0 1 7 3 8   거리 중 먼 곳을 선택     
1, 9 (8)        
0 1 7 3 8  1을 기준으로 한 기존 거리 리스트에서
8 7 1 5 0  9를 기준으로 한 거리 리스트
0 1 1 3 0  9가 추가됬으니 두말에서 가까운 정도를 나타낸 거리값 업데이트
1, 4 , 9 (3)  그중에서 거리 그나마 먼 3의 값이 담근 '4'번 좌표 선택
'''

'''
초기화 방법
{
    x1: x1,
    x2: x2,
    ...
    xN: xN
}

갱신 방법
{
    x1: x1-xX,
    x2: x2-xX,
    ...
    xN: xN-xX
}
'''

import copy
import sys
sys.stdin = open("4.txt", "rt")

# <------------ input -------------->
n, c = map(int, input().split())
coord = [int(input()) for _ in range(n)]

print(coord)
# <----------- main logic ------------->

dist = [float('inf')]*n
for i in range(c):
    stallcrd = coord[dist.index(max(dist))] # 빈 마굿간들중 말이 있는 마굿간에서 제일 멀리떨어진 곳 선택
    dist = [abs(coord[i]-stallcrd) if dist[i] > 
            abs(coord[i]-stallcrd) else dist[i] for i in range(n)] # 말이 있는 마굿간들 기준으로 얼마나 떨어져 있는지 거리 갱신

stallcrds = [coord[i] for i in range(n) if dist[i] == 0]
print(stallcrds)

howfar = [abs(stallcrds[i]-stallcrds[i+1]) for i in range(c-1)]
print(howfar)

print(min(howfar))
