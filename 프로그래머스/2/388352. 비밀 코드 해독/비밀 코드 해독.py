from itertools import combinations
def solution(n, q, ans):
    answer = 0
    nums = [i for i in range(1,n+1)]
    for combo in combinations(nums,5):
        flag = True
        for li, a in zip(q,ans):
            if len(set(li)&set(combo))!=a:
                flag=False
                break
        if flag:
            answer += 1
    return answer