class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        words = text.split(' ')
        cnt = 0

        for word in words:
            possible = True
            for ch in word:
                if ch in brokenLetters:
                    possible = False
            if possible:
                cnt += 1
        return cnt

solution = Solution()        
text = "hello world"
brokenLetters = "ad"
print(solution.canBeTypedWords(text,brokenLetters))