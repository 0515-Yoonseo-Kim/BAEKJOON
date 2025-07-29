import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int[] arr = new int[1000001];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(x);
        
        Arrays.fill(arr,-1);
        arr[x] = 0;
        
        while(!queue.isEmpty()){
            int now = queue.poll();
            
            for(int next: new int[]{now+n,now*2,now*3}){
                if(next < arr.length && arr[next] == -1){
                    arr[next] = arr[now]+1;
                    queue.offer(next);
                }
            }
        }
        
        return arr[y];
    }
}