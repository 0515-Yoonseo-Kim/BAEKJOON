class Solution {
    private int getDivisorSum(int n){
        int sum = 0;
        double maxNum = Math.sqrt(n);
        for(int i =1; i<=n;i++){
            if (n%i==0){
                sum += i;
            }
        }
        return sum;
    }
    public int solution(int n) {
        return getDivisorSum(n);
    }
}