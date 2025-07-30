import java.util.*;
class Solution {
    public String solution(String s) {
        String[] strArr = s.split(" ");           
        int[] nums = new int[strArr.length];      

        for (int i = 0; i < strArr.length; i++) {
            nums[i] = Integer.parseInt(strArr[i]); 
        }

        Arrays.sort(nums);
        int min = nums[0];
        int max = nums[nums.length - 1];

        return min + " " + max;
    }
}
