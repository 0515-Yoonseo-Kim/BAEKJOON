import sys
input = sys.stdin.readline

X,N = map(int,input().split())
num_list = list(map(int,input().split()))

sum_num = sum(num_list[:N])
max_num = sum_num
cnt = 1
for i in range(N,X):
    sum_num -= num_list[i-N]
    sum_num += num_list[i]
    if max_num == sum_num:
        cnt+=1
    if sum_num>max_num:
        max_num = sum_num
        cnt=1

if max_num == 0:
    print("SAD")
else:
    print(max_num)
    print(cnt)