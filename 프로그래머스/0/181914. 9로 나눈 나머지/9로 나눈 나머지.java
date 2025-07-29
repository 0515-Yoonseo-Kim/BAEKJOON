class Solution {
    public int solution(String number) {
        int total = 0;
        for (char ch : number.toCharArray()) {
            total += ch - '0';
        }
        return total % 9;
    }
}
