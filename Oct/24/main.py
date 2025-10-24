from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def backtracking(i, numLen, curNum, counter):
            if i == numLen:
                isBalanceNumber = True
                for d, freq in counter.items():
                    if freq != 0 and d != freq:
                        isBalanceNumber = False
                if isBalanceNumber:
                    yield curNum
                return

            for d in range(1, numLen+1):
                if counter[d] >= d: continue   
                if counter[d] + (numLen - i) < d: continue  
                counter[d] += 1
                yield from backtracking(i + 1, numLen, curNum * 10 + d, counter)
                counter[d] -= 1

        for numLen in range(len(str(n)), len(str(n)) + 2):
            for num in backtracking(0, numLen, 0, Counter()):
                if num > n:
                    return num
                

solution = Solution()
n = 1000
print(solution.nextBeautifulNumber(n)) 