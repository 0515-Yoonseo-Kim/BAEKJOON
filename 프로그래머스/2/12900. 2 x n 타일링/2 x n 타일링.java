import java.util.*;
class Solution {
    public int solution(int n) {
        
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        int arr[] = new int[n+1];
        Arrays.fill(arr,0);
        arr[1] = 1;
        arr[2] = 2;
        
        
        for(int i =3; i<arr.length;i++){
            arr[i] = (arr[i-1]+arr[i-2])% 1_000_000_007;
        }
        return arr[n];
    }
}