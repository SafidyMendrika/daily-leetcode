class Solution : 
    def getHappyString(self,n, k) :
        def backtrack(curr_str):
            if len(curr_str) == n:
                happy_strings.append(curr_str)
                return
            
            for char in ['a', 'b', 'c']:
                if not curr_str or curr_str[-1] != char:
                    backtrack(curr_str + char)
        
        happy_strings = []
        backtrack("")
        
        happy_strings.sort()
        
        return happy_strings[k-1] if k <= len(happy_strings) else ""
    
s = Solution()
n = 1, 
k = 3
print(s.getHappyString(n,k))