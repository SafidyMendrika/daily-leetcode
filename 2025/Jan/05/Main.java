public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String s = "abc";
        int[][] shifts = {{0, 1, 0}, {1, 2, 1},{0,2,1}};

        System.out.println(solution.shiftingLetters(s, shifts)); 
    }
}