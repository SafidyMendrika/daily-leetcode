from bisect import bisect_right
from sortedcontainers import SortedList
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res, full, dry = [-1]*len(rains), {}, SortedList()
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.add(i)
                res[i] = 1
            elif lake in full:
                j = dry.bisect_right(full[lake])
                if j == len(dry):
                    return []
                res[dry[j]] = lake
                dry.pop(j)
                full[lake] = i
            else:
                full[lake] = i
        return res
    
solution =  Solution()
rains = [1,2,0,0,2,1]
print(solution.avoidFlood(rains))