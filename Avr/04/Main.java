public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        Integer[] array = {3, 5, 1, 6, 2, 0, 8, null, null, 7, 4};
        TreeNode root = Solution.arrayToTree(array);

        Solution.printLevelOrder(solution.lcaDeepestLeaves(root)); 
    }
}
