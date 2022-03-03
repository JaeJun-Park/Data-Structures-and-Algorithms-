import sys

'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우 (회문 문자열)이면
YES를 출력하고, 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성
단, 회문을 검사할 때 대소문자를 구분하지 않는다.
'''

def isPalindrome(word):
    for i in range(len(word)//2 - 1):
        if word[i] != word[-(1+i)]: # 거꾸로 인덱스 접근
            return False
    else:
        return True
    

sys.stdin = open("1_.txt", "rt")
n = int(input())

for i in range(1,n+1):
    word = input().upper()
    if isPalindrome(word): # word == word[::-1]
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")

