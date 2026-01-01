
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        String[] words = {"a","b","c","d"};
        int[] groups = {1,0,1,1};

        System.out.println(solution.getLongestSubsequence(words, groups));

    }   
}