import sys
input = sys.stdin.readline
N = int(input())
steps = [int(input()) for _ in range(N)]
scores = [0 for _ in range(N)]

if N <= 2:
    print(sum(steps))
    sys.exit()

scores[0] = steps[0]
scores[1] = steps[0] + steps[1]
scores[2] = max(steps[1]+steps[2], scores[0]+steps[2])

for i in range(3,N):
    scores[i] = max(scores[i-3] + steps[i-1] + steps[i], scores[i-2] + steps[i])
    pass
print(scores[-1])