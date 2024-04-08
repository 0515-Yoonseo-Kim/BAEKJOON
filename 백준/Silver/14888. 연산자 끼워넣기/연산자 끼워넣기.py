N = int(input())
num_list = list(map(int,input().split()))
op = list(map(int,input().split()))

# pruning
maximum = -int(1e9)
minimum = int(1e9)
def pruning(depth, result, plus, minus, multiply, divide):
    global maximum,minimum
    if depth == N:
        maximum = max(maximum,result)
        minimum = min(minimum,result)
        return
    if plus:
        pruning(depth+1,result+num_list[depth],plus-1,minus,multiply,divide)
    if minus:
        pruning(depth+1,result-num_list[depth],plus,minus-1,multiply,divide)
    if multiply:
        pruning(depth+1,result*num_list[depth],plus,minus,multiply-1,divide)
    if divide:
        pruning(depth+1,int(result/num_list[depth]),plus,minus,multiply,divide-1)
    
pruning(1,num_list[0],op[0],op[1],op[2],op[3])

print(maximum)
print(minimum)