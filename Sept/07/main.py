class Solution:
    def sumZero(self, n: int) -> list[int]:
        return [-sum(a:=range(1,n)),*a]
    
solution = Solution()
n = 3
print(solution.sumZero(n))