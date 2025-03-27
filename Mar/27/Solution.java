import java.util.*;

class Solution {
    public int minimumIndex(List<Integer> nums) {
        int candidate = -1, count = 0;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        int totalOccurrences = 0;
        for (int num : nums) {
            if (num == candidate) {
                totalOccurrences++;
            }
        }

        int countLeft = 0;
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            if (nums.get(i) == candidate) {
                countLeft++;
            }
            int countRight = totalOccurrences - countLeft;
            
            if (countLeft * 2 > (i + 1) && countRight * 2 > (n - i - 1)) {
                return i;
            }
        }

        return -1; 
    }
}