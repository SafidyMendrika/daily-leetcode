class Solution {
    public long repairCars(int[] ranks, int cars) {
        long left = 0;
        long right = (long) getMaxRank(ranks) * (long) cars * (long) cars;
        
        while (left < right) {
            long mid = left + (right - left) / 2;
            
            if (canRepairAllCars(ranks, cars, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
    
    private boolean canRepairAllCars(int[] ranks, int cars, long time) {
        long totalCarsRepaired = 0;
        
        for (int rank : ranks) {
            long carsRepairedByThisMechanic = (long) Math.sqrt(time / rank);
            totalCarsRepaired += carsRepairedByThisMechanic;
            
            if (totalCarsRepaired >= cars) {
                return true;
            }
        }
        
        return totalCarsRepaired >= cars;
    }
    
    private int getMaxRank(int[] ranks) {
        int maxRank = ranks[0];
        for (int rank : ranks) {
            maxRank = Math.max(maxRank, rank);
        }
        return maxRank;
    }
}