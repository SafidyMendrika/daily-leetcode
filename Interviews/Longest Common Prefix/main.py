class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) == 0:
            return prefix
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))