class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    string = "A man, a plan, a canal: Panama"
    print( s.isPalindrome(string))