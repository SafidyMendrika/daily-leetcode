class Solution(object):
    def smallestNumber(self,pattern):
        n = len(pattern)
        result = [0] * (n + 1)
        used = set()  
        
        def canPlace(pos, num, prev_num):
            if num in used:
                return False
            
            if pos == 0:
                return True
                
            if pattern[pos-1] == 'I' and num <= prev_num:
                return False
            if pattern[pos-1] == 'D' and num >= prev_num:
                return False
                
            return True
        
        def backtrack(pos):
            if pos == n + 1:
                return True
                
            for num in range(1, 10):
                prev_num = result[pos-1] if pos > 0 else 0
                
                if canPlace(pos, num, prev_num):
                    result[pos] = num
                    used.add(num)
                    
                    if backtrack(pos + 1):
                        return True
                        
                    used.remove(num)
                    result[pos] = 0
                    
            return False
        
        backtrack(0)
        
        return ''.join(map(str, result))
    

s = Solution()

print(s.smallestNumber("IIIDIDDD"))