import java.util.PriorityQueue;

public class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        
        for (int num : nums) {
            pq.offer((long) num);
        }
        
        int operations = 0;
        long x = 0,y=0, newValue = 0;
        while (pq.size() >= 2 && pq.peek() < k) {
            x = pq.poll();
            y = pq.poll();
            
            newValue = Math.min(x, y) * 2 + Math.max(x, y);
            
            pq.offer(newValue);
            
            operations++;
        }
        
        if (pq.peek() < k) {
            return -1;
        }
        
        return operations;
    }
}
