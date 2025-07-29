class Solution {
    public int[] solution(int n, int m) {
        int gcd = 1;
        int temp = 1;
        while(temp <=n && temp<=m){
            if(n%temp==0 && m%temp==0)
                gcd = temp;
            temp += 1;
        }
        int[] answer = {};
        return new int[]{gcd,n*m/gcd};
    }
}