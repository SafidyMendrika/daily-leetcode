from collections import Counter
class Solution(object):

    def isAnagram(self,s, t):
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
        
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s,t))