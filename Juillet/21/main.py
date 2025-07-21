class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s

        i=0
        while i + 2 < len(s):
            if s[i] == s[i+1] == s[i+2]:
                s = s[:i+2] + s[i+3:] 
            else:
                i += 1
        return s
solution = Solution()
s = "aaabaaaa"
print(solution.makeFancyString(s))