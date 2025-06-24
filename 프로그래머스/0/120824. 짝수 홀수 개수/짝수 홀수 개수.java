

class Solution {
    public int[] solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        for (int num: num_list){
            if (isEven(num)) even++;
            else odd++;
        }
        int[] answer = {};
        return new int[]{even,odd};
    }
    
    private boolean isEven(int num){
        return num%2==0;
    }
}