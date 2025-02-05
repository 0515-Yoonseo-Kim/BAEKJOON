from collections import Counter

def solution(a):
    if not a:  # 빈 리스트일 경우 0 반환
        return 0

    counter = Counter(a)  # 각 숫자의 등장 횟수 계산
    max_length = 0  # 스타 수열의 최대 길이

    for target in counter:  # 모든 숫자를 target으로 시도
        if counter[target] * 2 <= max_length:  # 최대 길이를 넘을 가능성이 없으면 건너뛰기
            continue
        
        length = 0  # 현재 target으로 구성할 수 있는 스타 수열의 길이
        i = 0
        while i < len(a) - 1:
            if (a[i] == target or a[i+1] == target) and a[i] != a[i+1]:  # 조건을 만족하는 경우
                length += 2
                i += 1  # 다음 숫자로 넘어감
            i += 1

        max_length = max(max_length, length)  # 최댓값 갱신

    return max_length
