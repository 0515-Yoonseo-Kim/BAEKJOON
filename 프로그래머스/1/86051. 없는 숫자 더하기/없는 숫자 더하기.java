class Solution {
    public int solution(int[] numbers) {
        int maxVal = 45;
        for(int n :numbers){
            maxVal -= n;
        }
        return maxVal;
    }
}