
public class Main {
    public static void main(String[] args) {
        
        Solution solution = new Solution();
        int[][]  queries = {{1,3},{0,2},{1,3},{1,2}};
        int[] nums = {1,1,1,1};

        System.out.println(solution.maxRemoval(nums,queries));
        

    }   
}