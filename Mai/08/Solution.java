import java.util.*;

class Solution {
    class Pair implements Comparable<Pair> {
        int row;
        int col;
        long time;
        int which;

        Pair(int r, int c, long t,int w) {
            this.row = r;
            this.col = c;
            this.time = t;
            this.which = w;
        }

        @Override
        public int compareTo(Pair other) {
            return Long.compare(this.time, other.time);
        }
    }

    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;

        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.offer(new Pair(0, 0, 0L,-1));

        long[][] minTime = new long[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(minTime[i], Long.MAX_VALUE);
        }
        minTime[0][0] = 0L;

        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int r = current.row, c = current.col;
            long t = current.time;
             int add = (current.which==1?2:1);

            if (r == n - 1 && c == m - 1) return (int) t;

            for (int i = 0; i < 4; i++) {
                int rr = r + dx[i];
                int cc = c + dy[i];

                if (rr >= 0 && rr < n && cc >= 0 && cc < m) {
                    long newTime = Math.max(t + add, (long)(moveTime[rr][cc]+add));

                    if (minTime[rr][cc] > newTime) {
                        minTime[rr][cc] = newTime;
                        pq.offer(new Pair(rr, cc, newTime,add));
                    }
                }
            }
        }

        return -1; 
    }
}
