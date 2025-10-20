from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        countPP = operations.count("++X") + operations.count("X++")
        countMM = operations.count("--X") + operations.count("X--")
        return countPP - countMM


solution = Solution()
operations = ["++X","++X","X++"]
print(solution.finalValueAfterOperations(operations))