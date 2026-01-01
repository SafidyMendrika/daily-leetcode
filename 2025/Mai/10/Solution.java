class Solution {
    public long minSum(int[] nums1, int[] nums2) {
        long sum1 = 0, sum2 = 0;
        int zeros1 = 0, zeros2 = 0;
        
        for (int num : nums1) {
            sum1 += num;
            if (num == 0) zeros1++;
        }
        
        for (int num : nums2) {
            sum2 += num;
            if (num == 0) zeros2++;
        }
        
        long minPossibleSum1 = sum1 + zeros1; 
        long minPossibleSum2 = sum2 + zeros2; 
        
        if (zeros1 == 0 && minPossibleSum1 < minPossibleSum2) {
            return -1;
        }
        
        if (zeros2 == 0 && minPossibleSum2 < minPossibleSum1) {
            return -1; 
        }
        
        return Math.max(minPossibleSum1, minPossibleSum2);
    }
}