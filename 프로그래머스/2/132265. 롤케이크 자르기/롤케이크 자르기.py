# 개수(길이)와 상관 없이 종류만 같으면 됨 -> set 자료구조 사용
# 슬라이싱하면서 비교하면 시간 복잡도가 O(N^2)로 시간 초과. -> 순서 고정이니 누적합 비교
def solution(toppings):
    N = len(toppings)
    topping_left = [0]*N
    topping_right = [0]*N
    topping_left_set = {toppings[0]}
    topping_right_set = {toppings[-1]}
    topping_left[0],topping_right[-1] = 1,1
    for idx in range(1,N):
        if toppings[idx] not in topping_left_set:
            topping_left[idx] = topping_left[idx-1] + 1
            topping_left_set.add(toppings[idx])
        else:
            topping_left[idx] = topping_left[idx-1]
        if toppings[-idx-1] not in topping_right_set:
            topping_right[-idx-1] = topping_right[-idx] + 1
            topping_right_set.add(toppings[-idx-1])
        else:
            topping_right[-idx-1] = topping_right[-idx]
    answer = 0
    for i in range(N - 1):
        if topping_left[i] == topping_right[i + 1]:
            answer += 1
    return answer
