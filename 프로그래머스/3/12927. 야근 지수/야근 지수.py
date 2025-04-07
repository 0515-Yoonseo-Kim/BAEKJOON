import heapq

def solution(n, works):
    # 최대 힙을 만들기 위해 음수로 변환
    works = [-w for w in works]
    heapq.heapify(works)

    while n > 0:
        now = heapq.heappop(works)
        if now == 0:  # 실제 작업량 0이면 중단
            break
        heapq.heappush(works, now + 1)  # 작업량 감소 → 음수니까 +1
        n -= 1

    # 음수를 다시 양수로 바꾸고 제곱합 계산
    return sum((w ** 2 for w in works))
