N = int(input())
triangle = []
total = [[0]*i for i in range(1,N+1)]
for _ in range(N):
    arr = list(map(int,input().split()))
    triangle.append(arr)

total = [[0] * (i + 1) for i in range(N)]
total[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            total[i][j] = total[i - 1][j] + triangle[i][j]
        elif j == i:
            total[i][j] = total[i - 1][j - 1] + triangle[i][j]
        else:
            total[i][j] = max(total[i - 1][j - 1], total[i - 1][j]) + triangle[i][j]
print(max(total[-1]))