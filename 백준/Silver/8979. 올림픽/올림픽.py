import sys
from collections import defaultdict

input = sys.stdin.readline
medals = defaultdict(list)

N, K = map(int,input().split())
pos = []
for _ in range(N):
    num, g,s,b = map(int,input().split())
    medals[g,s,b].append(num)

    if num == K:
        temp = (g,s,b)
medal_arr = sorted(medals.keys(),key = lambda x: (-x[0],-x[1],-x[2]))
record = 1

for i in range(len(medal_arr)):
    if medal_arr[i] == temp:
        break
    record += len(medals[medal_arr[i]])

print(record)