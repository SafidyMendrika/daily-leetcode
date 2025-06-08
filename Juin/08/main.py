class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []
        current = 1 

        for _ in range(n):
            ans.append(current) 

            if current * 10 <= n:
                current *= 10
            else:
                while current % 10 == 9 or current + 1 > n:
                    current //= 10 
                current += 1  

        return ans


solution = Solution()
n = 13

print(solution.lexicalOrder(n))  