import bisect
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x : (x[0], x[1]))
        n = len(events)
        start = [e[0] for e in events]
        suffix = [0] * n
        suffix[-1] = events[-1][2]
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], events[i][2])

        res = 0
        for i in range(n):
            idx = bisect.bisect_left(start, events[i][1] + 1)
            val = events[i][2]
            if idx < n:
                val += suffix[idx]
            res = max(res, val)
        return res

solution = Solution()
events = [[1,3,2],[4,5,2],[2,4,3]]
print(solution.maxTwoEvents(events))