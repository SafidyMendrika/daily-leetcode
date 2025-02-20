class Solution : 
    def findDifferentBinaryString(self,nums):
        n = len(nums)
        result = ""
        
        for i in range(n):
            bit = nums[i][i]
            result += '1' if bit == '0' else '0'
        
        return result
    

nums = ["01","10"]
s = Solution()
print(s.findDifferentBinaryString(nums))