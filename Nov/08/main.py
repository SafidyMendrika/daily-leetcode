class Solution(object):
    def minimumOneBitOperations(self, n):
        if n==0:
            return 0
        
        k=0
        while 2**k<=n:
            k+=1
        k-=1

        return 2**(k+1)-1 - self.minimumOneBitOperations(2**k ^ n)
    
solution = Solution()
n = 3

print(solution.minimumOneBitOperations(n))