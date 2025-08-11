class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=sorted(str(n))
        for i in range(31):
            if s==sorted(str(2**i)):
                return True
        return False
    
solution = Solution()
n = 1
print(solution.reorderedPowerOf2(n))