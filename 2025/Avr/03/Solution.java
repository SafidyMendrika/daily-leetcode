class Solution {
    public long maximumTripletValue(int[] nums) {
        int n = nums.length;
        long result = 0;
        
        int[] maxDiff = new int[n];
        
        int[] maxNum = new int[n];
        maxNum[0] = nums[0];
        
        for (int i = 1; i < n; i++) {
            maxNum[i] = Math.max(maxNum[i-1], nums[i]);
        }
        
        for (int j = 1; j < n-1; j++) {
            maxDiff[j] = Math.max(maxDiff[j-1], maxNum[j-1] - nums[j]);
            
            result = Math.max(result, (long)maxDiff[j] * nums[j+1]);
        }
        
        return result;
    }
}