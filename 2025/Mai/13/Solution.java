class Solution {
    public int lengthAfterTransformations(String s, int t) {
        final int MOD = 1_000_000_007;
        
        long[] counts = new long[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }
        
        for (int i = 0; i < t; i++) {
            long[] newCounts = new long[26];
            
            for (int j = 0; j < 25; j++) {
                newCounts[j + 1] = (newCounts[j + 1] + counts[j]) % MOD;
            }
            
            newCounts[0] = (newCounts[0] + counts[25]) % MOD;  
            newCounts[1] = (newCounts[1] + counts[25]) % MOD;  
            
            counts = newCounts;
        }
        
        long total = 0;
        for (long count : counts) {
            total = (total + count) % MOD;
        }
        
        return (int) total;
    }
}