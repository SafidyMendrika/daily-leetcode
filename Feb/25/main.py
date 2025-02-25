class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even_count = 1  
        odd_count = 0
        result = 0
        current_sum = 0
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                result = (result + odd_count) % MOD
                even_count += 1
        return result
    
s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
print(s.numOfSubarrays(arr))  