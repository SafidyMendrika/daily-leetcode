class Solution(object):
    def wordPattern(self,pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for p, w in zip(pattern, words):
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False
            if w in word_to_char:
                if word_to_char[w] != p:
                    return False
            
            char_to_word[p] = w
            word_to_char[w] = p
        
        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    sol = Solution()
    print(sol.wordPattern(pattern,s))
        