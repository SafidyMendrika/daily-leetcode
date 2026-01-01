class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []
        for i in range(0, len(s), k):
            chunk = s[i:i+k]
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))
            result.append(chunk)
        return result
    

solution = Solution()
s = "abcdefghi"
k = 3
fill = "x"

print(solution.divideString(s,k,fill))