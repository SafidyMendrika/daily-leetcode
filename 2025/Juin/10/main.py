from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = float('-inf')
        min_even = float('inf')

        for count in freq.values():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        if max_odd == float('-inf') or min_even == float('inf'):
            return 0

        return max_odd - min_even


solution = Solution()
s = "aaaaabbc"

print(solution.maxDifference(s))  