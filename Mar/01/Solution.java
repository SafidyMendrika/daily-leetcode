public class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        for (int i = 0 ; i < n ; i++) {
            if (i < n-1 && nums[i] == nums[i + 1]) {
                result[i] = nums[i] * 2;
                nums[i+1] = 0;
            }else{
                result[i] = nums[i];
            }
        }

        result = this.shiftAllInEnd(0, result);

        return result;
    }
    public int[] shiftAllInEnd(int numToShift,int[] nums){
        int n = nums.length;
        int[] result = new int[n];

        int shiftIndex = 0;
        int normalIndex = 0;
        for(int i = 0 ; i < n; i++){
            if (nums[i] == numToShift) {
                result[n-shiftIndex-1] = nums[i];
                shiftIndex ++;
            }else{
                result[normalIndex] = nums[i];
                normalIndex++;
            }
        }

        return result;
    }
    public void displayArray(int[] arr){
        System.out.print("[");
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.print("]");

    }
}