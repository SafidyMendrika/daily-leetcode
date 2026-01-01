import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long countInterestingSubarrays(List<Integer> nums, int modulo, int k) {
        int n = nums.size();
        long result = 0;
        
        Map<Integer, Integer> prefixModFreq = new HashMap<>();
        prefixModFreq.put(0, 1); 
        
        int prefixMod = 0; 
        
        for (int i = 0; i < n; i++) {
            if (nums.get(i) % modulo == k) {
                prefixMod = (prefixMod + 1) % modulo;
            }
            
            int target = (prefixMod - k + modulo) % modulo;
            
            result += prefixModFreq.getOrDefault(target, 0);
            
            prefixModFreq.put(prefixMod, prefixModFreq.getOrDefault(prefixMod, 0) + 1);
        }
        
        return result;
    }
}