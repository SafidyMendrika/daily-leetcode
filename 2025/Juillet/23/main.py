class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, value):
            stack = []
            cnt = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    cnt += value
                else:
                    stack.append(ch)
            return ''.join(stack), cnt
        
        if x >= y:
            s, count1 = remove_pair(s, 'a', 'b', x)
            _, count2 = remove_pair(s, 'b', 'a', y)
        else:
            s, count1 = remove_pair(s, 'b', 'a', y)
            _, count2 = remove_pair(s, 'a', 'b', x)
        return count1 + count2
    
solution = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
print(solution.maximumGain(s,x,y))