import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int c = 0; c < commands.length; c++) {
            int i = commands[c][0];
            int j = commands[c][1];
            int k = commands[c][2];

            // 수동 슬라이싱
            int[] sub = new int[j - i + 1];
            for (int idx = i - 1; idx < j; idx++) {
                sub[idx - (i - 1)] = array[idx];
            }

            Arrays.sort(sub);               // 정렬
            answer[c] = sub[k - 1];         // k번째 값 추출
        }
        return answer;
    }
}