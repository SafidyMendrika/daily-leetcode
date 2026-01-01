class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 1_000_000_007

        if k > len(word):
            return 0

        li = []
        last = None
        count = 0
        for v in word:
            if v != last:
                li.append((last,count))
                last = v
                count = 0
            else:
                count += 1
        li.append((last,count))
        li = li[1:]
        m = len(li)

        tot = 1
        for c,v in li:
            tot *= v+1
            tot %= MOD


        k -= m
        if k <= 0:
            return tot

        dp = [1]*k
        for i,(c,v) in enumerate(li):
            lastdp = dp.copy()
            dp = [0]*k
            isum = 0
            for j in range(k):
                isum += lastdp[j]
                lastdp[j] = isum
            for j in range(k):
                dp[j] = lastdp[j]
                if j-v-1 >= 0:
                    dp[j] -= lastdp[j-v-1]
                dp[j] %= MOD

        return (tot-dp[-1]) % MOD
    
solution = Solution()
word = "aaabbb"
k = 3
print(solution.possibleStringCount(word, k))  