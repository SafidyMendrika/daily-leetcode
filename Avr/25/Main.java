import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        List<Integer> nums = List.of(3,1,9,6);
        int modulo = 3;
        int k = 0;

        System.out.println(solution.countInterestingSubarrays(nums,modulo,k)); 

    }   
}