
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int days = 10;
        int[][] meetings  = {{5,7},{1,3},{9,10}};
        
        System.out.println(solution.countDays(days, meetings));
    }
}
