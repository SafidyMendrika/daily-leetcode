class Solution:
    def get_max_pos(self,s:str) -> list[int]:
        max_char = max(s)
        return [i for i,ch in enumerate(s) if ch == max_char]
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        pos = self.get_max_pos(word)
        best = ""

        for p in pos:
            if p >= numFriends:
                cur = word[p:]
            else:
                Char_Remove = numFriends - p - 1
                length = len(word) - p - Char_Remove 
                cur = word[p : p + length]
            best = max(best,cur)
        
        return best

solution = Solution()
word = "dbca"
numFriends = 2

print(solution.answerString(word, numFriends)) 