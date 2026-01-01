class Solution:
    def countTriples(self, n: int) -> int:
        c = 0
        sq = [x**2 for x in range(1,n+1)]
        for i in range(1,n-1):
            for j in range(i+1,n):
                temp = (i**2 + j**2)
                if temp in sq:
                    c+=2
        return c
    
solution = Solution()
n = 5
print(solution.countTriples(n))