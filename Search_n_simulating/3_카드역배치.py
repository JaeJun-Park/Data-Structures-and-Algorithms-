'''
1~20까지 오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 주어진 구간ㄴ의 순서대로 위의 귳ㄱ에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치를 출력하는 프로그램을 작성해보자
'''

import sys
from xml.etree.ElementTree import tostring

sys.stdin = open("3_.txt", "rt")
cards = list(map(str,range(0,21)))

# def reverseList(lst):
#     tmp = list()
#     for item in lst:
#         tmp.insert(0,item) # 이거 비효율적인 방법임, 역배치시 스왑을 활용해야
#     return tmp

# for _ in range(10):
#     ai, bi = map(int, input().split())
#     cards = cards[:ai] + reverseList(cards[ai:bi+1]) + cards[bi+1:]

for _ in range(10):
    s, e = map(int, input().split())
    
    for i in range((e-s+1)//2):
        cards[s+i], cards[e-i] = cards[e-i], cards[s+i]

cards.pop(0)
print(' '.join(cards))