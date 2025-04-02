class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1]; 
        
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            int points = questions[i][0];
            int jumpForward = questions[i][1];
            
            int nextIndex = Math.min(i + jumpForward + 1, n);
            long solvePoints = points + dp[nextIndex];
            
            long skipPoints = dp[i + 1];
            
            dp[i] = Math.max(solvePoints, skipPoints);
        }
        
        return dp[0];
    }
}