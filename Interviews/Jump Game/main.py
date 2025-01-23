class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True

        
if "__main__" == __name__ : 
    s = Solution()
    nums = [3,2,1,0,4]
    print(s.canJump(nums))