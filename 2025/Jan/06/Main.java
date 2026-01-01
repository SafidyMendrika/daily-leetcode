public class Main {

    public static void main(String[] args) {
        String boxes = "001011";

        Solution solution = new Solution();

        int[] result = solution.minOperations(boxes);

        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + " ");
        }
    }
}