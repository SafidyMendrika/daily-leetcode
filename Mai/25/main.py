from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):   
        count = Counter(words)
        
        length = 0
        has_center = False
        
        for word in count:
            freq = count[word]
            
            if word[0] == word[1]:  
                pairs = freq // 2
                length += pairs * 4  
                
                if freq % 2 == 1 and not has_center:
                    has_center = True
                    length += 2 
                    
            else:  
                reverse_word = word[::-1]  
                
                if reverse_word in count and word < reverse_word:
                    pairs = min(freq, count[reverse_word])
                    length += pairs * 4  
        
        return length
    

solution = Solution()
    
words = ["lc","cl","gg"]
result = solution.longestPalindrome(words)
print(result)  