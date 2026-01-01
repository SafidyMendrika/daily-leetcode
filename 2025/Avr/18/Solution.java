class Solution {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        
        String prev = "1";
        
        for (int i = 2; i <= n; i++) {
            prev = getNext(prev);
        }
        
        return prev;
    }
    
    private String getNext(String s) {
        StringBuilder result = new StringBuilder();
        char currentChar = s.charAt(0);
        int count = 1;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == currentChar) {
                count++;
            } else {
                result.append(count).append(currentChar);
                currentChar = s.charAt(i);
                count = 1;
            }
        }
        
        result.append(count).append(currentChar);
        
        return result.toString();
    }
}