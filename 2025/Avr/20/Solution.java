import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numRabbits(int[] answers) {
        if (answers == null || answers.length == 0) {
            return 0;
        }
        
        Map<Integer, Integer> count = new HashMap<>();
        for (int answer : answers) {
            count.put(answer, count.getOrDefault(answer, 0) + 1);
        }
        
        int totalRabbits = 0;
        
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int reportedSameColor = entry.getKey();
            int rabbitsWithThisAnswer = entry.getValue();
            int groupSize = reportedSameColor + 1;
            int groupsNeeded = (int) Math.ceil((double) rabbitsWithThisAnswer / groupSize);
            
            totalRabbits += groupsNeeded * groupSize;
        }
        
        return totalRabbits;
    }
}