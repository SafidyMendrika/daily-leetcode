import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];
            adj[a].add(b);
            adj[b].add(a);
        }
        
        boolean[] visited = new boolean[n];
        int completeCount = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                List<Integer> component = new ArrayList<>();
                dfs(i, adj, visited, component);
                
                if (isComplete(component, adj)) {
                    completeCount++;
                }
            }
        }
        
        return completeCount;
    }
    
    private void dfs(int node, List<Integer>[] adj, boolean[] visited, List<Integer> component) {
        visited[node] = true;
        component.add(node);
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited, component);
            }
        }
    }
    
    private boolean isComplete(List<Integer> component, List<Integer>[] adj) {
        int size = component.size();
        
        for (int node : component) {
            if (adj[node].size() != size - 1) {
                return false;
            }
        }
        
        return true;
    }
}