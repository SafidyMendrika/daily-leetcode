class Solution {
    public int countGoodNumbers(long n) {
        long MOD = 1_000_000_007;
        long evenCount = 5; 
        long primeCount = 4;

        long evenPositions = (n + 1) / 2; 
        long oddPositions = n / 2; 

        long result = 1;
        result = (result * modPow(evenCount, evenPositions, MOD)) % MOD;
        result = (result * modPow(primeCount, oddPositions, MOD)) % MOD;

        return (int) result;
        }

    private long modPow(long base, long exp, long mod) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) {
            result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
        
        
    }
}