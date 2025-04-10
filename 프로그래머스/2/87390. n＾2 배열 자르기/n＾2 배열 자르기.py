def solution(n, left, right):
    answer = []
    for idx in range(left,right+1):
        r,c = idx//n, idx%n
        answer.append(max(r,c)+1)
    return answer