class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for el in s : 
            if el in "([{" :
                stack.append(el)
            else :
                if not stack or stack[-1] != self.invert(el) : return False
                else : stack.pop()
        
        return not stack
    
    def invert(self,c : str) : 
        if c == ")" : return '('
        if c == "(" : return ')'
        if c == "[" : return ']'
        if c == "]" : return '['
        if c == "{" : return '}'
        if c == "}" : return '{'
        return None

solution = Solution()
s = "()[]{}"
print(solution.isValid(s))