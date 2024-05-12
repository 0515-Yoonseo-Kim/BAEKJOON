import sys
N, M = map(int,input().split())
input = sys.stdin.readline

keyword_dict = dict()
for _ in range(N):
    keyword_dict[input().rstrip()] = 1

for _ in range(M):
    li = list(input().rstrip().split(','))
    for l in li:
        keyword_dict.pop(l,None)
    print(len(keyword_dict))
