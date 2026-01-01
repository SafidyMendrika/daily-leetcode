class Solution {
    public int longestNiceSubarray(int[] nums) {
        int maxLength = 1; 
        int left = 0;       
        int runningOR = 0; 
        
        for (int right = 0; right < nums.length; right++) {
            while ((runningOR & nums[right]) != 0) {
                runningOR ^= nums[left];
                left++;
            }
            
            runningOR |= nums[right];
            
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}