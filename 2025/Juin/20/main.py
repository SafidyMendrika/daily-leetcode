class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        nh = sh = et = wt = 0
        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                nh += 1
            elif c == 'S':
                sh += 1
            elif c == 'E':
                et += 1
            elif c == 'W':
                wt += 1
            x = abs(nh - sh)
            y = abs(et - wt)
            d = x + y
            dis = d + min(2 * k, i + 1 - d)
            ans = max(ans, dis)
        return ans
    
solution = Solution()
s = "NWSE"
k = 1

print(solution.maxDistance(s,k))