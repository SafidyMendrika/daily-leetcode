import java.util.List;

public class Main {
    public static void main(String[] args) {
        String[] words = {"bab", "dab", "cab"};
        int[] groups = {1, 2, 2};
        
        Solution solution = new Solution();
        List<String> result1 = solution.getWordsInLongestSubsequence(words, groups);
        
        System.out.println(result1);
        

    }   
}