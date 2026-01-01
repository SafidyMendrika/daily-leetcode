import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int countDays(int days, int[][] meetings) {
        if (meetings == null || meetings.length == 0) {
            return days;
        }
        
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);
        
        List<int[]> mergedMeetings = new ArrayList<>();
        mergedMeetings.add(meetings[0]);
        
        for (int i = 1; i < meetings.length; i++) {
            int[] lastMeeting = mergedMeetings.get(mergedMeetings.size() - 1);
            int[] currentMeeting = meetings[i];
            
            if (currentMeeting[0] <= lastMeeting[1]) {
                lastMeeting[1] = Math.max(lastMeeting[1], currentMeeting[1]);
            } else {
                mergedMeetings.add(currentMeeting);
            }
        }
        
        int occupiedDays = 0;
        for (int[] meeting : mergedMeetings) {
            occupiedDays += meeting[1] - meeting[0] + 1;
        }
        
        return Math.max(0, days - occupiedDays);
    }
}