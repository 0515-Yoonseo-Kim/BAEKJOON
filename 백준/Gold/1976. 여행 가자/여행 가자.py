N = int(input())
M = int(input())

parents = [i for i in range(N)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        parents[py] = px

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N):
        if arr[j]:
            union(i,j)


plan = [num-1 for num in list(map(int,input().split()))]

if len(set(map(find,plan))) == 1:
    print("YES")
else:
    print("NO")