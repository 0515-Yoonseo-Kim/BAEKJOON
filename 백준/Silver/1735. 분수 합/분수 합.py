import sys
input = sys.stdin.readline


def gcd(a,b):
    # 유클리우드 호제법
    while b!=0:
        a,b = b, a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)

A1, B1 = map(int,input().split())
A2, B2 = map(int,input().split())

denom = lcm(B1,B2)
numer = denom//B1*A1 + denom//B2*A2

common = gcd(denom,numer)
print(numer//common,denom//common)