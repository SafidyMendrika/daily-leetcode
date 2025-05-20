class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] diff = new int[n + 1];
        
        for (int[] query : queries) {
            int left = query[0];
            int right = query[1];
            
            diff[left]++;
            diff[right + 1]--;
        }
        
        int decrements = 0;
        
        for (int i = 0; i < n; i++) {
            decrements += diff[i];
            if (decrements < nums[i]) {
                return false;
            }
        }
        
        return true;
    }
}