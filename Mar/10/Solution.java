class Solution {
    public long countOfSubstrings(String word, int k) {
        int[][] frequencies = new int[2][128];
        
        frequencies[0]['a'] = 1;
        frequencies[0]['e'] = 1;
        frequencies[0]['i'] = 1;
        frequencies[0]['o'] = 1;
        frequencies[0]['u'] = 1;
        
        long result = 0;  
        int consonantCount = 0;
        int vowelCount = 0;     
        int extraLeft = 0;      
        
        for (int right = 0, left = 0; right < word.length(); right++) {
            char rightChar = word.charAt(right);
            
            if (frequencies[0][rightChar] == 1) {
                if (++frequencies[1][rightChar] == 1) {
                    vowelCount++; 
                }
            } else {
                consonantCount++; 
            }
            
            while (consonantCount > k) {
                char leftChar = word.charAt(left);
                if (frequencies[0][leftChar] == 1) {
                    if (--frequencies[1][leftChar] == 0) {
                        vowelCount--; 
                    }
                } else {
                    consonantCount--;
                }
                left++;
                extraLeft = 0;
            }
            
            while (vowelCount == 5 && consonantCount == k && left < right && 
                   frequencies[0][word.charAt(left)] == 1 && frequencies[1][word.charAt(left)] > 1) {
                extraLeft++;
                frequencies[1][word.charAt(left)]--;
                left++;
            }
            
            if (consonantCount == k && vowelCount == 5) {
                result += (1L + extraLeft);  
            }
        }
        
        return result;
    }
}