class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        for i, j in conflictingPairs:
            right[max(i, j)].append(min(i, j))

        res = 0
        left = [0, 0]
        prefix = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            res += r - left[0]

            if left[0] > 0:
                prefix[left[0]] += left[0] - left[1]
        return res + max(prefix)
solution = Solution()
n = 5
conflictingPairs = [[1,2],[2,5],[3,5]]
print(solution.maxSubarrays(n,conflictingPairs))