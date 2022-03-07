'''
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저 있다. N의 크기는 항상 홀수이다. 가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사 과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
'''
import sys

sys.stdin = open("7_.txt", "rt")

n = int(input())
farm = [list(map(int, input().split())) for _ in range(n)]

num_of_apple = 0

# for i in range(n):
#     if i <= n//2:
#         num_of_apple += sum(farm[i][n//2-i:n//2+i+1])
#     else:  # 3 4   n//2 is 2
#         num_of_apple += sum(farm[i][i-n//2: n//2-i])

s, e = n//2, n//2+1

for i in range(n):
    num_of_apple += sum(farm[i][s:e])
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(num_of_apple)
