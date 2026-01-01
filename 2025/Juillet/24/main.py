from collections import defaultdict


class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        def dfs(node):  # (bottom up)
            if node in visited:
                return 
            
            visited.add(node)
            
            for neigh in adjs[node]:
                if neigh in visited:
                    continue 
                
                dfs(neigh)

                prefix[node] ^= prefix[neigh]

                children[node].add(neigh)

                children[node] |= children[neigh]
                
        n = len(nums)

        indegree = [0] * n

        adjs = defaultdict(list)
        for src, des in edges:
            adjs[src] += [des]
            adjs[des] += [src]
            indegree[src] += 1
            indegree[des] += 1
        
        max_degree = max(indegree)

        for i, degree in enumerate(indegree):
            if degree == max_degree: 
                root = i

        prefix = [num for num in nums]   
        visited = set()                    
        children = defaultdict(set)      

        dfs(root)

        res = float('inf')

        for i in range(1, n - 1):
            for j in range(i):
                (a, b), (c, d) = edges[i], edges[j]

                if b in children[a]: 
                    a, b = b, a

                if d in children[c]: 
                    c, d = d, c


                if c in children[a]: 
                    part1 = prefix[c]                  
                    part2 = prefix[a] ^ prefix[c]       
                    part3 = prefix[root] ^ prefix[a]  

                elif a in children[c]: 
                    part1 = prefix[a]                   
                    part2 = prefix[c] ^ prefix[a]       
                    part3 = prefix[root] ^ prefix[c]    

                else: 
                    part1 = prefix[a]                   
                    part2 = prefix[c]                  
                    part3 = prefix[root] ^ prefix[a] ^ prefix[c]   
                delta = max(part1, part2, part3) - min(part1, part2, part3)
                res = min(res, delta)

        return res
    
solution = Solution()
nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]
print(solution.minimumScore(nums,edges))