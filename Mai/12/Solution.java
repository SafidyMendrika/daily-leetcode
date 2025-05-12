import java.util.*;

class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] frequency = new int[10];
        for (int digit : digits) {
            frequency[digit]++;
        }
        
        List<Integer> result = new ArrayList<>();
        
        for (int i = 1; i <= 9; i++) {
            if (frequency[i] > 0) {
                frequency[i]--; 
                
                for (int j = 0; j <= 9; j++) {
                    if (frequency[j] > 0) {
                        frequency[j]--;
                        
                        for (int k = 0; k <= 8; k += 2) {
                            if (frequency[k] > 0) {
                                int num = i * 100 + j * 10 + k;
                                result.add(num);
                            }
                        }
                        
                        frequency[j]++;
                    }
                }
                
                frequency[i]++; 
            }
        }
        
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        Arrays.sort(answer);
        
        return answer;
    }
}