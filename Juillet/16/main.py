class Solution:
    def isValid(self, word: str) -> bool:
        if not word.isalnum():
            return False
        
        n = len(word)
        if n < 3:
            return False
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        vowel = False
        cons = False

        for c in word:
            if c.isalpha():
                if c in vowels:
                    vowel = True
                else:
                    cons = True
        
        return vowel and cons
solution = Solution()
print(solution.isValid("234Adas")) 
