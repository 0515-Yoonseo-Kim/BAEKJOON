from collections import defaultdict
T = int(input())

for _ in range(T):
    N = int(input())
    schools = defaultdict(int)
    for _ in range(N):
        name, number = input().split()
        schools[name] += int(number)
    max_school,max_num="",0
    for k,v in schools.items():
        if max_num < v:
            max_school=k
            max_num=v
    print(max_school)
