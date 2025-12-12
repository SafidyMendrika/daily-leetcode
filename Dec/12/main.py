from collections import deque
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        off = deque()
        point_c = [0] * numberOfUsers
        all_c = 0
        on_c = 0
        for m, t, ids in events:
            t = int(t)
            while off and off[0][0] <= t:
                _, id, l_on = off.popleft() 
                point_c[id] -= on_c - l_on

            if m == "MESSAGE":
                for id in ids.split(' '):
                    if id == "HERE":
                        on_c += 1
                    elif id == "ALL":
                        all_c += 1
                    else:
                        point_c[int(id[2:])] += 1
            else:
                off.append((t+60, int(ids), on_c))
        
        while off:
            _, id, l_on = off.popleft() 
            point_c[id] -= on_c - l_on
        return [c + all_c + on_c for c in point_c]
    
solution = Solution()
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
print(solution.countMentions(numberOfUsers,events))