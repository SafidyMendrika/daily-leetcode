class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        nums_with_indices = [(num, i) for i, num in enumerate(nums)]
        
        nums_with_indices.sort(key=lambda x: -x[0])
        
        top_k = sorted(nums_with_indices[:k], key=lambda x: x[1])
        
        return [num for num, _ in top_k]

solution = Solution()
nums = [3,4,3,3]
k = 2


print(solution.maxSubsequence(nums,k))