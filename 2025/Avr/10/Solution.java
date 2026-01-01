class Solution {
    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        return solve(String.valueOf(finish), s, limit) - solve(String.valueOf(start-1), s, limit);
    }

    private long solve(String str, String inputSuffix, int limit)
    {
        if(str.length()<inputSuffix.length()) return 0;
        int remainingLen=str.length()-inputSuffix.length();
        long cnt=0;
        for(int i=0;i<remainingLen;i++)
        {
            long digit=str.charAt(i)-'0';
            if(digit<=limit)
            {
                cnt+=digit*Math.pow(limit+1, remainingLen-i-1);
            }
            else
            {
                cnt+=Math.pow(limit+1, remainingLen-i);
                return cnt;
            }
        }
        if(Long.parseLong(str.substring(str.length()-inputSuffix.length(), str.length()))>=Long.parseLong(inputSuffix)) cnt+=1;
        return cnt;
    }
}