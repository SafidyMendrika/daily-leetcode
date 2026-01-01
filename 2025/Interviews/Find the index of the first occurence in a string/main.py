class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

        
if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    s = Solution()
    print(s.strStr(haystack, needle  ))