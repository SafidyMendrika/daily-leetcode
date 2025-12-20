from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        count = 0

        for col in range(n):
            for row in range(m - 1):
                if strs[row][col] > strs[row + 1][col]:
                    count += 1
                    break
        return count
    
solution = Solution()
strs = ["cba","daf","ghi"]
print(solution.minDeletionSize(strs))