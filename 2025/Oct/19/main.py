from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        res = s
        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            res = min(res, curr)
            s1 = list(curr)
            for i in range(1, len(s1), 2):
                s1[i] = str((int(s1[i]) + a) % 10)
            s1 = ''.join(s1)
            s2 = curr[-b:] + curr[:-b]
            queue.extend([s1, s2])
        return res
    

solution = Solution()
s = "5525"
a = 9
b = 2
print(solution.findLexSmallestString(s, a, b))  