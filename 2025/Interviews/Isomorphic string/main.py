class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


if __name__ == "__main__"  :
    s = "egg"
    t = "add"
    s = Solution()
    print(s.isIsomorphic(s, t))