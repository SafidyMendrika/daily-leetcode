import java.util.HashMap;
import java.util.Map;

public class Solution {

    public boolean canConstruct(String s, int k) {
        if (s.length() < k) {
            return false;
        }
    
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
    
        int oddCount = 0;
        for (int count : charCount.values()) {
            if (count % 2 != 0) {
                oddCount++;
            }
        }
    
        return oddCount <= k;
    }
}
