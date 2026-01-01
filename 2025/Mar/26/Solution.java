import java.util.Arrays;

class Solution {
    public int minOperations(int[][] grid, int x) {
        int m = grid.length;
        int n = grid[0].length;
        int[] nums = new int[m * n];
        
        int index = 0;
        for (int[] row : grid) {
            for (int num : row) {
                nums[index++] = num;
            }
        }
        
        Arrays.sort(nums);
        
        for (int num : nums) {
            if ((num - nums[0]) % x != 0) {
                return -1;
            }
        }
        
        int median = nums[(m * n) / 2];
        
        int totalOps = 0;
        for (int num : nums) {
            totalOps += Math.abs(num - median) / x;
        }
        
        return totalOps;
    }
}