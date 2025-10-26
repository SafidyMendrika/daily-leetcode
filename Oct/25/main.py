class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        # print(weeks)
        rem_days = n%7
        sum = 0
        i = 28
        for x in range(weeks):
            sum += i
            i += 7
        sum += (rem_days/2)*(2*(weeks+1)+(rem_days-1))

        return int(sum)
    
solution = Solution()
n = 4
print(solution.totalMoney(n))