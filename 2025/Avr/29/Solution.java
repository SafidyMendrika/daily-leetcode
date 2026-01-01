class Solution {
    public long countSubarrays(int[] nums, int k) {
        int maxElement = Integer.MIN_VALUE;
        for (int num : nums) {
            maxElement = Math.max(maxElement, num);
        }
        
        int n = nums.length;
        long result = 0;
        int maxCount = 0;
        int left = 0;
        int right = 0;
        
        while (right < n) {
            if (nums[right] == maxElement) {
                maxCount++;
            }
            
            while (maxCount >= k) {
                result += n - right;
                
                if (nums[left] == maxElement) {
                    maxCount--;
                }
                left++;
            }
            
            right++;
        }
        
        return result;
    }
}