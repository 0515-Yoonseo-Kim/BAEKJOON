import sys
input = sys.stdin.readline

#word_dict : key값 = word , value = 겹치는 접두사의 최대 길이
word_dict = {}

# 입력받고 value를 0으로 초기화
N = int(input())
for _ in range(N):
    now = input().rstrip()
    word_dict[now] = 0

# word_cnt_list : dictionary에 입력된 순서를 idx로 저장 ( 나중에 생각하니 굳이? ), sorted로 사전 순서대로 배열한다.
#-> **사전순서대로 배열해서 인접한 string끼리만 비교해서 시간복잡도를 크게 줄일 수 있다.**
word_cnt_list = sorted([word for word in word_dict])

# max_cnt : 겹치는 접두사의 길이의 최댓값. 나중에 dictionary를 순회하면서 value가 max_cnt인 item만 비교할 예정
max_cnt = 0
for idx, word in enumerate(word_cnt_list):
	# IndexERROR를 피함
    if idx == N-1:
        break
    now, compare = word_cnt_list[idx], word_cnt_list[idx+1]
	#max_len : now,compare중 더 짧은 길이만큼만 순회
    max_len = min(len(now),len(compare))
    #for 루프를 돌면서 word_dict의 값 초기화
    for i in range(max_len):
		# 같은 경우 continue
        # 한 string이 다른 string에 포함되는 경우. i값으로 초기화가 되지 않는 문제가 존재해서 if문으로 초기화
        if now[i] == compare[i]:
            if i == max_len-1:
                word_dict[now] = max(word_dict[now],max_len)
                word_dict[compare] = max_len
                max_cnt=max(max_cnt,max_len)
            continue
        else:
        	#글자가 다른경우 word_dict에 초기화
            word_dict[now] = max(word_dict[now],i)
            word_dict[compare] = i
            max_cnt=max(max_cnt,i)
            break
            

# chk : st가 정해졌는지 확인용
chk = 0
S,T = str(),str()
# dictionary를 순회하면서 value가 max_cnt인 key찾기
# S가 정해졌으면 S의 접두사와 같은 접두사를 갖는 T찾기
for k,v in word_dict.items():
    if v == max_cnt:
        if chk == 0:
            S=k
            chk = 1
        elif S[:max_cnt]==k[:max_cnt]:
            T = k
            break
print(S)
print(T)