from typing import List

class Solution:
  def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    appleSum = sum(apple)
    capacitySum = 0

    for i, c in enumerate(sorted(capacity, reverse=True)):
      capacitySum += c
      if capacitySum >= appleSum:
        return i + 1

    return len(capacity)
  

solution = Solution()
apple = [1,3,2]
capacity = [4,3,1,5,2]
print(solution.minimumBoxes(apple,capacity))