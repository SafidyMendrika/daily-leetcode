class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        if n == 1:
            return 1
        candies = [1 for i in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
        
if "__main__" == __name__:
    ratings = [1,0,2]
    s = Solution()
    print(s.candy(ratings))