class Solution {
    public boolean divideArray(int[] nums) {
        int[] frequency = new int[501];
        
        for (int num : nums) {
            frequency[num]++;
        }
        
        for (int count : frequency) {
            if (count % 2 != 0) {
                return false;
            }
        }
        
        return true;
    }
}