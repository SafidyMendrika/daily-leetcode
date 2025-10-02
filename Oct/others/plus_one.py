from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = self.toNumber(digits)
        integer += 1
        return self.toArray(integer)
    
    def toNumber(self,digits : List[int]):
        return int("".join(map(str,digits)))
    
    def toArray(self, number : int) -> List[int] : 
        return list(map(int,list(str(number))))

solution = Solution()
digits = [1,2,3]
print(solution.plusOne(digits))