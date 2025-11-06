from typing import List

class Solution:                    
    def processQueries(self, c: int, connections, queries) -> List[int]:
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        parent = list(range(c + 1))
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb: parent[rb] = ra

        next_node, comp_min, last = [0] * (c + 1), [0] * (c + 1), {}
        for i in range(1, c + 1):
            r = find(i)
            if comp_min[r] == 0: comp_min[r] = i
            else: next_node[last[r]] = i
            last[r] = i

        offline, res = [False] * (c + 1), []
        for t, x in queries:
            if t == 1:
                if not offline[x]: res.append(x)
                else:
                    r, m = find(x), comp_min[find(x)]
                    res.append(m if m else -1)
            else:
                if offline[x]: continue
                offline[x], r = True, find(x)
                if comp_min[r] == x:
                    y = next_node[x]
                    while y and offline[y]: y = next_node[y]
                    comp_min[r] = y
        return res

solution = Solution()
c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
print(solution.processQueries(c,connections,queries))