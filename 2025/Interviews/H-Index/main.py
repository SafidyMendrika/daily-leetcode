class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        if n == 0:
            return 0
        citations.sort()
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
        

if __name__ == "__main__":
    citations = [3,0,6,1,5]
    s = Solution()
    print(s.hIndex(citations))