class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v="AEIOUaeiou"
        vowels=[c for c in s if c in v ]
        if len(vowels)!=0 or len(vowels)==1:
            return True
        else:
            return False
        
solution = Solution()
s = "bbcd"
print(solution.doesAliceWin(s))