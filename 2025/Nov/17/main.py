from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1
        for i, v in enumerate(nums):
            if v == 1:
                if last >= 0 and i - last - 1 < k:
                    return False
                last = i
        return True
        

solution = Solution()
nums = [1,0,0,0,1,0,0,1]
k = 2
print(solution.kLengthApart(nums,k))