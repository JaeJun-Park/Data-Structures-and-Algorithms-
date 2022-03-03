'''
문자와 숫자가 섞여있는  문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만든다.
만들어진 자연수와 그 자연수의 약수 개수를 출력한다.
만약 "t0e0a1c2h0er"에서 숫자만 추출하면 00120이고 이것을 자연수로 만들면 120이 된다.
'''

import sys

sys.stdin = open("2_.txt", "rt")

n = int(''.join(filter(lambda ch: ch.isdecimal(), input())))

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
print(n, cnt, sep='\n')

