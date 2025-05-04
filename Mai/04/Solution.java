class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] count = new int[100]; 
        int result = 0;
        int min = 0;
        int max = 0;
        int index = 0;
        for (int[] domino : dominoes) {
            min = Math.min(domino[0], domino[1]);
            max = Math.max(domino[0], domino[1]);
            index = min * 10 + max; 
            result += count[index]; 
            count[index]++; 
        }
        return result;
    }
}