import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        if(arr.length==1){
            return new int[]{-1};
        }
        int min = Arrays.stream(arr).min().getAsInt();
        for (int a:arr){
            if (a!=min){
                answer.add(a);
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}