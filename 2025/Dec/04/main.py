class Solution:
    def countCollisions(self, directions: str) -> int:
        
        ans = 0
        stack = []

        for ch in directions:
            if not stack:
                stack.append(ch)
            else:
                top = stack[-1]

                if top == 'R' and ch == 'L':
                    ans += 2
                    stack.pop()
                    ch = 'S'
                elif top == 'R' and ch == 'S':
                    ans += 1
                    stack.pop()
                    ch = 'S'
                elif top == 'S' and ch == 'L':
                    ans += 1
                    stack.pop()
                    ch = 'S'
                while stack and (stack[-1] == 'R' and ch == 'S'):
                    ans += 1
                    stack.pop()
                stack.append(ch)
        return ans
    

solution = Solution()
directions = "RLRSLL"
print(solution.countCollisions(directions))