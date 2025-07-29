import java.util.*;
class Solution {
    public long solution(long n) {
        
        // 1. n을 String으로 바꾸기 -> 문자 배열로 분해
        String[] digits = String.valueOf(n).split("");
        // 2. digits를 내림차순으로 정렬하기 
        Arrays.sort(digits,Collections.reverseOrder());
        // 3. 정렬된 문자열을 다시 숫자로 변환.
        StringBuilder sb = new StringBuilder();
        for(String d: digits){
            sb.append(d);
        }
        
        return Long.parseLong(sb.toString());
    }
}