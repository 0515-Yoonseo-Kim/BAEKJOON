N = int(input())
ppl = [list(map(int,input().split())) for _ in range(N)]
ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if ppl[i][0] < ppl[j][0] and ppl[i][1] < ppl[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)