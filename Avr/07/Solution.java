class Solution {
    public boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        if (totalSum % 2 != 0) {
            return false;
        }
        int targetSum = totalSum / 2;
        boolean[] dp = new boolean[targetSum + 1];
        dp[0] = true;
        
        for (int currentNum : nums) {
            for (int j = targetSum; j >= currentNum; j--) {
                if (dp[j - currentNum]) {
                    dp[j] = true;
                }
            }
        }
        
        return dp[targetSum];
    }
}