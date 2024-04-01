import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    candidates = []
    for _ in range(N):
        candidate = list(map(int,input().split()))
        if candidate[0] == 1:
            second_limit = candidate[1]
        if candidate[1] == 1:
            first_limit = candidate[0]
        candidates.append(candidate)
    cnt = 0
    candidates.sort(key = lambda x : x[0])
    for candidate in candidates:
        if candidate[0] <= first_limit or candidate[1] <= second_limit:
            if candidate[0] < first_limit and candidate[1] < second_limit:
                cnt-=1
            first_limit,second_limit = min(first_limit,candidate[0]),min(second_limit,candidate[1])
            cnt+=1
    print(cnt)
