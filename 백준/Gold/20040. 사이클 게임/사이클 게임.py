import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
parents = [i for i in range(N)]  # 각 노드의 부모 노드를 저장하는 리스트

def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x > parent_y:
        parents[parent_x] = parent_y
    else:
        parents[parent_y] = parent_x

for i in range(M):
    A, B = map(int, input().split())
    if find_parent(A) == find_parent(B):
        cnt = i + 1  # 1부터 시작하기 때문에 1을 더해줌
        break
    union(A, B)

print(cnt)
