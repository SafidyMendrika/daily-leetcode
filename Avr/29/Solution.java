class Solution {
    public long countSubarrays(int[] nums, int k) {
        int maxElement = Integer.MIN_VALUE;
        for (int num : nums) {
            maxElement = Math.max(maxElement, num);
        }
        
        int n = nums.length;
        long result = 0;
        int count = 0;
        for (int start = 0; start < n; start++) {
            count = 0;  
            
            for (int end = start; end < n; end++) {
                if (nums[end] == maxElement) {
                    count++;
                }
                
                if (count >= k) {
                    result++;
                }
            }
        }
        
        return result;
    }
}