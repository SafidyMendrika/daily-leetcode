public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int [] nums = {0,1,7,4,4,5};
        int lower = 3;
        int upper = 6;

        System.out.println(solution.countFairPairs(nums, lower, upper)); 

    }   
}