from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        b=["electronics","grocery","pharmacy","restaurant"]
        s=["!","@","#","$","^","&","*","(",")","+",".","?","/",">","<","=","-"]
        d={"electronics":[],"grocery":[],"pharmacy":[],"restaurant":[]}
        l=[]
        for i in range(0,len(code)):
            c=0
            if((businessLine[i] in b) and (isActive[i]==True)):
                a=code[i]
                if(a!=""):
                    for j in a:
                        if j in s:
                            break
                        else:
                            c=c+1
                    if(c==len(a)):
                       
                        d[businessLine[i]].append(a)
        for i in d:
            d[i].sort()
        for i in d:
            if(d[i]!=[]):
                l.extend(d[i])
        return l
    
solution = Solution()
code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]
print(solution.validateCoupons(code,businessLine,isActive))