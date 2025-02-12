import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> digitSumMap = new HashMap<>(); 
        int maxSum = -1;
        
        for (int num : nums) {
            int sumDigits = this.getDigitSum(num);
            
            if (digitSumMap.containsKey(sumDigits)) {
                maxSum = Math.max(maxSum, num + digitSumMap.get(sumDigits));
                digitSumMap.put(sumDigits, Math.max(digitSumMap.get(sumDigits), num));
            } else {
                digitSumMap.put(sumDigits, num);
            }
        }
        
        return maxSum;
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
