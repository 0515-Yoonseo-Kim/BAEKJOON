import java.util.*;
class Solution {
    public String solution(String[] seoul) {
        // seoul 배열에서 문자열 "Kim"을 찾으면 정답 String에 대입해서 반환.
        int idx = Arrays.asList(seoul).indexOf("Kim");
        
        String answer = String.format("김서방은 %d에 있다",idx);
        return answer;
    }
}