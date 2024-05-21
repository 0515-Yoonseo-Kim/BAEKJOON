import sys
input = sys.stdin.readline


word_dict = {}

N = int(input())
for _ in range(N):
    now = input().rstrip()
    word_dict[now] = 0

word_cnt_list = sorted([[idx,word] for idx, word in enumerate(word_dict)],key = lambda x: x[1])

max_cnt = 0
for idx, word in enumerate(word_cnt_list):
    if idx == N-1:
        break
    now, compare = word_cnt_list[idx][1], word_cnt_list[idx+1][1]

    max_len = min(len(now),len(compare))
    for i in range(max_len):

        if now[i] == compare[i]:
            if i == max_len-1:

                word_dict[now] = max(word_dict[now],max_len)
                word_dict[compare] = max_len
                max_cnt=max(max_cnt,max_len)
            continue
        else:
            word_dict[now] = max(word_dict[now],i)
            word_dict[compare] = i
            max_cnt=max(max_cnt,i)
            break

chk = 0
st,ed = str(),str()
for k,v in word_dict.items():
    if v == max_cnt:
        if chk == 0:
            st=k
            chk = 1
        elif st[:max_cnt]==k[:max_cnt]:
            ed = k
            break
print(st)
print(ed)