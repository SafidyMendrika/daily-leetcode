import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        int n = words.length;
        int[] dp = new int[n];
        int[] prev = new int[n];
        
        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);
        
        int maxLength = 1;
        int endIndex = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (groups[i] != groups[j] && 
                    words[i].length() == words[j].length() &&
                    hammingDistance(words[i], words[j]) == 1 &&
                    dp[j] + 1 > dp[i]) {
                    
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                    
                    if (dp[i] > maxLength) {
                        maxLength = dp[i];
                        endIndex = i;
                    }
                }
            }
        }
        
        List<String> result = new ArrayList<>();
        while (endIndex != -1) {
            result.add(words[endIndex]);
            endIndex = prev[endIndex];
        }
        
        Collections.reverse(result);
        return result;
    }
    
    private int hammingDistance(String s1, String s2) {
        int distance = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                distance++;
            }
        }
        return distance;
    }
}