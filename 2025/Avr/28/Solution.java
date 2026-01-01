class Solution {
    public long countSubarrays(int[] nums, long k) {
        int n = nums.length;
        long count = 0;
        long sum = 0;
        
        for (int left = 0, right = 0; right < n; right++) {
            sum += nums[right];
            
            while (left <= right && sum * (right - left + 1) >= k) {
                sum -= nums[left];
                left++;
            }
            
            count += (right - left + 1);
        }
        
        return count;
    }
}