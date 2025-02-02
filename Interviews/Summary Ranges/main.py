class Solution(object):
    def summaryRanges(self,nums):
        if not nums:
            return []
    
        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]

        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, nums[-1]))

        return ranges
        
if __name__ == "__main__":
    s = Solution()
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))
    