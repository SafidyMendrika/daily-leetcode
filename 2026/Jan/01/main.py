from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        
        rem=0
        digits[-1]+=1
        for i in range(n-1,-1,-1):
            Sum=rem+digits[i]
            digits[i]=(Sum%10) 
            rem=Sum//10
        
        if rem:
            digits.insert(0,rem)
        return digits

        

solution = Solution()
digits = [1,2,3]
print(solution.plusOne(digits))