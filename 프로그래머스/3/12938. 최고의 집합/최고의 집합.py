def solution(n, s):
    if s < n:
        return [-1]
    div,mod = s//n, s%n
    answer = [div]*n
    for i in range(1,mod+1):
        answer[-i]+= 1
    return answer