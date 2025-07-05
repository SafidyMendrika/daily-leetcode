from collections import Counter
class Solution:
    def findLucky(self,arr):

        freq = Counter(arr)
        luckyNum = -1

        for key, value in freq.items():
            if key == value:
                luckyNum = max(luckyNum, key)

        return luckyNum
    
solution = Solution()
arr = [1,2,2,3,3,3]
print(solution.findLucky(arr))  