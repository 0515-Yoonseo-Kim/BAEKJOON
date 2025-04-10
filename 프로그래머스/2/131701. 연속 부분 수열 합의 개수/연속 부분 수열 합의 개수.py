# 원형 수열의 부분 수열 합 구하기
# 중복 허용 x -> set() 사용하기
def solution(elements):
    partial_sum_set = set()
    N = len(elements)
    double_elements = elements*2
    for i in range(1,N+1):
        for idx in range(N):
            curr_sum = sum(double_elements[idx:idx+i])
            partial_sum_set.add(curr_sum)
    return len(partial_sum_set)