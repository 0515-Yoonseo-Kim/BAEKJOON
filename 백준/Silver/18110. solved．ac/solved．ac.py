import sys
input = sys.stdin.readline

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
scores = [int(input()) for _ in range(N)]

if N == 0:
    print(0)
else:
    limit = roundUp(N * 0.15)
    scores = sorted(scores)[limit:N-limit]
    average = roundUp(sum(scores) / len(scores))
    print(average)
