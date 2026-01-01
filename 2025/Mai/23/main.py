class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        n = len(nums)
        
        benefits = []
        for i in range(n):
            benefit = (nums[i] ^ k) - nums[i]
            benefits.append(benefit)
        
        benefits.sort(reverse=True)
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + benefits[i]
        
        max_sum = sum(nums) 
        
        for count in range(2, n + 1, 2):
            if prefix_sum[count] > 0: 
                current_sum = sum(nums) + prefix_sum[count]
                max_sum = max(max_sum, current_sum)
        
        return max_sum



solution = Solution()

nums= [7, 7, 7, 7, 7, 7]
k = 3
edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
result = solution.maximumValueSum(nums, k, edges)
print(f" {result}")