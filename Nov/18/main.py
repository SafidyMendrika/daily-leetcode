class Solution:
    def isOneBitCharacter(self, bits):
    
        current_index = 0
        array_length = len(bits)
      
        while current_index < array_length - 1:
            current_index += bits[current_index] + 1

        return current_index == array_length - 1

solution = Solution()
bits = [1,0,0]
print(solution.isOneBitCharacter(bits))