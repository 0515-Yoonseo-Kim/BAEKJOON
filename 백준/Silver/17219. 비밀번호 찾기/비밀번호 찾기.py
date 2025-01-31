import sys
input = sys.stdin.readline
N, M = map(int,input().split())
site_password = dict()
for _ in range(N):
    k,v = input().split()
    site_password[k]=v

for _ in range(M):
    print(site_password[input().rstrip()])