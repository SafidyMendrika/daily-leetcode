
from typing import List
import math
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        first, second = -math.inf, -math.inf
        count = 0

        for interval in intervals:
            start = interval[0]
            end = interval[-1]
            if not (start <= second <= end): # no overlap
                count += 2
                first = end - 1
                second = end
            elif not (start <= first <= end):
                count += 1
                first = min(second, end-1) 
                second = end
        return count
    
solution = Solution()
intervals = [[1,3],[3,7],[8,9]]
print(solution.intersectionSizeTwo(intervals))