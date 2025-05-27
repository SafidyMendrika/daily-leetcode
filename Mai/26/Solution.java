import java.util.*;
class Solution {
    public int largestPathValue(String colors, int[][] edges) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        int n = colors.length();
        int inDegree[] = new int[n];
        for(int edge[] : edges){
            graph.computeIfAbsent(edge[0], k->new ArrayList<>()).add(edge[1]);
            inDegree[edge[1]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<n; i++){
            if(inDegree[i] == 0){
                q.offer(i);
            }
        }
        int count[][] = new int[n][26];
        int ans = 0, nodeSeen = 0;
        while( !q.isEmpty() ){
            int node = q.poll();
            ans = Math.max(ans, ++count[node][colors.charAt(node) - 'a']);
            nodeSeen++;
            if( !graph.containsKey(node) ){
                continue;
            }

            for(int neighbour : graph.get(node)){
                for(int i=0; i<26; i++){
                    count[neighbour][i] = Math.max(count[node][i], count[neighbour][i]);
                }
                inDegree[neighbour]--;
                if(inDegree[neighbour] == 0){
                    q.offer(neighbour);
                }
            }
        }
        return nodeSeen < n ? -1 : ans; 
    }
}