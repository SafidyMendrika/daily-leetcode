from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        totals = [row.count('1') for row in bank if row.count('1') > 0]
        result = 0
        for i in range(1, len(totals)):
            result += totals[i - 1] * totals[i]
        return result
    
solution = Solution()   
bank = ["011001","000000","010100","001000"]
print(solution.numberOfBeams(bank))