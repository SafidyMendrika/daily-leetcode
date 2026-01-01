class Solution {
    public int numberOfSubstrings(String s) {
        int result = 0;
        int n = s.length();
        
        int[] lastIndex = {-1, -1, -1}; 
        
        for (int i = 0; i < n; i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
            
            int minIndex = Math.min(lastIndex[0], Math.min(lastIndex[1], lastIndex[2]));
            
            if (minIndex != -1) {
                result += minIndex + 1;
            }
        }
        
        return result;
    }
}