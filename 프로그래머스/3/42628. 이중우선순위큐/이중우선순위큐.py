import heapq

def select_operation(oper: str) -> int:
    if oper[0] == "I":
        return 1
    elif oper[-1] == "1" and oper[-2] == "-":
        return 2
    else:
        return 3

def solution(operations):
    min_heap = []
    
    for oper in operations:
        operation = select_operation(oper)
        
        if operation == 1:
            _, num = oper.split()
            heapq.heappush(min_heap, int(num))
        elif operation == 2:
            if min_heap:
                heapq.heappop(min_heap)
        elif operation == 3:
            if min_heap:
                min_heap.pop()  
        
    min_heap.sort()
    return [min_heap[-1] if min_heap else 0,min_heap[0] if min_heap else 0]

