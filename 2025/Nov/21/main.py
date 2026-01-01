class Solution:
    def countPalindromicSubsequence(self, s: str) -> int: 
        out = 0
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = [i]
            else:
                freq[s[i]].append(i)

        for c in set(s):
            l = freq[c][0]
            r = freq[c][-1]
            if r-l >=2:
                out += len(set(s[l+1:r]))
        return out
                

solution = Solution()
s = "aabca"
print(solution.countPalindromicSubsequence(s))