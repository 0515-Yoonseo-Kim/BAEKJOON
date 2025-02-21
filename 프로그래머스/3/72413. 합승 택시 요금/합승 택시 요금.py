# 시작 지점 : s 로 동일함.
# 도착 지점 : a, b로 각각 주어짐.
# 간선 마다 요금이 다름.
# 최저 예상 택시 요금을 구하자.
# 택시 중간까지 동승 가능함. -> 동승 시 요금 절약 가능
# 조건을 보니 플로이드-워셜로 가능할 듯.

def solution(n, s, a, b, fares):
    INF = int(1e9)
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for fare in fares:
        s1, s2, f = fare
        s1,s2 = s1-1, s2-1
        dist[s1][s2] = f
        dist[s2][s1] = f
        
    for k in range(n):
        for j in range(n):
            for i in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    s, a, b = s - 1, a - 1, b - 1
    min_fare = INF
    for k in range(n):
        min_fare = min(min_fare, dist[s][k] + dist[k][a] + dist[k][b])
    return min_fare