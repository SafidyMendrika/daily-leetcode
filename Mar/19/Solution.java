class Solution {
    public int minOperations(int[] nums) {
        int n = nums.length;
        
        if (n < 3) {
            for (int num : nums) {
                if (num == 0) return -1;
            }
            return 0; 
        }
        
        int[] copy1 = nums.clone();
        int ops1 = 0;
        
        for (int i = 0; i <= n - 3; i++) {
            if (copy1[i] == 0) {
                copy1[i] ^= 1;
                copy1[i + 1] ^= 1;
                copy1[i + 2] ^= 1;
                ops1++;
            }
        }
        
        boolean allOnes1 = true;
        for (int num : copy1) {
            if (num == 0) {
                allOnes1 = false;
                break;
            }
        }
        
        if (!allOnes1) {
            return -1; 
        }
        
        return ops1;
    }
}