public class Solution {
    public int minimumLength(String s) {
        if (s == null || s.length() <= 2) return s.length();
        
        char[] chars = s.toCharArray();
        boolean[] removed = new boolean[chars.length];
        boolean changed;
        
        do {
            changed = false;
            for (int i = 0; i < chars.length; i++) {
                if (removed[i]) continue;
                
                int left = -1;
                for (int j = i - 1; j >= 0; j--) {
                    if (!removed[j] && chars[j] == chars[i]) {
                        left = j;
                        break;
                    }
                }
                
                int right = -1;
                for (int j = i + 1; j < chars.length; j++) {
                    if (!removed[j] && chars[j] == chars[i]) {
                        right = j;
                        break;
                    }
                }
                
                if (left != -1 && right != -1) {
                    removed[left] = true;
                    removed[right] = true;
                    changed = true;
                }
            }
        } while (changed); 
        
        int remaining = 0;
        for (boolean isRemoved : removed) {
            if (!isRemoved) remaining++;
        }
        
        return remaining;
    }

}
