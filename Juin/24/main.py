class Solution:
    def findKDistantIndices(self, nums : list[int], key : int, k : int):
        index = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    index.append(i)
                    break
        return index

solution = Solution()
nums = [2,2,2,2,2]
key = 2
k = 2

print(solution.findKDistantIndices(nums,key,k))