import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
class Solution {
    public int countPaths(int n, int[][] roads) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] road : roads) {
            graph.get(road[0]).add(new int[]{road[1], road[2]});
            graph.get(road[1]).add(new int[]{road[0], road[2]});
        }
        
        int mod = (int)1e9 + 7;
        
        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;
        
        int[] count = new int[n];
        count[0] = 1;
        
        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.add(new long[]{0, 0});
        
        while (!pq.isEmpty()) {
            long[] current = pq.poll();
            long time = current[0];
            int node = (int)current[1];
            
            if (time > dist[node]) continue;
            
            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0];
                long nextTime = dist[node] + neighbor[1];
                
                if (nextTime < dist[nextNode]) {
                    dist[nextNode] = nextTime;
                    pq.add(new long[]{nextTime, nextNode});
                    count[nextNode] = count[node];
                }
                else if (nextTime == dist[nextNode]) {
                    count[nextNode] = (count[nextNode] + count[node]) % mod;
                }
            }
        }
        
        return count[n-1];
    }
}