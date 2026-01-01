
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] tasks = {3,2,1};
        int[]  workers = {0,3,3};
        int pills = 1;
        int strength = 1;


        System.out.println(solution.maxTaskAssign(tasks, workers, pills, strength)); 

    }   
}