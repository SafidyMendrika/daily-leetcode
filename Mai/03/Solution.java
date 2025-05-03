class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        
        int rotationsForTop = checkRotations(tops[0], tops, bottoms);
        
        int rotationsForBottom = checkRotations(bottoms[0], tops, bottoms);
        
        int minRotations = Math.min(rotationsForTop, rotationsForBottom);
        return minRotations == Integer.MAX_VALUE ? -1 : minRotations;
    }
    
    private int checkRotations(int target, int[] tops, int[] bottoms) {
        int n = tops.length;
        int rotationsForTop = 0; 
        int rotationsForBottom = 0;  
        
        for (int i = 0; i < n; i++) {
            if (tops[i] != target && bottoms[i] != target) {
                return Integer.MAX_VALUE;
            }
            
            if (tops[i] != target) {
                rotationsForTop++;
            }
            
            if (bottoms[i] != target) {
                rotationsForBottom++;
            }
        }
        
        return Math.min(rotationsForTop, rotationsForBottom);
    }
}