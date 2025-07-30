import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        Stack<Character> stk = new Stack<>();
        for(int i =0; i<s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '(') stk.push(ch);
            if (ch == ')'){
                if (stk.isEmpty()) return false;
                else stk.pop();
            }
        }
        if (!stk.isEmpty()) return false;
        return answer;
    }
}