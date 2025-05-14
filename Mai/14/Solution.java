import java.util.List;

class Solution {
    public int lengthAfterTransformations(String s, int t, List<Integer> nums) {
        final int MOD = 1_000_000_007;
        
        int[] numsArray = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            numsArray[i] = nums.get(i);
        }
        
        int[] charCount = new int[26];
        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;
        }
        
        int[][] matrix = new int[26][26];
        
        for (int i = 0; i < 26; i++) {  
            int count = numsArray[i]; 
            for (int j = 0; j < count; j++) {
                matrix[i][(i + j + 1) % 26]++;
            }
        }
        
        int[][] resultMatrix = matrixPower(matrix, t, MOD);
        
        long finalLength = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                finalLength = (finalLength + (long)charCount[i] * resultMatrix[i][j]) % MOD;
            }
        }
        
        return (int)finalLength;
    }
    
    private int[][] matrixPower(int[][] matrix, long power, int mod) {
        int n = matrix.length;
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            result[i][i] = 1;
        }
        
        while (power > 0) {
            if (power % 2 == 1) {
                result = matrixMultiply(result, matrix, mod);
            }
            matrix = matrixMultiply(matrix, matrix, mod);
            power /= 2;
        }
        
        return result;
    }
    
    private int[][] matrixMultiply(int[][] A, int[][] B, int mod) {
        int n = A.length;
        int[][] C = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long sum = 0;
                for (int k = 0; k < n; k++) {
                    sum = (sum + (long)A[i][k] * B[k][j]) % mod;
                }
                C[i][j] = (int)sum;
            }
        }
        
        return C;
    }
}