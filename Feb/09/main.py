class Solution(object):
    def countBadPairs(self,nums) :
        n = len(nums)
        total_pairs = (n * (n - 1)) // 2
        
        value_count = {}
        
        for i in range(n):
            diff = nums[i] - i
            value_count[diff] = value_count.get(diff, 0) + 1
        
        good_pairs = 0
        for count in value_count.values():
            good_pairs += (count * (count - 1)) // 2
        
        return total_pairs - good_pairs
        
if __name__ == "__main__":
    s = Solution()
    nums = [4,1,3,3]
    print(s.countBadPairs(nums))