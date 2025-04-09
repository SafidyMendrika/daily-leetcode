import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minOperations(int[] nums, int k) {
        for (int num : nums) {
            if (num < k) return -1;
        }

        Set<Integer> unique = new HashSet<>();
        for (int num : nums) {
            if (num > k) {
                unique.add(num);
            }
        }

        return unique.size();
    }
}