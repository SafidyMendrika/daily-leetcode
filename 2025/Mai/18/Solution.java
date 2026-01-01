import java.util.*;

class Solution {
    static final int MOD = 1_000_000_007;

    public int colorTheGrid(int m, int n) {
        List<int[]> validStates = new ArrayList<>();
        Map<String, Integer> stateToIndex = new HashMap<>();
        generateStates(m, new ArrayList<>(), validStates, stateToIndex);
        int totalStates = validStates.size();
        List<List<Integer>> compatible = new ArrayList<>();
        for (int i = 0; i < totalStates; i++) {
            compatible.add(new ArrayList<>());
            for (int j = 0; j < totalStates; j++) {
                if (isCompatible(validStates.get(i), validStates.get(j))) {
                    compatible.get(i).add(j);
                }
            }
        }
        long[][] dp = new long[n][totalStates];
        Arrays.fill(dp[0], 1L); 
        for (int col = 1; col < n; col++) {
            for (int curr = 0; curr < totalStates; curr++) {
                for (int prev : compatible.get(curr)) {
                    dp[col][curr] = (dp[col][curr] + dp[col - 1][prev]) % MOD;
                }
            }
        }
        long result = 0;
        for (int i = 0; i < totalStates; i++) {
            result = (result + dp[n - 1][i]) % MOD;
        }
        return (int) result;
    }
    private void generateStates(int m, List<Integer> curr, List<int[]> states, Map<String, Integer> map) {
        if (curr.size() == m) {
            int[] arr = curr.stream().mapToInt(i -> i).toArray();
            states.add(arr);
            map.put(Arrays.toString(arr), states.size() - 1);
            return;
        }
        for (int color = 0; color < 3; color++) {
            if (curr.isEmpty() || curr.get(curr.size() - 1) != color) {
                curr.add(color);
                generateStates(m, curr, states, map);
                curr.remove(curr.size() - 1);
            }
        }
    }
    private boolean isCompatible(int[] a, int[] b) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == b[i]) return false;
        }
        return true;
    }
}