class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = [] 

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return [] 
            ans.append([nums[i - 2], nums[i - 1], nums[i]])
        
        return ans
    
s = Solution()
nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k = 14

print(s.divideArray(nums,k))