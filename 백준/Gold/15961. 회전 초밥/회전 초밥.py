from collections import defaultdict
import sys
input = sys.stdin.readline

N,D,K,C = map(int,input().split())
sushi = [int(input()) for _ in range(N)]

curr_sushi = defaultdict(int)
for i in range(K):
    curr_sushi[sushi[i]] += 1
max_kind = len(curr_sushi)

if C not in curr_sushi:
    max_kind += 1

for i in range(N):
    left = sushi[i]
    right = sushi[(i+K)%N]

    curr_sushi[left] -= 1
    if curr_sushi[left] == 0:
        del curr_sushi[left]
    curr_sushi[right] += 1
    kind = len(curr_sushi)

    if C not in curr_sushi:
        kind += 1
    max_kind = max(max_kind, kind)

print(max_kind)