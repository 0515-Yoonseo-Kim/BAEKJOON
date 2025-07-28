class Solution {
    public boolean solution(int x) {
        int num = x;
        boolean answer = true;
        int total = 0;
        while(x > 0){
            total += x%10;
            x/=10;
        }
        
        return (int) num/total == (double) num/total;
    }
}