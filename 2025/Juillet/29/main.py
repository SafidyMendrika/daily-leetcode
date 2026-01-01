class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        len_bit = 30
        n = len(nums)
        pref = {}
        ans = [1] * n
        for i in range(n-1, -1, -1):
            b = 1
            for j in range(len_bit):
                if nums[i] & b:
                    pref[j] = i
                elif j in pref and pref[j] - i + 1 > ans[i]:
                    ans[i] = pref[j] - i + 1
                b += b
        return ans
    
solution = Solution()
nums = [1,0,2,1,3]
print(solution.smallestSubarrays(nums))