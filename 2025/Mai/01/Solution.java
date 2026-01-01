import java.util.Arrays;
import java.util.TreeMap;

class Solution {
    public int maxTaskAssign(int[] tasks, int[] workers, int pills, int strength) {
        Arrays.sort(tasks);
        Arrays.sort(workers);
        
        int left = 0;
        int right = Math.min(tasks.length, workers.length);
        
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            
            if (canAssign(tasks, workers, pills, strength, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
    
    private boolean canAssign(int[] tasks, int[] workers, int pills, int strength, int count) {
        int[] selectedTasks = Arrays.copyOf(tasks, count);
        int[] selectedWorkers = new int[count];
        
        for (int i = 0; i < count; i++) {
            selectedWorkers[i] = workers[workers.length - count + i];
        }
        
        TreeMap<Integer, Integer> availableWorkers = new TreeMap<>();
        for (int w : selectedWorkers) {
            availableWorkers.put(w, availableWorkers.getOrDefault(w, 0) + 1);
        }
        
        for (int i = count - 1; i >= 0; i--) {
            int task = selectedTasks[i];
            
            Integer strongEnoughWorker = availableWorkers.ceilingKey(task);
            
            if (strongEnoughWorker != null) {
                if (availableWorkers.get(strongEnoughWorker) == 1) {
                    availableWorkers.remove(strongEnoughWorker);
                } else {
                    availableWorkers.put(strongEnoughWorker, availableWorkers.get(strongEnoughWorker) - 1);
                }
            } else if (pills > 0) {
                Integer potentialWorker = availableWorkers.ceilingKey(task - strength);
                
                if (potentialWorker != null) {
                    pills--;
                    if (availableWorkers.get(potentialWorker) == 1) {
                        availableWorkers.remove(potentialWorker);
                    } else {
                        availableWorkers.put(potentialWorker, availableWorkers.get(potentialWorker) - 1);
                    }
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        
        return true;
    }
}