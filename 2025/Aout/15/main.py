from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) % 1 == 0
        if n == 1:
            return True
        if n <= 0 or n % 4:
            return False
        
        return self.isPowerOfFour(n // 4)
    
solution = Solution()
n = 16
print(solution.isPowerOfFour(n))  