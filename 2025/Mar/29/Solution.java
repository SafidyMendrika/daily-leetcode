import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public int maximumScore(List<Integer> nums, int k) {
        final int MOD = 1_000_000_007;
        int n = nums.size();
        
        int[] primeScores = new int[n];
        for (int i = 0; i < n; i++) {
            primeScores[i] = calculatePrimeScore(nums.get(i));
        }
        
        int[] left = new int[n];
        int[] right = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && primeScores[stack.peek()] < primeScores[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
        stack.clear();
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && primeScores[stack.peek()] <= primeScores[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        
        long[] counts = new long[n];
        for (int i = 0; i < n; i++) {
            counts[i] = (long)(i - left[i]) * (right[i] - i);
        }
        
        List<Operation> operations = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            operations.add(new Operation(nums.get(i), counts[i]));
        }
        
        operations.sort((a, b) -> b.value - a.value);
        
        long score = 1L;
        long remainingOps = k;
        
        for (Operation op : operations) {
            long opsToUse = Math.min(remainingOps, op.count);
            
            if (opsToUse <= 0) continue;
            
            long power = fastPow(op.value, opsToUse, MOD);
            score = (score * power) % MOD;
            
            remainingOps -= opsToUse;
            if (remainingOps == 0) break;
        }
        
        return (int) score;
    }
    
    private int calculatePrimeScore(int num) {
        int score = 0;
        int n = num;
        
        if (n % 2 == 0) {
            score++;
            while (n % 2 == 0) {
                n /= 2;
            }
        }
        
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) {
                score++;
                while (n % i == 0) {
                    n /= i;
                }
            }
        }
        if (n > 1) {
            score++;
        }
        
        return score;
    }
    
    private long fastPow(long base, long exp, int mod) {
        long result = 1;
        base = base % mod;
        
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        
        return result;
    }
    
}
class Operation {
    int value;
    long count;
    
    Operation(int value, long count) {
        this.value = value;
        this.count = count;
    }
}