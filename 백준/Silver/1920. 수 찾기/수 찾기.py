N = int(input())

nums = list(map(int,input().split()))
num_dict = {k:1 for k in nums}
M =  int(input())
question = list(map(int,input().split()))

for q in question:
    print(num_dict.get(q,0))