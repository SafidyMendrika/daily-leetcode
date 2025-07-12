from collections import deque

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        min_round = n
        max_round = 0
        queue = deque([(list(range(1, n + 1)), 1)])
        
        while queue:
            arr, r = queue.pop()

            if len(arr) <= 2:
                if arr[0] == firstPlayer and arr[-1] == secondPlayer \
                    or arr[-1] == secondPlayer and arr[0] == firstPlayer:
                    min_round = min(min_round, r)
                    max_round = max(max_round, r)
                continue

            new_arr = [[]] if len(arr) % 2 == 0 else [[arr[len(arr) // 2]]]
            for i in range(len(arr) // 2):
                if arr[i] == firstPlayer and arr[len(arr) - i - 1] == secondPlayer \
                or arr[i] == secondPlayer and arr[len(arr) - i - 1] == firstPlayer:
                    min_round = min(min_round, r)
                    max_round = max(max_round, r)
                    continue

                stack = []
                if arr[i] == firstPlayer or arr[i] == secondPlayer:
                    for x in new_arr:
                        stack.append(x + [arr[i]])
                elif arr[len(arr) - i - 1] == firstPlayer or arr[len(arr) - i - 1] == secondPlayer:
                    for x in new_arr:
                        stack.append(x + [arr[len(arr) - i - 1]])
                else:
                    for x in new_arr:
                        stack.append(x + [arr[i]])
                        stack.append(x + [arr[len(arr) - i - 1]])
                new_arr = stack
            
            for arrs in new_arr:
                queue.append((sorted(arrs), r + 1))

        return [min_round, max_round]

solution = Solution()
n = 11
firstPlayer = 2
secondPlayer = 4
print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))