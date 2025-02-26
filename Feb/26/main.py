class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = 0  
        min_sum = 0  
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)        
        return max(max_sum, abs(min_sum))
    
s = Solution()
nums = [1,-3,2,3,-4]
print(s.maxAbsoluteSum(nums))