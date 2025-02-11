import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    # 2의 거듭제곱 중 n보다 크거나 같은 최소값을 찾기
    power = 1
    cnt = 0
    while power < n:
        power *= 2
        cnt += 1
    print(cnt + 1)  # 첫 1마리를 데려오는 연산 포함