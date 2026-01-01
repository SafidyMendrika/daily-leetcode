class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        from collections import defaultdict; from math import inf
        g=defaultdict(list)
        for i,n in enumerate(nums): g[n%k].append(i)
        a,r=0,[]
        for rem in g: a=max(a,len(g[rem])); g[rem].append(inf); r.append(rem)
        for i in range(len(r)):
            for j in range(i+1,len(r)):
                x=y=c=0; last=-1
                while g[r[i]][x]!=g[r[j]][y]:
                    if g[r[i]][x]<g[r[j]][y]:
                        if last!=r[i]: c+=1; last=r[i]
                        x+=1
                    else:
                        if last!=r[j]: c+=1; last=r[j]
                        y+=1
                a=max(a,c)
        return max(a,2)

solution = Solution()
nums = [1,4,2,3,1,4]
k = 3
print(solution.maximumLength(nums, k))