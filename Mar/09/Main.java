public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int [] colors = {0,1,0,0,1,0,1}; 
        int k = 6;

        System.out.println(solution.numberOfAlternatingGroups(colors, k));
    }
}
