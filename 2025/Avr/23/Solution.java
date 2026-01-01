class Solution {
    public int countLargestGroup(int n) {
        int[] countMap = new int[37];
        
        for (int i = 1; i <= n; i++) {
            int digitSum = getDigitSum(i);
            countMap[digitSum]++;
        }
        
        int maxSize = 0;
        for (int count : countMap) {
            maxSize = Math.max(maxSize, count);
        }
        
        int result = 0;
        for (int count : countMap) {
            if (count == maxSize) {
                result++;
            }
        }
        
        return result;
    }
    
    private int getDigitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}