from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)

        low, high = 0, total // n

        while low < high:
            mid = (low + high + 1) // 2

            usable = 0
            for b in batteries:
                usable += min(b, mid)
                if usable >= mid * n:
                    break

            if usable >= mid * n:
                low = mid
            else:
                high = mid - 1

        return low


solution = Solution()
n = 2
batteries = [3,3,3]
print(solution.maxRunTime(n,batteries))