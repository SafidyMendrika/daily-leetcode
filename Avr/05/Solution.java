class Solution {
    public int subsetXORSum(int[] nums) {
        return calculateSubsetXORSum(nums, 0, 0);
    }
    
    private int calculateSubsetXORSum(int[] nums, int index, int currentXOR) {
        if (index == nums.length) {
            return currentXOR;
        }
        
        int includeCurrentElement = calculateSubsetXORSum(nums, index + 1, currentXOR ^ nums[index]);
        int excludeCurrentElement = calculateSubsetXORSum(nums, index + 1, currentXOR);
        
        return includeCurrentElement + excludeCurrentElement;
    }
}