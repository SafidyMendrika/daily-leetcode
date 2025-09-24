class Solution:
    def fractionToDecimal(self,n: int, d: int) -> str:
        if n == 0: return "0"  
        res = "-" if (n < 0) ^ (d < 0) else ""
        n, d = abs(n), abs(d)
        res += str(n // d)
        n %= d
        if not n: return res  
        res += "."
        seen = {}
        while n:
            if n in seen:  
                return res[:seen[n]] + "(" + res[seen[n]:] + ")"
            seen[n] = len(res)
            n *= 10
            res += str(n // d)
            n %= d
        return res


solution = Solution()
numerator = 1
denominator = 2

print(solution.fractionToDecimal(numerator, denominator))  