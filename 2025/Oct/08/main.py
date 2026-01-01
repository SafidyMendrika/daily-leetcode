from typing import List
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []
        
        for spell in spells:
            required_potion = math.ceil(success / spell)
            
            if required_potion > potions[-1]:
                result.append(0)
                continue
            
            left, right = 0, n - 1
            position = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if potions[mid] >= required_potion:
                    position = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            result.append(n - position)
        
        return result
    
solution = Solution()
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(solution.successfulPairs(spells, potions, success))  