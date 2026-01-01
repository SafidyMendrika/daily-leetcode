public class Main {

    public static void main(String[] args) {
        String[] words = {"apple", "banana", "apricot", "avocado", "blueberry"};
        String pref = "ap";

        Solution sol = new Solution();
        System.out.println(sol.prefixCount(words, pref));
    }
}