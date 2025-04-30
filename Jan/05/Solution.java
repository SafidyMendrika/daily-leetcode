class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int[] changes = new int[s.length() + 1];
        
        for (int[] shift : shifts) {
            int start = shift[0];
            int end = shift[1];
            int direction = shift[2];
            
            int value = direction == 1 ? 1 : -1;
            
            changes[start] += value;      
            changes[end + 1] -= value;    
        }
        
        char[] result = s.toCharArray();
        int sum = 0;
        
        for (int i = 0; i < s.length(); i++) {
            sum += changes[i];
            
            int shift = ((result[i] - 'a') + sum) % 26;
            if (shift < 0) shift += 26;  
            
            result[i] = (char) ('a' + shift);
        }
        
        return String.valueOf(result);
    }
}