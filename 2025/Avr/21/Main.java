public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[]  differences = {3,-4,5,1,-2};
        int lower = -4;
        int upper = 5;

        System.out.println(solution.numberOfArrays(differences, lower, upper)); 

    }   
}