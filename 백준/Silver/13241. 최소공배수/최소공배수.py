import sys
input = sys.stdin.readline


def gcd(a,b):
    # 유클리우드 호제법
    while b!=0:
        a,b = b, a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)

A, B = map(int,input().split())
print(lcm(A,B))
