public class Main {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        Solution solution = new Solution();
        int[] result = solution.twoSum(nums, target);
        System.out.println("["+result[0] + "," + result[1]+"]");
    }
}
