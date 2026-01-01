class Solution : 
    def punishmentNumber(self,n):
        def can_partition(s, target, curr_sum=0, start=0):
            if start == len(s):
                return curr_sum == target
                
            for i in range(start, len(s)):
                if s[start] == '0' and i != start:
                    break
                    
                curr_num = int(s[start:i + 1])
                
                if curr_sum + curr_num > target:
                    break
                    
                if can_partition(s, target, curr_sum + curr_num, i + 1):
                    return True
                    
            return False

        total = 0
        for i in range(1, n + 1):
            square = i * i
            if can_partition(str(square), i):
                total += square
                
        return total

s = Solution()
print(s.punishmentNumber(10)) 
print(s.punishmentNumber(37))  