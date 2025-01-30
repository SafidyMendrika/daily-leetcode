from collections import defaultdict, deque

class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        def find_max_groups(start: int, graph: defaultdict) -> int:
            visited = {start: 0}  
            queue = deque([(start, 0)])  
            max_group = 0
            
            while queue:
                node, curr_group = queue.popleft()
                
                for neighbor in graph[node]:
                    if neighbor in visited:
                        if abs(visited[neighbor] - curr_group) != 1:
                            return -1
                    else:
                        next_group = curr_group + 1
                        visited[neighbor] = next_group
                        max_group = max(max_group, next_group)
                        queue.append((neighbor, next_group))
            
            return max_group + 1
        
        def find_component(node: int, visited: set, graph: defaultdict) -> set:
            component = {node}
            stack = [node]
            
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        component.add(neighbor)
                        stack.append(neighbor)
            
            return component
        
        visited = set()
        total_groups = 0
        for node in range(n):
            if node not in visited:
                component = find_component(node, visited, graph)
                max_groups = -1
                for start in component:
                    groups = find_max_groups(start, graph)
                    if groups != -1:
                        max_groups = max(max_groups, groups)
                
                if max_groups == -1:
                    return -1
                total_groups += max_groups
        
        return total_groups
    
if __name__ == "__main__":
    n = 6
    edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
    s = Solution()
    print(s.magnificentSets(n,edges))