
class Solution(object):
    def eventualSafeNodes(self, graph):
        def dfs(i):
            if color[i] != 0:
                return color[i] == 1
            color[i] = 2
            for j in graph[i]:
                if not dfs(j):
                    return False
            color[i] = 1
            return True

        color = [0] * len(graph)
        return [i for i in range(len(graph)) if dfs(i)]
        

if __name__ == '__main__':
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    s = Solution()
    print(s.eventualSafeNodes(graph))