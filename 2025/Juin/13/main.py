class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        
        def countPairs(x):
            count = 0
            i = 0
            while i < len(nums) -1:
                if nums[i+1] - nums[i] <= x:
                    count += 1
                    i+= 2
                else:
                    i+= 1
            return count

        nums.sort()
        l, r = 0, (nums[-1] - nums[0])
        res = r

        while l <= r:
            m = (l + r) // 2
            if countPairs(m) >= p:
                res = m
                r = m -1
            else:
                l = m + 1

        return res
    
s = Solution()
nums = [10,1,2,7,1,3]
p = 2

print(s.minimizeMax(nums,p))