class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while (True):

            if (num1 == 0 or num2 == 0):
                break

            if (num1 >= num2):
                num1 -= num2
            else:
                num2 -= num1

            count += 1

        return count 
        

solution = Solution()
num1 = 2
num2 = 3
print(solution.countOperations(num1,num2))