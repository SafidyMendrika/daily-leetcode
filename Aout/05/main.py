class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced
solution = Solution()
fruits = [4,2,5]
baskets = [3,5,4]
print(solution.numOfUnplacedFruits(fruits, baskets))