public class Main {

    public static void main(String[] args) {
        
        //A = [1,3,2,4], B = [3,1,2,4]

        int[] A = {1,3,2,4};
        int[] B = {3,1,2,4};

        Solution solution = new Solution();

        int[] result = solution.findThePrefixCommonArray(A, B);
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i] + " ");
        }

        
    }
}