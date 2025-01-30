# 1부터 생성자를 만들면서 loop를 돎
# 만약, loop를 돌면서 생성자가 만들어지지 않았으면 그 때 self number에 추가함.
num = 10000
dp = [False]*(num+1)
self_number_list = []
def get_self_number(num):
    while num <=10000:
        dp[num]=True
        num += sum([int(n) for n in str(num)])
    return
for i in range(1,num+1):
    if dp[i]:
        continue
    self_number_list.append(i)
    get_self_number(i)

print(*self_number_list,sep="\n")