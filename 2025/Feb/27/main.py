class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        s = set(arr)
        max_length = 0
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                length = 2  
                while a + b in s:
                    a, b = b, a + b
                    length += 1
                    max_length = max(max_length, length)
        return max_length if max_length >= 3 else 0
    
s = Solution()
arr = [1,3,7,11,12,14,18]
print(s.lenLongestFibSubseq(arr))