
N = int(input())

buildings = []
for n in range(N):
    L,H = map(int, input().split())
    buildings.append([L,H])
 
buildings.sort()

max_idx = 0
max_height = 0
for i in range(N):
    if buildings[i][1] > max_height:
        max_height = buildings[i][1]
        max_idx = i



area = max_height
l, h = buildings[0]
for i in range(max_idx + 1): 
    if buildings[i][1] >= h:
        height = h
        width = buildings[i][0] - l
        area += width * height
        l, h= buildings[i]
    else:
        pass

l, h = buildings[-1]
for i in range(N - 1, max_idx - 1, -1):
    if buildings[i][1] >= h:  
        height = h
        width = l - buildings[i][0]
        area += width * height
        l,h = buildings[i]
    else:
        pass

print(area)