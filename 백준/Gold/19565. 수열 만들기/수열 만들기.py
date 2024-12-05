import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    
    # 수열의 길이 출력
    print(n * n + 1)
    
    if n == 2:
        # 특수 경우 처리
        print("1 1 2 2 1")
        return
    
    visited = [[False] * n for _ in range(n)]  # 방문 여부 배열
    
    # 첫 번째 1 출력
    print(1, end=' ')
    
    # 첫 번째 패턴 구성
    for i in range(n, 0, -1):
        print((i % n) + 1, i, end=' ')
        visited[i - 1][i - 1] = True
        visited[(i % n)][i - 1] = True
    
    # 두 번째 패턴 구성
    for i in range(n):
        j = (i + 2) % n  # 초기값 설정
        while j != i:
            if visited[i][j]:
                j = (j + 1) % n
                continue
            diff = (j - i + n) % n
            p = j
            visited[i][j] = True
            while True:
                nxt = (p + diff) % n
                print(p + 1, end=' ')
                if visited[p][nxt]:
                    break
                visited[p][nxt] = True
                p = nxt
            j = (j + 1) % n  # 증감 조건
        
        # 마지막에 다시 돌아오는 부분
        print((i + 1) % n + 1, end=' ')

if __name__ == "__main__":
    main()
