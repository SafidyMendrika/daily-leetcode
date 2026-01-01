class Solution {
    final int MOD = 1_000_000_007;
    final int MAX_DISTINCT = 14; 

    public int idealArrays(int n, int maxValue) {
        
        long[][] dp = new long[maxValue + 1][MAX_DISTINCT + 1];
        
        for (int i = 1; i <= maxValue; i++) {
            dp[i][1] = 1;
        }
        
        for (int len = 2; len <= MAX_DISTINCT; len++) {
            for (int val = 1; val <= maxValue; val++) {
                for (int div = 2; div * val <= maxValue; div++) {
                    dp[div * val][len] = (dp[div * val][len] + dp[val][len - 1]) % MOD;
                }
            }
        }
        
        long[][] comb = new long[n + 1][MAX_DISTINCT + 1];
        for (int i = 0; i <= n; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= Math.min(i, MAX_DISTINCT); j++) {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }
        
        long result = 0;
        for (int val = 1; val <= maxValue; val++) {
            for (int len = 1; len <= MAX_DISTINCT && len <= n; len++) {
                if (dp[val][len] > 0) {
                    result = (result + (dp[val][len] * comb[n - 1][len - 1]) % MOD) % MOD;
                }
            }
        }
        
        return (int) result;
    }
}