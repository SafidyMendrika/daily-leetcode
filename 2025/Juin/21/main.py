from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word).values()
        res = float("inf")

        for i in freq:
            cur = 0
            for j in freq:
                cur += j if j < i else max(0, j - (i + k))
            res = min(res, cur)
        return res
    
solution = Solution()
word = "dabdcbdcdcd"
k = 2

print(solution.minimumDeletions(word,k))