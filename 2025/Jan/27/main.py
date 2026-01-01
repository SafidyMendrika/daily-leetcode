from collections import defaultdict
from collections import deque
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        dp = [[False] * numCourses for _ in range(numCourses)]
        for i in range(numCourses):
            queue = deque()
            queue.append(i)
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if not dp[i][v]:
                        dp[i][v] = True
                        queue.append(v)
        res = []
        for u, v in queries:
            res.append(dp[u][v])
        return res
        

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    queries = [[0,1],[1,0]]
    solution = Solution()
    print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))