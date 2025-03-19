str1 = input()
str2 = input()
N,M = len(str1),len(str2)

lcs = [[0 for _ in range(M+1)] for _ in range(N+1)]
max_length = 0

for i in range(N):
    for j in range(M):
        if str1[i] == str2[j]:
            lcs[i+1][j+1] = lcs[i][j] + 1
        else:
            lcs[i+1][j+1] = max(lcs[i][j+1],lcs[i+1][j])
    max_length = max(max_length,max(lcs[i+1]))
print(max_length)