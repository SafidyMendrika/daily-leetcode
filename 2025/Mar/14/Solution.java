class Solution {
    public int maximumCandies(int[] candies, long k) {
        int maxCandy = 0;
        for (int candy : candies) {
            maxCandy = Math.max(maxCandy, candy);
        }
        
        long totalCandies = 0;
        for (int candy : candies) {
            totalCandies += candy;
        }
        if (totalCandies < k) {
            return 0;
        }
        
        int left = 1; 
        int right = maxCandy;
        int result = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (canAllocate(candies, k, mid)) {
                result = mid; 
                left = mid + 1;
            } else {
                right = mid - 1; 
            }
        }
        
        return result;
    }
    
    private boolean canAllocate(int[] candies, long k, int candiesPerChild) {
        long piles = 0;
        
        for (int candy : candies) {
            piles += candy / candiesPerChild; 
            
            if (piles >= k) {
                return true; 
            }
        }
        
        return false; 
    }
}