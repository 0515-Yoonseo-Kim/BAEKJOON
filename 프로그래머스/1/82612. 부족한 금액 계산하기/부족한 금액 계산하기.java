class Solution {
    public long solution(int price, int money, int count) {
        long fee = (long)price*(count*(count+1)/2);
        long shortage = fee-money;
        return Math.max(0,shortage);
    }
}