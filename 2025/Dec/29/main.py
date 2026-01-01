from typing import List
from collections import defaultdict
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        def dfs(next_bottom, bottom):
            m, n = len(next_bottom), len(bottom)
            if n == 1:
                return True
            if m + 1 == n:
                if next_bottom in memo:
                    return False
                memo.add(next_bottom)    
                return dfs('', next_bottom)
            for ch in dic_allowed[bottom[m:m+2]]:
                if dfs(next_bottom + ch, bottom):
                    return True
            return False
        
        memo, dic_allowed = set(), defaultdict(list)
        for a, b, c in allowed:
            dic_allowed[a+b].append(c)
        return dfs('', bottom)