import sys


def isItOkayToHave(meetings, numOfMeetings):
    for first in range(0, len(meetings)-numOfMeetings+1):
        cnt = 1
        prev = meetings[first][1]
        next = prev
        while next <= meetings[-1][0]:
            if meetings[next][0] >= meetings[prev][1]:
                prev = next
                cnt += 1
            next += 1
        if cnt >= numOfMeetings:
            return True
    return False


sys.stdin = open("binary_and_greedy/5.txt", "rt")

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda meeting: meeting[1])
print(meetings)

maxNumOfMeetings = 0
lt = 1
rt = n

while lt <= rt:
    numOfMeetings = (lt+rt)//2

    if isItOkayToHave(meetings, numOfMeetings):  # 위 numOfMeetings이 가능하냐? 안하냐
        maxNumOfMeetings = numOfMeetings
        lt = numOfMeetings + 1
    else:
        rt = numOfMeetings - 1

print(maxNumOfMeetings)
