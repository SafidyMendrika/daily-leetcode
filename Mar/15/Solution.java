class Solution {
    public int minCapability(int[] nums, int k) {
        int left = 1; 
        int right = (int)1e9; 
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (canRobKHouses(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private boolean canRobKHouses(int[] nums, int k, int capability) {
        int count = 0;
        int i = 0;
        
        while (i < nums.length) {
            if (nums[i] <= capability) {
                count++;
                i += 2;
            } else {
                i++;  
            }
        }
        
        return count >= k;
    }
}