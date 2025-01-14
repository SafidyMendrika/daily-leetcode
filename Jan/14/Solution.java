import java.util.HashSet;
import java.util.Set;

public class Solution {

    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] result = new int[n];
        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        for (int i = 0; i < n; i++) {
            setA.add(A[i]);
            setB.add(B[i]);
            int commonCount = 0;
            for (int num : setA) {
            if (setB.contains(num)) {
                commonCount++;
            }
            }
            result[i] = commonCount;
        }

        return result;
    }
}