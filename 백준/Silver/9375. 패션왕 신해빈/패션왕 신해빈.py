from collections import defaultdict
T = int(input())

for _ in range(T):
    N = int(input())
    clothes = defaultdict(list)

    for _ in range(N):
        v, k = input().split()
        clothes[k].append(v)
    cnt = 1
    for v in clothes.values():
        cnt *= (len(v)+1)
    print(cnt-1)