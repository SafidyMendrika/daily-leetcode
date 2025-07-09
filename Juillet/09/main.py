class Solution:
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        pre = 0
        space = []

        for i in range(len(startTime)):
            diff = startTime[i] - pre
            space.append(diff)
            pre = endTime[i]

        diff = eventTime - endTime[-1]
        space.append(diff)

        k += 1
        if k >= len(space):
            k = len(space)

        _sum = sum(space[:k])
        max_free = _sum

        for i in range(len(space) - k):
            _sum = _sum - space[i] + space[i + k]
            max_free = max(max_free, _sum)

        return max_free
    

solution = Solution()
eventTime = 5
k = 1
startTime = [1,3]
endTime = [2,5]

print(solution.maxFreeTime(eventTime, k, startTime, endTime)) 