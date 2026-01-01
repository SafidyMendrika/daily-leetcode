class Solution(object):
    def numTilePossibilities(self,tiles) :
        char_count = {}
        for tile in tiles:
            char_count[tile] = char_count.get(tile, 0) + 1
        
        def backtrack(counter):
            total = 0
            
            for char in counter:
                if counter[char] > 0:
                    total += 1
                    
                    counter[char] -= 1
                    
                    total += backtrack(counter)
                    
                    counter[char] += 1
                    
            return total
        
        return backtrack(char_count)
    

s = Solution()
print(s.numTilePossibilities("AAB")) 
