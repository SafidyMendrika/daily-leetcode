from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        total = 0
        dec = 0
        i = len(happiness) - 1

        while k > 0 and i >= 0:
            curr = happiness[i] - dec
            if curr <= 0:
                break
            total += curr
            dec += 1
            i -= 1
            k -= 1

        return total

solution = Solution()
happiness = [1,2,3]
k = 2
print(solution.maximumHappinessSum(happiness,k))