from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)-1]
    N = len(set(gems))
    gem_counter = defaultdict(int)
    left = 0
    min_dist = len(gems)

    for right in range(len(gems)):
        gem_counter[gems[right]] += 1

        while len(gem_counter) == N:
            if right - left < min_dist:
                min_dist = right - left
                answer = [left, right]

            gem_counter[gems[left]] -= 1
            if gem_counter[gems[left]] == 0:
                del gem_counter[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]
