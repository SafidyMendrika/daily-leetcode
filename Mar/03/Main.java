import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution s=  new Solution();
        int[] nums = {9,12,5,10,14,3,10};
        int pivot = 10;
        System.out.println(Arrays.toString(s.pivotArray(nums,pivot)));
    }
}
