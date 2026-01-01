
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] status = {1,0,1,0};
        int[] candies = {7,5,4,100};
        int[][] keys = {{},{},{1},{}};
        int[][] containedBoxes = {{1,2},{3},{},{}};
        int[] initialBoxes = {0};


        System.out.println(solution.maxCandies(status,candies,keys,containedBoxes,initialBoxes)); 

    }   
}