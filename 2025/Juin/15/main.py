class Solution:
    def maxDiff(self, num: int) -> int:
        numStr = str(num)
        N = len(numStr)

        maxNumList = [digit for digit in numStr]
        minNumList = [digit for digit in numStr]
        xMax, yMax, xMin, yMin = None, None, None, None

        if numStr[0] != "1":
            xMin, yMin = numStr[0], "1"
            minNumList[0] = yMin

        for idx, digit in enumerate(numStr):
            if (xMax != None) and digit == xMax:
                maxNumList[idx] = yMax
            if (xMin != None) and digit == xMin:
                minNumList[idx] = yMin

            if (xMax == None) and digit != "9":
                xMax, yMax = digit, "9"
                maxNumList[idx] = yMax
                

            if (xMin == None):
                if digit != "1" and digit != "0":
                    xMin, yMin = digit, "0"
                    minNumList[idx] = yMin

        maxNum, minNum = int("".join(maxNumList)), int("".join(minNumList))
        return maxNum - minNum
    
s = Solution()
num = 555

print(s.maxDiff(num))