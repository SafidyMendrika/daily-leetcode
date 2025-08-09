class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i < n:
            i +=1
        return 2**i == n
    

solution = Solution()
print(solution.isPowerOfTwo(1)) 
print(solution.isPowerOfTwo(16)) 
print(solution.isPowerOfTwo(3)) 