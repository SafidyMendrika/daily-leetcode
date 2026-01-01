class Solution(object):
    def maxAscendingSum(self, nums):
        max_sum = current_sum = nums[0]
    
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        

if __name__ == "__main__":
    nums = [12,17,15,13,10,11,12]
    s = Solution()
    print(s.maxAscendingSum(nums))