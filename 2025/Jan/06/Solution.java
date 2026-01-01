public class Solution {
    public int[] minOperations(String boxes) {
        int[] result = new int[boxes.length()];

        for (int i = 0; i < boxes.length(); i++) {
            int count = 0;

            for (int j = 0; j < boxes.length(); j++) {
                if (boxes.charAt(j) == '1') {
                    count += Math.abs(i - j);
                }
            }

            result[i] = count;
        }

        return result;
    }
}
