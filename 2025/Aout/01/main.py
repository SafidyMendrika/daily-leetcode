class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l=[[1]]
        for i in range(1,numRows):
            p=l[-1]
            t=[1]
            for j in range(1,i):
                t.append(p[j-1]+p[j])
            t.append(1)
            l.append(t)
        return l
    
solution = Solution()
numRows = 5
print(solution.generate(numRows))