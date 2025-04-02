class Solution {
    public long maximumTripletValue(int[] nums) {
    int n = nums.length;
    long maxValue = 0;
    long value = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                value= (long)(nums[i] - nums[j]) * nums[k];
                maxValue = Math.max(maxValue, value);
            }
        }
    }
    
    return maxValue;
}
}