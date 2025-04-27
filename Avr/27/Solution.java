class Solution {
    public int countSubarrays(int[] nums) {
        int count = 0;
        
        if (nums.length < 3) {
            return 0;
        }
        int first = 0;
        int second = 0;
        int third = 0;
        for (int i = 0; i <= nums.length - 3; i++) {
            first = nums[i];
            second = nums[i + 1];
            third = nums[i + 2];
            
            if (first + third == second / 2.0) {
                count++;
            }
        }
        
        return count;
    }
}