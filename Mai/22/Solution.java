import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int maxRemoval(int[] nums, int[][] queries) {
      Arrays.sort(queries, Comparator.comparingInt(a -> a[0]));
        int n = nums.length;
        int m = queries.length;
        int[] delta = new int[n + 2];
        int ops = 0, r = 0;

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int l = 0; l < n; l++) {
            ops += delta[l];

            while (r < m && queries[r][0] == l) {
                maxHeap.add(queries[r][1]);
                r++;
            }

            while (ops < nums[l]) {
                if (maxHeap.isEmpty() || maxHeap.peek() < l) {
                    return -1;
                }
                int end = maxHeap.poll();
                delta[end + 1] -= 1;
                ops++;
            }
        }

        return maxHeap.size();
    }
}