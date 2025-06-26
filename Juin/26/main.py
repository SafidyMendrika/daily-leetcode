class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        cnt_zero = sum(1 if x == '0' else 0 for x in s)
        cur_sum = 0
        max_length = cnt_zero

        for i in range(n-1, -1, -1):
            if s[i] == '1':
                cur_sum += (1 << (n-1-i))
                if cur_sum <= k:
                    max_length += 1
                else:
                    break
        
        return max_length

    

solution = Solution()
s = "001101"
k = 5

print(solution.longestSubsequence(s,k))