import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        # data 초기 배열
        self.n = len(data)
        self.tree = [0]*(4 * self.n)
        self.build(0,0,self.n-1,data)

    def build(self,node,start,end,data):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start+end)//2
            l_node = 2 * node + 1
            r_node = 2 * node + 2
            self.build(l_node,start,mid,data)
            self.build(r_node,mid+1,end,data)
            self.tree[node] = self.tree[l_node] + self.tree[r_node]

    def update(self,idx,value,node,start,end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            l_node = 2*node + 1
            r_node = 2*node + 2
            if idx <= mid:
                self.update(idx,value,l_node,start,mid)
            else:
                self.update(idx,value,r_node,mid+1,end)
            self.tree[node] = self.tree[l_node] + self.tree[r_node]
        
    def query(self,left,right,node,start,end):
        if left > end or right < start:
            return 0
        
        if left <= start and right >= end:
            return self.tree[node]
        
        mid = (start+end)//2
        left_query = self.query(left,right,2*node+1,start,mid)
        right_query = self.query(left,right,2*node+2,mid+1,end)
        
        return left_query + right_query
    

N,M,K = map(int,input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))

seg_tree = SegmentTree(nums)

for _ in range(M+K):
    com,a,b = map(int,input().split())
    if com == 1:
        seg_tree.update(a-1,b,0,0,N-1)
    else:
        partial_sum = seg_tree.query(a-1, b-1, 0, 0, N - 1)
        print(partial_sum)
