class Solution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        int n = colors.length;
        int count = 0;
        int alternatingCount = 0;

        for (int i = 0; i < k - 1; i++) {
            if (colors[i] != colors[i + 1]) {
                alternatingCount++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (alternatingCount == k - 1) {
                count++;
            }

            int outIndex = i;               
            int inIndex = (i + k - 1) % n;  

            if (colors[outIndex] != colors[(outIndex + 1) % n]) {
                alternatingCount--;
            }

            if (colors[inIndex] != colors[(inIndex + 1) % n]) {
                alternatingCount++;
            }
        }

        return count;
    }
}