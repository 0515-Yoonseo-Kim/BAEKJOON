import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        // 1. for문으로 divisor나눠서 조건에 맞으면 List에 추가.
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i<arr.length;i++){
            if(arr[i]%divisor==0){
                list.add(arr[i]);
            }
        }
        if (list.size()==0){
            return new int[]{-1};
        }
        // 2. 오름차순 정렬
        Collections.sort(list);
        // 3. List를 int[]로 변환.
        int[] answer = new int[list.size()];
        for(int i = 0;i<answer.length;i++){
            answer[i]=list.get(i);
        }
        return answer;
    }
}