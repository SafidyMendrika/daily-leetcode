class Solution:
    def numberOfWays(self, corridor: str) -> int:
        fa = {
            (0,'P'): (0,0), (0,'S'): (0,1),
            (1,'P'): (0,1), (1,'S'): (1,2),
            (2,'P'): (2,2), (2,'S'): (0,1),
        }
        ans,p,state,MOD = 1, 0, 0, int(1e9+7)
        for inp in corridor:
            act,state = fa[(state,inp)]
            if  act==1: ans = ans * (p+1) %MOD;  p=0
            if  act==2: p  += 1
        return  ans  if state==2  else 0
    
solution = Solution()
corridor = "SSPPSPS"
print(solution.numberOfWays(corridor))