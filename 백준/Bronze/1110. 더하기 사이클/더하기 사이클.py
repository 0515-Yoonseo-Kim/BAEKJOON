num = int(input())
cnt = 0
ans = num
while True:
    cnt += 1
    n1,n2 = num//10,num%10
    new = n1 + n2
    num = n2*10 + new%10
    if num == ans:
        break
print(cnt)
