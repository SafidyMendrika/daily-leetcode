from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        a=''
        l=[]
        for i in nums:
            a+=str(i)
            v=int(a,2)
            if v%5==0:
                l.append(True)
            else:
                l.append(False)
        return l
    
solution = Solution()
nums = [0,1,1]
print(solution.prefixesDivBy5(nums))