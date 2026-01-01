class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        p,N=0,len(nums)
        count=0

        for i in range(N):
            if nums[i]-nums[p] <= k:
                continue
            else:
                p=i
                count+=1
        
        if nums[N-1] - nums[p] <=k:
            count+=1

        return count

s = Solution()
nums = [2,2,4,5]
k = 0

print(s.partitionArray(nums,k))