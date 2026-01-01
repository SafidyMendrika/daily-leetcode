class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        def poisk2():
            def dfs(i, p, n):
                ans = 0
                for next in sm2[i]:
                    if next != p:
                        ans += dfs(next, i, n + 1)
                return ans + n % 2

            return max(dfs(0, -1, 0), dfs(sm2[0][0], -1, 0))

        def poisk1():
            def dfs(i, p, n, fl):
                if fl and n % 2 == 0:
                    set1.add(i)
                ans = 0
                for next in sm1[i]:
                    if next != p:
                        ans += dfs(next, i, n + 1, fl)
                return ans + (n + 1) % 2

            a1 = dfs(0, -1, 0, True)
            a2 = dfs(sm1[0][0], -1, 0, False)
            for i in range(len(ans1)):
                if i in set1:
                    ans1[i] = a1
                else:
                    ans1[i] = a2

        ans1 = [1] * (len(edges1) + 1)
        set1 = set()

        sm1 = [[] for _ in range(len(edges1) + 1)]
        sm2 = [[] for _ in range(len(edges2) + 1)]

        for u, v in edges1:
            sm1[u].append(v)
            sm1[v].append(u)

        for u, v in edges2:
            sm2[u].append(v)
            sm2[v].append(u)

        max2 = poisk2()

        poisk1()
        for i in range(len(ans1)):
            ans1[i] += max2

        return ans1

solution = Solution()
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

print(solution.maxTargetNodes(edges1, edges2))  