class Solution {
    public long solution(long n) {
        long answer = 0;
        double maxNum = Math.sqrt(n);
        while(answer<=maxNum){
            if(Math.pow(answer,2)==n){
                return (long) Math.pow(answer+1,2);
            }
            answer+=1;
        }
        return -1;
    }
}