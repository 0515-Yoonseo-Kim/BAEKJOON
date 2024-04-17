import sys
input = sys.stdin.readline

N,K = map(int,input().split())
table = [i for i in input().rstrip()]
cnt = 0
for i in range(N):
    if table[i] == 'P':
        start = max(i-K,0)
        end = min(i+K+1,N)
        for j in range(start,end):
            if table[j] == 'H':
                table[j] = '0'
                cnt+=1
                break

print(cnt)
