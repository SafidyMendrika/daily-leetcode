from collections import deque


class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        window = deque()
        curr = ans = 0

        def is_possible(window):
            left, right = window[0][0], window[-1][0]
            a = abs(startPos - left) + abs(left - right) 
            b = abs(startPos - right) + abs(left - right)  
            return min(a, b) <= k

        for idx, amt in fruits:
            window.append((idx, amt))
            curr += amt

            while window and not is_possible(window):
                curr -= window.popleft()[1] 

            ans = max(ans, curr)

        return ans
    
solution = Solution()
fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
print(solution.maxTotalFruits(fruits, startPos, k)) 