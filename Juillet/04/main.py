class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        k -= 1
        
        bits = k.bit_length()        
        res = 0
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i]
        
        return chr(ord('a') + (res % 26))
    
solution = Solution()
k = 10
operations = [0,1,0,1]
print(solution.kthCharacter(k,operations))  