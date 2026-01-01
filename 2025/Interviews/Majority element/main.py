class Solution(object):
    def majorityElement(self, nums : list[int]):
        nums.sort()
        return nums[len(nums)//2]

        

if __name__ == '__main__':
    s = Solution()

    print(s.majorityElement([1,2,3,4,5]))
    print(s.majorityElement([1,2,2,2,1]))