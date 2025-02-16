class Solution : 
    def constructDistancedSequence(self,n):
        length = 2 * n - 1  
        result = [0] * length  
        used = [False] * (n + 1)  
        
        def backtrack(pos):
            if pos >= length:
                return True
                
            if result[pos] != 0:
                return backtrack(pos + 1)
                
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                    
                if num > 1:
                    if pos + num >= length or result[pos + num] != 0:
                        continue
                        
                    result[pos] = num
                    result[pos + num] = num
                    used[num] = True
                    
                    if backtrack(pos + 1):
                        return True
                        
                    result[pos] = 0
                    result[pos + num] = 0
                    used[num] = False
                else:
                    result[pos] = num
                    used[num] = True
                    
                    if backtrack(pos + 1):
                        return True
                        
                    result[pos] = 0
                    used[num] = False
                    
            return False
        
        backtrack(0)
        return result


s = Solution()
print(s.constructDistancedSequence(3)) 
print(s.constructDistancedSequence(5)) 