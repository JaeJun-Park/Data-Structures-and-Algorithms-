'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하시오
'''
import sys

sys.stdin = open("./4_.txt", "rt")
n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))


sys.stdin = open("4_.txt", "rt")
n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

lst = []
i, j = 0, 0
for _ in range(n+m):
    if lst1[i] <= lst2[j]:
        lst.append(lst1[i])
        i += 1
        if i >= n:
            lst = lst + lst2[j:]
            break
    else:
        lst.append(lst2[j])
        j += 1
        if j >= m:
            lst = lst + lst1[i:]
            break
print(lst)
