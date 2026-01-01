class Solution(object):
    def findRedundantConnection(self, edges):
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parent[root_x] = root_y
            return True
        
        parent = {i: i for i in range(1, len(edges) + 1)}
        for edge in edges:
            if not union(*edge):
                return edge
        return []
        

if __name__ == "__main__":
    edges = [[1,2], [1,3], [2,3]]
    print(Solution().findRedundantConnection(edges)) 