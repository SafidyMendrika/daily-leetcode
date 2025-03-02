import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        int[][] nums1 = {{1,2},{2,3},{4,5}};
        int[][] nums2 = {{1,4},{3,2},{4,1}};
        

        System.out.println(Arrays.deepToString(s.mergeArrays(nums1, nums2)));
    }
}
