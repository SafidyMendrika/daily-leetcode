class Solution(object):
    def isArraySpecial(self,nums):
        if len(nums) == 1:
            return True

        for i in range(len(nums) - 1):
            if (nums[i] % 2 == nums[i + 1] % 2):  
                return False

        return True
        

if __name__ == "__main__":
    s = Solution()
    nums = [4,3,1,6]
    print(s.isArraySpecial(nums))