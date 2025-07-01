class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        count = 1
        last = word[0]

        for i in range(1, len(word)):
            if word[i] != last:
                ans += count - 1
                count = 1
                last = word[i]
            else:
                count += 1

        ans += count - 1
        return ans

solution = Solution()
word  = "abbcccc"

print(solution.possibleStringCount(word)) 