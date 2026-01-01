from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        known = [set(ls) for ls in languages]
        need = set()

        for u, v in friendships:
            u -= 1; v -= 1
            if known[u] & known[v]:
                continue
            need.add(u); need.add(v)

        if not need:
            return 0

        ans = float('inf')
        for lang in range(1, n + 1):
            cnt = sum(1 for person in need if lang not in known[person])
            ans = min(ans, cnt)
        return ans
    
solution = Solution()
n = 3
languages = [[2],[1,3],[1,2],[3]]
friendships = [[1,4],[1,2],[3,4],[2,3]]
print(solution.minimumTeachings(n,languages,friendships))