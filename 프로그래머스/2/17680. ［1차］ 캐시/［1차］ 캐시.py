from collections import deque
def solution(cacheSize, cities):
    queue = deque()
    answer = 0
    for city in cities:
        city=city.upper()
        if city in queue:
            answer+=1
            queue.remove(city)
            queue.append(city)
        else:
            answer+=5
            queue.append(city)
            if len(queue)>cacheSize:
                queue.popleft()
    return answer