import regex

class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
        

if __name__ == "__main__":
    s = Solution()
    string = "the sky is blue"
    print(s.reverseWords(string))