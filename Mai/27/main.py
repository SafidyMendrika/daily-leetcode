class Solution(object):
    def differenceOfSums(self, n, m):
        total = n * (n + 1) // 2
        count = n // m
        sum_div_m = m * (count * (count + 1) // 2)
        return (total - sum_div_m) - sum_div_m

solution = Solution()        
n = 10
m = 3

print(solution.differenceOfSums(n, m))  # 19