from functools import lru_cache
class Solution(object):
    def numberOfWays(self,n,x):
        p=[]
        l=int(pow(n,1.0/x))
        while (l+1)**x<=n:l+=1
        while l>0:
            p.append(l**x)
            l-=1
        m=10**9+7
        @lru_cache(None)
        def f(i,s):
            if s>n:return 0
            if s==n:return 1
            if i==len(p):return 0
            return (f(i+1,s+p[i])+f(i+1,s))%m
        return f(0,0)
    
solution = Solution()
n = 10
x = 2
print(solution.numberOfWays(n, x))