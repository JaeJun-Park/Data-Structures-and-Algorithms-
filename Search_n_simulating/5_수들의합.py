'''
n개의 수로 된 수열 a[1] a[2] ... a[n]이 있다. 이 수열의 i번째 수 부터 j 번째 수까지의 합 a[i]+a[i+1]+...+a[j-1]+a[j]가 m이 되는 경우의 수를 구하는 프로그램을 작성하시오. 

첫째 줄에 n, m이 주어진다. 다음 줄에는 a[1], a[2], ..., a[n]이 공백으로 분리되어 주어진다. 
'''

import sys

sys.stdin = open("5_.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(n, m)
print(arr)

# 내가 처음 짠 코드 (이게 더 정확한거 아닌가 싶다)
cnt = 0
for ln in range(1, m+1):
    # len(a[i:j+1])가 ln일떄 a[i]+...+a[j]가 m이 되게하는 경우의 수
    for i in range(n-ln+1):
        if sum(arr[i:i+ln]) == m:
            cnt += 1
print(cnt)

# 다른 풀이
cnt1 = 0
lt, rt = 0, 1
while rt <= n:
    tot = sum(arr[lt:rt])
    if tot < m:
        rt += 1
    elif tot == m:
        cnt1 += 1
        rt += 1
    else:
        lt += 1


print(cnt1)
