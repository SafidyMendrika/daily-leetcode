import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countGood(int[] nums, int k) {
        int n = nums.length;
        long result = 0;
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        
        int left = 0;
        long currentPairs = 0;
        
        for (int right = 0; right < n; right++) {
            int currentFreq = frequencyMap.getOrDefault(nums[right], 0);
            currentPairs += currentFreq; 
            frequencyMap.put(nums[right], currentFreq + 1);
            
            while (left <= right && currentPairs >= k) {
                result += (n - right);
                
                int leftFreq = frequencyMap.get(nums[left]);
                frequencyMap.put(nums[left], leftFreq - 1);
                
                currentPairs -= (leftFreq - 1);
                
                left++;
            }
        }
        
        return result;
    }
}