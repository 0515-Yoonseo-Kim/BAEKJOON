from collections import defaultdict
N, M = map(int,input().split())
mod_dict = defaultdict(int)
mod_dict[0] = 1

nums = list(map(lambda x: int(x) % M,input().split()))

prefix_sum = 0
cnt = 0

for num in nums:
    prefix_sum += num
    remainder = prefix_sum % M
    cnt += mod_dict[remainder]
    mod_dict[remainder] += 1
print(cnt)