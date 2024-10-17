def solution(n):
    partial_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        partial_sum[i] = partial_sum[i - 1] + i  # 정확한 누적 합 배열 생성

    left, right = 0, 1  # 시작 포인터 설정
    cnt = 0

    while right <= n:
        current_sum = partial_sum[right] - partial_sum[left]
        if current_sum == n:
            cnt += 1
            left += 1
        elif current_sum < n:
            right += 1
        else:
            left += 1

    return cnt
