def solution(people, limit):
    people.sort()
    left, right = 0, len(people)-1
    cnt = 0
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
        else:
            left += 1
            right -= 1
        cnt += 1
    return cnt