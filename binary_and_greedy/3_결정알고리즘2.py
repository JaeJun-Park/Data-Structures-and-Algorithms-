from audioop import reverse
import sys
from unittest import makeSuite


def divideDvd(musics, dvd_size):
    num_dvd = 0

    # if lt < rt:
    #     num_dvd += 1
    lt, rt = 0, 1
    while rt <= len(musics):
        tot = sum(musics[lt:rt])
        if tot > dvd_size:
            num_dvd += 1
            lt = rt-1
        elif tot == dvd_size:
            num_dvd += 1
            lt = rt
            rt += 1
        else:
            rt += 1
    if lt < rt:
        num_dvd += 1

    return num_dvd


# <-------------- input ----------------->
sys.stdin = open("binary_and_greedy/3.txt", "rt")

n, m = map(int, input().split())
musics = list(map(int, input().split()))

# <------------ test ------------------------>


# <------------ main logic --------------->
lt = max(musics)
rt = sum(musics)

while lt < rt:
    dvd_size = (lt+rt)//2
    num_dvd = divideDvd(musics, dvd_size)
    if num_dvd > m:
        lt = dvd_size + 1
    elif num_dvd <= m:
        rt = dvd_size


print(dvd_size)
