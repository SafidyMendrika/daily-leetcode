import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumOperations(int[] nums) {
        int operations = 0;
        int index = 0;
        
        while (index < nums.length) {
            if (areAllDistinct(nums, index)) {
                return operations;
            }
            
            operations++;
            index += Math.min(3, nums.length - index);
        }
        
        return operations;
    }
    
    private boolean areAllDistinct(int[] nums, int startIndex) {
        Set<Integer> seen = new HashSet<>();
        
        for (int i = startIndex; i < nums.length; i++) {
            if (seen.contains(nums[i])) {
                return false;
            }
            seen.add(nums[i]);
        }
        
        return true;
    }
}