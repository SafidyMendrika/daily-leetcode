class Solution:
    def minNumberOperations(self, target):
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(target[i] - target[i - 1], 0)
        return ans
    


solution = Solution()
target = [1,2,3,2,1]
print(solution.minNumberOperations(target))