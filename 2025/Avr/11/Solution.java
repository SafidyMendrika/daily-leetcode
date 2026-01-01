class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int result = 0;

        for (int i = low; i <= high; i++) {
            if (isSymmetric(i)) {
                result++;
            }
        }

        return result;
    }

    private boolean isSymmetric(int n) {
        String str = Integer.toString(n);
        int len = str.length();

        if (len % 2 != 0) {
            return false;
        }

        int mid = len / 2;
        int leftSum = 0, rightSum = 0;

        for (int i = 0; i < mid; i++) {
            leftSum += str.charAt(i) - '0';
            rightSum += str.charAt(len - 1 - i) - '0';
        }

        return leftSum == rightSum;
    }
}