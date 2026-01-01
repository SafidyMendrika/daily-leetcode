class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        long result = 0;
        int leftBound = -1;  
        int lastMinKPos = -1;  
        int lastMaxKPos = -1;  
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < minK || nums[i] > maxK) {
                leftBound = i;
                lastMinKPos = -1;
                lastMaxKPos = -1;
            } else {
                if (nums[i] == minK) {
                    lastMinKPos = i;
                }
                if (nums[i] == maxK) {
                    lastMaxKPos = i;
                }
                
                if (lastMinKPos != -1 && lastMaxKPos != -1) {
                    int validLeftEndpoint = Math.min(lastMinKPos, lastMaxKPos) - leftBound;
                    result += validLeftEndpoint > 0 ? validLeftEndpoint : 1;
                }
            }
        }
        
        return result;
    }
}