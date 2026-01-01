class Solution {
    public long goodTriplets(int[] nums1, int[] nums2) {
        int n = nums1.length;
        
        int[] pos = new int[n];
        for (int i = 0; i < n; i++) {
            pos[nums2[i]] = i;
        }
        
        int[] mapped = new int[n];
        for (int i = 0; i < n; i++) {
            mapped[i] = pos[nums1[i]];
        }
        
        long[] smaller = new long[n];
        long[] greater = new long[n];
        
        Bit bit = new Bit(n);
        
        for (int i = 0; i < n; i++) {
            smaller[i] = bit.query(mapped[i] - 1);
            bit.update(mapped[i], 1);
        }
        
        bit = new Bit(n);
        
        for (int i = n - 1; i >= 0; i--) {
            greater[i] = bit.query(n - 1) - bit.query(mapped[i]);
            bit.update(mapped[i], 1);
        }
        
        long result = 0;
        for (int i = 0; i < n; i++) {
            result += smaller[i] * greater[i];
        }
        
        return result;
    }
    
    
}