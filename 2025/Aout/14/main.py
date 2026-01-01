
from collections import deque


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        window = deque(num[:3])

        result = []
        if window[0] == window[1] == window[2]:
            result = list(window)
        for i in range(3, len(num)):

            window.popleft()
            window.append(num[i])
            if window[0] == window[1] == window[2]:
                if not result:
                    result = list(window)
                else:
                    if window[0] > result[0]:
                        result = list(window)
        return ''.join(list(result))


solution = Solution()
num = "6777133339"
print(solution.largestGoodInteger(num))