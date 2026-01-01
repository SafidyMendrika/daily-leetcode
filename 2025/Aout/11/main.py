class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:

        powers = []
        
        i = 1
        while i <= n:
            if (n & i) != 0: powers.append(i)
            i <<= 1

        ans = []
        MOD = 10 ** 9 + 7
        for left, right in queries:

            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD

            ans.append(product)
        return ans
    
solution = Solution()
n = 15
queries = [[0,1],[2,2],[0,3]]
print(solution.productQueries(n, queries))