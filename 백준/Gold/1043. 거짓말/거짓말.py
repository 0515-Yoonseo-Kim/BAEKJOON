import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())

_,*truth_list = list(map(int,input().split()))

parents = [i for i in range(N+1)]
max_party_num = 0
KNOWN_GRP = 0

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(a,b):
    a = find_parents(a)
    b = find_parents(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in truth_list:
    union(KNOWN_GRP, i)

parties = []
for _ in range(M):
    num_ppl,*party = list(map(int,input().split()))
    parties.append(party)

    for i in range(num_ppl - 1):
        union(party[i],party[i+1])

for party in parties:
    if find_parents(party[0]) == KNOWN_GRP:
        continue
    
    max_party_num += 1

print(max_party_num)
    
    