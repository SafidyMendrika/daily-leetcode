from typing import Counter


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        minX = min(basket1 + basket2)

        for key in count1.keys():
            while count1[key] > 0 and count2[key] > 0:
                min_count = min(count1[key], count2[key])
                count1[key] -= min_count
                count2[key] -= min_count
        for val in list(count1.values()) + list(count2.values()):
            if val % 2 == 1:
                return -1
        
        swap1 = []
        for key in count1.keys():
            swap1.extend([key] * (count1[key] // 2))

        swap2 = []
        for key in count2.keys():
            swap2.extend([key] * (count2[key] // 2))
            
        swap1, swap2 = sorted(swap1), sorted(swap2)[::-1]

        res = 0
        for i in range(len(swap1)):
            res += min(swap1[i], swap2[i], minX * 2)

        return res
    
solution = Solution()
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
print(solution.minCost(basket1, basket2))