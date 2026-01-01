import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Solution solution = new Solution();

        String[] a = {"amazon","apple","facebook","google","leetcode"};
        String[] b = {"e","o"};
        
        ArrayList<String> swb = solution.wordSubsets(a,b);
        System.out.println("solution : ");
        for (String string : swb) {
            System.out.println(string);
        }


    }
}
