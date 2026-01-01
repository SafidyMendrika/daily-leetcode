class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        
        segment_start = [-1] * (length + 1)
        for idx in range(length):
            segment_start[idx + 1] = idx if idx == 0 or s[idx - 1] == "0" else segment_start[idx]
        
        total = 0
        for end in range(1, length + 1):
            zero_count = 0 if s[end - 1] == "1" else 1
            pos = end
            
            while pos > 0 and zero_count * zero_count <= length:
                one_count = (end - segment_start[pos]) - zero_count
                
                if one_count >= zero_count * zero_count:
                    valid_starts = one_count - zero_count * zero_count + 1
                    max_starts = pos - segment_start[pos]
                    total += min(max_starts, valid_starts)
                
                pos = segment_start[pos]
                zero_count += 1
        
        return total
    
solution = Solution()
s = "00011"
print(solution.numberOfSubstrings(s))