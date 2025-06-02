class Solution {
    public long distributeCandies(int n, int limit) {
        return countWays(n, limit);
    }

    private long countWays(int n, int limit) {
        long res = comb(n + 2, 2);  

        for (int i = 1; i <= 3; i++) {
            long sign = (i % 2 == 1) ? -1 : 1;
            for (int mask = 0; mask < (1 << 3); mask++) {
                if (Integer.bitCount(mask) == i) {
                    int reduced = (limit + 1) * i;
                    if (n - reduced >= 0) {
                        res += sign * comb(n - reduced + 2, 2);
                    }
                }
            }
        }

        return res;
    }

    private long comb(long n, long k) {
        if (n < 0 || k < 0 || k > n) return 0;
        long res = 1;
        for (long i = 1; i <= k; i++) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }
}
