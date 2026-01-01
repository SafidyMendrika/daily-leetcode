class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff1 = abs(x - z)
        diff2 = abs(y - z)

        if diff1 < diff2:
            return 1
        elif diff2 < diff1:
            return 2
        else:
            return 0
        
solution = Solution()
x, y, z = 2, 5, 6
print(solution.findClosest(x, y, z))