import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countCompleteSubarrays(int[] nums) {
        Set<Integer> distinctElements = new HashSet<>();
        for (int num : nums) {
            distinctElements.add(num);
        }
        int totalDistinct = distinctElements.size();
        
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            Set<Integer> currentDistinct = new HashSet<>();
            for (int end = start; end < nums.length; end++) {
                currentDistinct.add(nums[end]);
                
                if (currentDistinct.size() == totalDistinct) {
                    count++;
                }
            }
        }
        
        return count;
    }
}