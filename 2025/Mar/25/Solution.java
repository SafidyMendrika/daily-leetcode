import java.util.Arrays;

class Solution {
    public boolean checkValidCuts(int n, int[][] rectangles) {
        if(getCount(rectangles, true)>=3) return true;
        if(getCount(rectangles, false)>=3) return true;
        return false;
    }

    int getCount(int[][] rectangles, boolean xAxis){
        int last = 0, count = 0, i = xAxis ? 0 : 1;
        Arrays.sort(rectangles, (a,b)->a[i]-b[i]);
        for(int[] rec : rectangles) {
            int a = rec[i], b = rec[i+2];
            if(a<last){ 
                last = Math.max(last, b);
                continue;
            }
            count++;
            last = b;
        }
        return count;
    }
}