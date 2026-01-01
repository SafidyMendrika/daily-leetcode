from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        checklist = range(len(strs) - 1)
        for j in range(len(strs[0])):
            new_checklist = []
            for i in checklist:
                if strs[i][j] > strs[i+1][j]:
                    res += 1
                    break
                elif strs[i][j] == strs[i+1][j]:
                    new_checklist.append(i)
            else:
                if not new_checklist:
                    return res
                checklist = new_checklist
        return res
    
solution = Solution()
strs = ["ca","bb","ac"]
print(solution.minDeletionSize(strs))