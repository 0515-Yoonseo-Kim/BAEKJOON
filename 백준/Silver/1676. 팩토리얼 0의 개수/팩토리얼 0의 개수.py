N = int(input())

def count(num):
    num_five=0

    while num%5 == 0:
        num_five +=1
        num //=5
    return num_five
dp = []
for i in range(1,N+1):
    dp.append(count(i))
print(sum(dp))