class Solution(object):
    def isHappy(self, n,epsilon=999):
        
        powered_sum = sum([pow(int(e),2) for e in str(n)])
        if powered_sum == 1 : return True

        if epsilon == 0 : return False
        
        return self.isHappy(powered_sum,epsilon=epsilon-1)
        
if __name__ == "__main__":
    n = 1111111
    s = Solution()
    print(s.isHappy(n))