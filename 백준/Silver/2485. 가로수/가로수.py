import sys
input = sys.stdin.readline


def gcd(a,b):
    # 유클리우드 호제법
    while b!=0:
        a,b = b, a%b
    return a


N = int(input())
first = int(input())
diff = []
for i in range(N-1):
    num = int(input())
    diff.append(num-first)
    first = num

gcd_now = diff[0]

for i in range(N-1):

    gcd_now = gcd(gcd_now,diff[i])


cnt = 0
for d in diff:
    cnt+=(d//gcd_now-1)

print(cnt)