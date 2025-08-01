class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        res = []
        s = 1
        for i in arr:
            n = len(res)
            res.append(i)
            for j in range(s, n):
                v = res[j] | i
                if (res[-1] != v):
                    res.append(v)
            s = n
        return len(set(res))
    

solution = Solution()
arr = [1, 2, 4]
print(solution.subarrayBitwiseORs(arr)) 