from audioop import reverse
import sys
from unittest import makeSuite


def dvdorder(musics, dvd_size):
    num_dvd = 0

    lt = 0
    for rt in range(1, len(musics)):
        mins = sum(musics[lt:rt])
        if mins >= dvd_size:
            num_dvd += 1
            lt = rt

    if lt < rt:
        num_dvd += 1

    return num_dvd


# <-------------- input ----------------->
sys.stdin = open("binary_and_greedy/3.txt", "rt")

n, m = map(int, input().split())
musics = list(map(int, input().split()))
musics.sort(reverse=True)


# <------------ main logic --------------->
lt = max(musics)
rt = sum(musics)

while lt <= rt:
    dvd_size = (lt+rt)//2
    num_dvd = dvdorder(musics, dvd_size)
    if num_dvd > m:
        lt = dvd_size + 1
    elif num_dvd <= m:
        rt = dvd_size - 1


print(dvd_size)
