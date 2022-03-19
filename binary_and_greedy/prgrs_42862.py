def solution(n, lost, reserve):
    answer = 0
    students = [1]*(n+2)

    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1

    #1 1 2 3 4 5 1
    #1 2 0 2 0 2 1

    for i in range(1, n+1):
        if students[i] == 0 and students[i-1] == 2:
            students[i] += 1
            students[i-1] -= 1
        elif students[i] == 0 and students[i+1] == 2:
            students[i] += 1
            students[i+1] -= 1

    answer = sum([1 for st in students[1:n+1] if st > 0])

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))

'''
2 1 0 1 1
1 1 1 1 1
'''
