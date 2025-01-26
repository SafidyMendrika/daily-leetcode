class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                return False
        return True
        

if __name__ == '__main__':
    ransomNote = "a"
    magazine = "b"
    s = Solution()
    print(s.canConstruct(ransomNote, magazine))