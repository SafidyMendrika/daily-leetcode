public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int start = 1 ;
        long finish = 6000;
        int limit = 4;
        String s = "124";

        System.out.println(solution.numberOfPowerfulInt(start,finish,limit,s));
    }
}