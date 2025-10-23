class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s) != 2):

            temp = ""

            i = 0
            while(i < len(s) - 1):
                
                temp += str((int(s[i]) + int(s[i + 1])) % 10)
                i += 1

            s = temp

        if(s[0] == s[1]):
            return True
        else:
            return False

solution = Solution()
s = "3902"
print(solution.hasSameDigits(s))