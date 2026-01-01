class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int n2 = n * n;
        int[] freq = new int[n2 + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                freq[grid[i][j]]++;
            }
        }
        int repeated = -1;
        int missing = -1;
        for (int i = 1; i <= n2; i++) {
            if (freq[i] == 2) {
                repeated = i;
            } else if (freq[i] == 0) {
                missing = i;
            }
            
            if (repeated != -1 && missing != -1) {
                break;
            }
        }
        return new int[] {repeated, missing};
    }
}