class Solution:
    def minMaxDifference(self, num: int) -> int:
        dig = list(str(num))
        a, b, flag = dig[0], dig[0], 0
        maxn, minn, n = 0, 0, len(dig)
        for i, x in enumerate(dig):
            if x != '9' and flag == 0:
                a = x
                flag = 1
                maxn += 9*10**(n-i-1)
            elif x == a:
                maxn += 9*10**(n-i-1)
            else:
                maxn += int(x)*10**(n-i-1)

            if x != b:
                minn += int(x)*10**(n-i-1)
                
        return maxn-minn
    
s = Solution()
num = 11891

print(s.minMaxDifference(11891))