import java.util.Arrays;

class Solution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        
        return countPairsLessThanOrEqual(nums, upper) - countPairsLessThanOrEqual(nums, lower - 1);
    }
    
    private long countPairsLessThanOrEqual(int[] nums, int val) {
        long count = 0;
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            if (nums[left] + nums[right] <= val) {
                count += right - left;
                left++;
            } else {
                right--;
            }
        }
        
        return count;
    }
}