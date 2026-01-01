class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        long minVal = 0;
        long maxVal = 0;
        long curr = 0;
        
        for (int diff : differences) {
            curr += diff;
            minVal = Math.min(minVal, curr);
            maxVal = Math.max(maxVal, curr);
        }
        
        long validStartCount = (upper - lower) - (maxVal - minVal) + 1;
        
        return validStartCount > 0 ? (int)validStartCount : 0;
    }
}