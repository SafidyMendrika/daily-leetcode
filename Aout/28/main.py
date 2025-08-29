class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odd = (n + 1) // 2    
        even = m // 2         
        odd1 = (m + 1) // 2   
        even1 = n // 2        

        return odd1 * even1 + odd * even
    
solution = Solution()
n = 3
m = 2
print(solution.flowerGame(n, m)) 