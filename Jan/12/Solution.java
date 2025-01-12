public class Solution {
    public boolean canBeValid(String s, String locked) {
        if (s.length() % 2 != 0) {
            return false;
        }

        int open = 0, close = 0, flexible = 0;

        for (int i = 0; i < s.length(); i++) {
            if (locked.charAt(i) == '0') {
                flexible++;
            } else if (s.charAt(i) == '(') {
                open++;
            } else {
                close++;
            }

            if (close > open + flexible) {
                return false;
            }
        }

        open = 0;
        close = 0;
        flexible = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (locked.charAt(i) == '0') {
                flexible++;
            } else if (s.charAt(i) == '(') {
                open++;
            } else {
                close++;
            }

            if (open > close + flexible) {
                return false;
            }
        }

        return true;
    }
}