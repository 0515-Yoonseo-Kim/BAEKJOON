import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        // 1. 시작 시간 기준 정렬
        Arrays.sort(book_time, (a, b) -> a[0].compareTo(b[0]));

        // 2. 종료 시간을 저장할 우선순위 큐 (오름차순)
        PriorityQueue<Integer> roomQueue = new PriorityQueue<>();

        for (String[] time : book_time) {
            int start = toMinutes(time[0]);
            int end = toMinutes(time[1]) + 10; // 청소 시간 포함

            // 3. 사용할 수 있는 방이 있는지 확인
            if (!roomQueue.isEmpty() && roomQueue.peek() <= start) {
                roomQueue.poll(); // 가장 먼저 끝난 방 재사용
            }

            roomQueue.offer(end); // 현재 예약의 종료 시간 저장
        }

        return roomQueue.size(); // 동시에 필요한 최대 객실 수
    }

    // "HH:MM" → 분(int) 변환
    private int toMinutes(String time) {
        String[] parts = time.split(":");
        int hour = Integer.parseInt(parts[0]);
        int min = Integer.parseInt(parts[1]);
        return hour * 60 + min;
    }
}
