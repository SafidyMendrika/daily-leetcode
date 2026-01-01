class Solution:
    def maxOperations(self, s: str) -> int:
        total = 0
        ones = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1

                if s[i+1] == "0":
                    total += ones


        return total
    
solution = Solution()
s = "1001101"
print(solution.maxOperations(s))